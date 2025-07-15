import requests
import os
import torch

# --- Data Acquisition ---
# We'll use "Pride and Prejudice" by Jane Austen as our training data.
# It's in the public domain and a good size for a micro-model.

data_dir = 'micro-llm/data'
file_path = os.path.join(data_dir, 'pride_and_prejudice.txt')
url = 'https://www.gutenberg.org/files/1342/1342-0.txt'

if not os.path.exists(file_path):
    print("Downloading training data...")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # The book text starts after a header and ends before a footer.
        # We'll do a simple cleanup to get the main content.
        text = response.text
        start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE ***"
        end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE ***"
        
        start_index = text.find(start_marker)
        if start_index != -1:
            start_index += len(start_marker)
            
        end_index = text.find(end_marker, start_index)
        
        if start_index != -1 and end_index != -1:
            text = text[start_index:end_index].strip()
        else:
            print("Warning: Could not find start/end markers. Using full text.")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Data saved to {file_path}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")
        exit()
else:
    print("Training data already exists.")

# Load the text data
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded {len(text)} characters of text.")

# --- Tokenization ---
# We'll use a simple character-level tokenizer.
# This means every character is a token.

# Get all unique characters in the text
chars = sorted(list(set(text)))
vocab_size = len(chars)
print(f"Vocabulary size: {vocab_size}")
print(f"Vocabulary: {''.join(chars)}")

# Create a mapping from characters to integers (and vice-versa)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }

# Encoder: take a string, output a list of integers
def encode(s):
    return [stoi[c] for c in s]

# Decoder: take a list of integers, output a string
def decode(l):
    return ''.join([itos[i] for i in l])

# Test the tokenizer
test_string = "hello world"
encoded_test = encode(test_string)
decoded_test = decode(encoded_test)
print(f"\nTesting tokenizer:")
print(f"Original: '{test_string}'")
print(f"Encoded: {encoded_test}")
print(f"Decoded: '{decoded_test}'")
assert test_string == decoded_test

# --- Hyperparameters ---
batch_size = 32 # How many independent sequences will we process in parallel?
block_size = 8 # What is the maximum context length for predictions?

# --- Data Loading ---
# Let's now split up the data into a training and a validation set
data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data)) # first 90% will be train, rest val
train_data = data[:n]
val_data = data[n:]

def get_batch(split):
    # generate a small batch of data of inputs x and targets y
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x, y

# See an example of a batch
xb, yb = get_batch('train')
print("\n--- Example Batch ---")
print("inputs:")
print(xb.shape)
print(xb)
print("targets:")
print(yb.shape)
print(yb)
print("--------------------")

# --- Model Architecture ---
import torch.nn as nn
from torch.nn import functional as F

class Head(nn.Module):
    """ one head of self-attention """
    def __init__(self, head_size):
        super().__init__()
        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)
        q = self.query(x)
        wei = q @ k.transpose(-2,-1) * C**-0.5
        wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf'))
        wei = F.softmax(wei, dim=-1)
        v = self.value(x)
        out = wei @ v
        return out

class MultiHeadAttention(nn.Module):
    """ multiple heads of self-attention in parallel """
    def __init__(self, num_heads, head_size):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size) for _ in range(num_heads)])
        self.proj = nn.Linear(n_embd, n_embd)

    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        out = self.proj(out)
        return out

class FeedForward(nn.Module):
    """ a simple linear layer followed by a non-linearity """
    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd, n_embd),
        )

    def forward(self, x):
        return self.net(x)

class Block(nn.Module):
    """ Transformer block: communication followed by computation """
    def __init__(self, n_embd, n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size)
        self.ffwd = FeedForward(n_embd)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x):
        x = x + self.sa(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x

class MicroLLM(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.position_embedding_table = nn.Embedding(block_size, n_embd)
        self.blocks = nn.Sequential(*[Block(n_embd, n_head=n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        tok_emb = self.token_embedding_table(idx)
        pos_emb = self.position_embedding_table(torch.arange(T))
        x = tok_emb + pos_emb
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
            loss = F.cross_entropy(logits, targets)
        return logits, loss

    def generate(self, idx, max_new_tokens):
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -block_size:]
            logits, loss = self(idx_cond)
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)
            idx = torch.cat((idx, idx_next), dim=1)
        return idx

# --- Hyperparameters for the model ---
n_embd = 32
n_head = 4
n_layer = 3

# --- Create the model ---
model = MicroLLM()
logits, loss = model(xb, yb)
print("\n--- Model Output ---")
print("Logits shape:", logits.shape)
print("Initial loss:", loss.item())

# Test generation
print("\n--- Test Generation ---")
context = torch.zeros((1, 1), dtype=torch.long)
generated_output = model.generate(context, max_new_tokens=100)[0].tolist()
print(decode(generated_output))
print("----------------------")

# --- Training the model ---
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)

for steps in range(10000):
    # sample a batch of data
    xb, yb = get_batch('train')

    # evaluate the loss
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

    if steps % 1000 == 0:
        print(f"Step {steps}, Loss: {loss.item()}")

# --- Final Generation ---
print("\n--- Generating after training ---")
context = torch.zeros((1, 1), dtype=torch.long)
generated_output = model.generate(context, max_new_tokens=500)[0].tolist()
print(decode(generated_output))
print("---------------------------------")

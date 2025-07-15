---
layout: blog-post
title: "Beyond the Black Box: Building a Micro-LLM from Scratch in Python"
author: Freddy Ayala
date: 2025-08-01
read_time: 10 min
image: /assets/images/micro-llm-banner.jpg # Placeholder image
---

In our last article, we demystified how Large Language Models work using interactive diagrams. Today, we’re taking the next logical step: building one ourselves. Forget black boxes and magical APIs—we are going to build a genuine, working, character-level Transformer LLM from the ground up, using only Python and PyTorch.

This isn’t just a "hello world" tutorial. By the end of this post, you will have the complete code for a micro-LLM that can read a text and learn to generate new text in the same style. This is the ultimate "show, don't tell" explanation of how AI really works.

Let's get started.

## The Goal: A Character-Level "Austen-Bot"

Our goal is to build a small language model that can learn the style of Jane Austen. We'll train it on the text of "Pride and Prejudice" and then ask it to generate new text. Since it's a character-level model, it will learn everything from spelling and punctuation to sentence structure and dialogue, one character at a time.

The entire project is contained in a single Python script. You can find the complete, runnable code in our repository here: `[LINK TO micro-llm/train.py ON GITHUB]`

## Step 1: Data Acquisition

First, our model needs something to read. We'll write a simple Python script to download the complete text of "Pride and Prejudice" from Project Gutenberg.

```python
import requests
import os

data_dir = 'micro-llm/data'
file_path = os.path.join(data_dir, 'pride_and_prejudice.txt')
# ... (rest of the download code from train.py) ...
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded {len(text)} characters of text.")
```

## Step 2: Tokenization - The Language of Numbers

As we discussed in our previous post, LLMs don't see words; they see numbers. We need to convert our text into a format the model can understand. We'll create a simple character-level tokenizer.

First, we create our "vocabulary"—the set of all unique characters in the text.

```python
chars = sorted(list(set(text)))
vocab_size = len(chars)
```

Then, we create a mapping to convert each character to an integer and back.

```python
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])
```

With this, we can convert the entire 700,000+ character text into a list of integers.

## Step 3: The Data Pipeline - Preparing Batches

We don't feed the entire book to the model at once. Instead, we train it on small, random chunks of text called "batches." We'll define a `block_size` (the length of a single training chunk, e.g., 8 characters) and a `batch_size` (how many chunks we process at once, e.g., 32).

Our `get_batch` function will grab `batch_size` random chunks from the text and prepare them as input (`x`) and target (`y`) tensors. For each character in the input, the target is the *next* character in the sequence.

```python
import torch

def get_batch(split):
    # ... (code from train.py) ...
    return x, y
```
This is how the model learns: by constantly trying to predict the next character based on the ones it has already seen.

## Step 4: Building the Brain - The Transformer Model

This is the heart of the project. We build our LLM using several `torch.nn.Module` classes. The architecture is a simplified version of what you'd find in models like GPT-4.

1.  **Embedding Layers**: We create tables to look up embeddings for both character tokens and their positions in the sequence.
2.  **`Head`**: A single head of self-attention. It calculates the key, query, and value vectors to determine how much attention each token should pay to others.
3.  **`MultiHeadAttention`**: This combines several attention heads in parallel, allowing the model to focus on different aspects of the relationships between tokens simultaneously.
4.  **`FeedForward`**: A simple neural network that processes the output from the attention heads.
5.  **`Block`**: This assembles the attention and feed-forward components into a standard Transformer block.
6.  **`MicroLLM`**: The final model class. It chains together the embedding tables, multiple Transformer blocks, and a final linear layer to produce the output logits.

Here is a snippet of the final model class:
```python
class MicroLLM(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.position_embedding_table = nn.Embedding(block_size, n_embd)
        self.blocks = nn.Sequential(*[Block(n_embd, n_head=n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size)

    def forward(self, idx, targets=None):
        # ... (forward pass logic from train.py) ...
        return logits, loss

    def generate(self, idx, max_new_tokens):
        # ... (generation logic from train.py) ...
        return idx
```

## Step 5: The Training Loop

With the model and data pipeline ready, the final step is to train it. We create a PyTorch optimizer (we use `AdamW`) and a simple training loop.

In each step, we:
1.  Get a new batch of data.
2.  Calculate the model's loss (how wrong its predictions were).
3.  Use backpropagation to calculate the gradients (`loss.backward()`).
4.  Update the model's weights to improve its predictions (`optimizer.step()`).

```python
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)

for steps in range(10000):
    # ... (training loop from train.py) ...
    if steps % 1000 == 0:
        print(f"Step {steps}, Loss: {loss.item()}")
```

## The Result: A Learning Machine

After just 10,000 training steps (which takes a few minutes on a modern laptop), we can see clear evidence of learning. The loss value, which starts at `~4.5`, drops to `~1.7`.

More excitingly, we can ask the trained model to generate new text. While it's far from perfect, it's clearly learned the structure of English and the style of Jane Austen. It produces words, names, and even dialogue-like structures.

**Generated Text Snippet:**
> “Andnot must forthing
> Mrs. _RiCly
> walking his, or
> wayso her could supprizabeter attence, windo_ how onlucersever, it, of
> give. And tity was such I apposing words. Hust will by sen conty. Elizabeth very herse not joke. I sing to
> must, and of Miss dectnatult.”

## Conclusion: From Black Box to Toolbox

We did it. We built a working language model from scratch. This simple `train.py` script does everything a multi-billion dollar model does, just on a much smaller scale. It reads data, tokenizes it, builds a deep understanding through Transformer blocks, and learns to generate new text.

This exercise proves that LLMs are not magical black boxes. They are complex, yes, but they are also understandable pieces of engineering. By building one ourselves, we transform AI from a mysterious force into a powerful tool in our own toolbox. 
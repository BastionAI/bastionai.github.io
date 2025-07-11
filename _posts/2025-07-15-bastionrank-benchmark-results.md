---
layout: blog-post
title: "The BastionRank Showdown: Crowning the Best On-Device AI Models of 2025"
date: 2025-07-11
author: BastionAI
---

At BastionAI, we're obsessed with pushing the boundaries of what's possible with local, on-device AI. To that end, we created **BastionRank**, a comprehensive benchmark designed to rigorously test language models on the metrics that matter most to users and developers: raw performance and qualitative excellence.

We recently evaluated 10 of the most promising models in our Bastion Chat app. The results were fascinating, revealing a clear hierarchy of performance and some surprising nuances in model behavior.

This report shares our findings, crowning the top performers and offering a guide to which models are best suited for your on-device AI applications.

## Our Humble Benchmark: A Focus on Real-World Applications

Before diving into the results, it's important to state our philosophy. This is a humble benchmark test. We are not trying to determine if a model can achieve PhD-level reasoning. Instead, **we care about real and concrete applications.** Our goal was to simulate the tasks a typical user might perform: summarizing an article, extracting key information from a work document, or understanding nuanced language.

Our testing process involved three pillars of comprehension, using the same text for each model:

1.  **Literary Prose (Herman Melville's *Moby Dick*):** We prompted the models to summarize the opening chapter, focusing on capturing the narrator's deep, melancholic tone and motivations. This tests for emotional and tonal nuance.
2.  **Technical Article (The "Hydra Attention" paper):** We asked for a concise summary of a dense, academic paper. This tests the ability to parse jargon and accurately recall key technical innovations and metrics.
3.  **Business Memo (The "Project Phoenix" pivot):** We provided a corporate memo and asked for a summary that extracted the key decision, the reasoning, and the action items. This tests for understanding of professional communication and structure.

## Why On-Device Testing Matters: A Level Playing Field

A key requirement for any model entering BastionRank is its ability to run efficiently on an actual mobile device. For consistency and to establish a stable performance baseline, the benchmarks in this report were conducted on a Mac.

However, the ultimate goal is real-world mobile performance. Based on our tests with leading models like `Hermes-3-Llama-3.2-3B` on an iPhone 12, developers can expect inference speeds to be approximately **20-25% slower** than the Mac results published here. This is due to the thermal and power constraints of a compact, fanless device—a testament to how impressive even these reduced speeds are.

This methodology creates a level playing field. By forcing models of different architectures and training sets into the exact same conditions, we can compare them in a raw, honest form. This is where the core quality of a model's design truly shows.

## The Reasoning Test: A Reality Check for Function Calling

We also included a reasoning test: we asked models to extract specific information (Ticket ID, Project Name, and VP Name) from the business memo and return it in a structured JSON format.

**Every single model failed.**

Instead of JSON, they returned a natural language response, often including a polite refusal, like this one:
> "I understand you're trying to use a function, but function calling is currently disabled. Let me provide a natural response instead:..."

This was an expected but critical finding. It confirms that out-of-the-box, these models are not fine-tuned for reliable function calling or structured data output. Developers needing this capability must implement specific fine-tuning or advanced prompt engineering.

## The Nuances of Performance: Quantization and "Thinking Models"

Not all models are created equal, even if they have the same parameter count. Two key factors influenced performance in our tests:

*   **Quantization:** You'll notice suffixes like `Q4_K_M` or `Q3_K_XL` in the model IDs. These refer to the quantization level—a process that shrinks the model by reducing the precision of its weights. While this makes the model faster and smaller, aggressive quantization (a lower number) can sometimes degrade the quality of its responses. The excellent performance of models with `Q3` and `Q4` quantization shows a healthy balance of size and intelligence.

*   **"Thinking Models" (Instruction Fine-Tuning):** Two of our top performers were `Qwen3-4B-UD` and `Qwen3-1.7B-UD`. These models were originally developed by the **Qwen team at Alibaba**, and the versions we tested were optimized and republished by **Unsloth**. The "UD" stands for **User-Centric Densification**, a special fine-tuning process designed to make models better at following complex user instructions. This focus on being a "thinking model" that deeply understands user intent likely contributed to their superior performance. A big shoutout to the team at Unsloth for their incredible work in model optimization and for their clear, helpful guides that make on-device AI more accessible to everyone.

## Performance Rankings: The Speed Kings

When it comes to speed, two models stood head and shoulders above the rest.

### Time To First Token (TTFT) - Lower is Better

| Rank | Model Name                | TTFT (ms) |
| :--- | :------------------------ | :-------- |
| 1    | **Qwen3-4B-UD**           | **104.9** |
| 2    | LLaVA-Phi-3-mini          | 106.6     |
| 3    | Phi-4-mini-instruct       | 107.1     |
| 4    | Hermes-3-Llama-3.2-3B     | 107.9     |
| 5    | Llama-3.2-1B-Instruct     | 109.7     |

**`Qwen3-4B-UD`** takes the crown for responsiveness, making it ideal for real-time chat.

### Inference Speed (tokens/sec) - Higher is Better

| Rank | Model Name                | Tokens/sec |
| :--- | :------------------------ | :--------- |
| 1    | **Hermes-3-Llama-3.2-3B** | **197.9**  |
| 2    | **Qwen3-4B-UD**           | **179.4**  |
| 3    | Llama-3.2-1B-Instruct     | 59.2       |
| 4    | LLaVA-Phi-3-mini          | 57.1       |
| 5    | Gemma-3-4B-Instruct       | 56.7       |

**`Hermes-3-Llama-3.2-3B`** is the undisputed champion of throughput, generating text at a blistering pace perfect for longer tasks. `Qwen3-4B-UD` is a very close second.

## Qualitative Analysis: Beyond the Numbers

Speed is nothing without intelligence. Our qualitative tests revealed critical differences in how models "think."

### The Good: Deep Comprehension

In summarizing a complex passage from *Moby Dick*, some models truly shined.
*   **`Gemma-3-4B-Instruct`** demonstrated exceptional nuance, using phrases like "quotidian routine" and "existential despair" that captured the deep, philosophical tone of the original text.
*   **`Qwen3-4B-UD`** also excelled, correctly identifying the narrator's desire to escape "societal pressures."

### The Bad: Critical Factual Errors

The most telling failure came from **`Qwen2.5-0.5B`**. In its summary of *Moby Dick*, it confidently identified the narrator as **"Captain Ahab"** when it is, in fact, Ishmael. This is a major factual error that raises serious concerns about its reliability for any task requiring accuracy. It's a stark reminder that smaller models can sometimes confuse related but distinct concepts.

### The Quirky: Stylistic Hallucinations

When summarizing a technical paper, both **`Llama-3.2-3B-Instruct`** and **`Phi-4-mini-instruct`** included a perfectly formatted but entirely fake citation at the end, like `[Ref 1]`. This shows they are adept at mimicking the *style* of academic writing they were trained on, but it's a "stylistic hallucination" that highlights their pattern-matching nature.

## The Final BastionRank: A Tiered Ranking

After weighing both performance and quality, we've ranked the models into tiers.

### S-Tier: Top Performers
*For users who demand the absolute best.*

1.  🥇 **`Qwen3-4B-UD`**: The best all-around model. It combines the fastest response time with the second-highest speed and top-tier comprehension. It's the champion for interactive chat.
2.  🥈 **`Hermes-3-Llama-3.2-3B`**: The speed king. Its raw generation speed is unmatched, making it the top choice for document generation, summarization, and other long-form tasks.

### A-Tier: The Efficiency Champion
*For developers working in resource-constrained environments.*

3.  🥉 **`Llama-3.2-1B-Instruct`**: The most impressive model relative to its size. Despite being a small 1B model, it punches far above its weight, delivering speeds competitive with much larger models. It's the best choice for balancing performance and efficiency.

### B-Tier: Solid & Balanced
*Reliable models with good, all-around capabilities.*

4.  **`LLaVA-Phi-3-mini`**: A very strong and balanced choice with excellent responsiveness and solid speed.
5.  **`Gemma-3-4B-Instruct`**: A top qualitative performer with competitive speed metrics.

### C-Tier: Capable but Slower
*Functional models for less demanding tasks.*

This tier includes `Qwen2.5-0.5B`, `Llama-3.2-3B-Instruct`, `DeepHermes-3-Llama-3-3B`, and `Qwen3-1.7B-UD`. They perform adequately but are noticeably slower than the top tiers.

---
*Note: `Phi-4-mini-instruct` was left unranked due to an erroneous inference speed measurement, but its excellent TTFT suggests it holds great potential pending further testing.*

## Conclusions: Key Learnings and Next Steps

This first round of BastionRank testing has been incredibly revealing. The results prove that **on-device AI is ready for primetime**, with models like `Qwen3-4B-UD` delivering high-performance, real-time experiences directly on personal devices. We also learned that **efficiency is as important as size**; the `Llama-3.2-1B-Instruct` model's standout performance shows that a well-designed smaller model can easily outperform larger ones.

Qualitative testing proved essential, as the factual errors made by some models show why **nuance matters** for building trust and reliability. Furthermore, the success of specially tuned models highlights that **specialization is a game-changer**. Finally, our tests showed that **function calling is the next great challenge** for on-device AI, and unlocking reliable structured data output is the next major hurdle we are committed to tackling at BastionAI.

Our work with BastionRank is just beginning. We will continuously benchmark new models, investigate performance anomalies, and focus our R&D on solving the on-device function calling problem, which is key to unlocking the next generation of powerful, agentic applications. Stay tuned.

The results of this benchmark will directly inform which models we productionize in Bastion Chat and our other products. We hope these findings are just as valuable to the wider developer community as you build the next generation of private, on-device AI.

## Complete List of Tested Models

For full transparency, here is the complete list of all models included in this BastionRank benchmark.

| Model Name                | Model ID                                                                       |
| :------------------------ | :----------------------------------------------------------------------------- |
| Hermes-3-Llama-3.2-3B     | `NousResearch/Hermes-3-Llama-3.2-3B-GGUF/Hermes-3-Llama-3.2-3B.Q4_K_M.gguf`      |
| Llama-3.2-1B-Instruct     | `bartowski/Llama-3.2-1B-Instruct-GGUF/Llama-3.2-1B-Instruct-Q4_K_M.gguf`          |
| Qwen3-1.7B-UD             | `unsloth/Qwen3-1.7B-GGUF/Qwen3-1.7B-UD-Q6_K_XL.gguf`                             |
| Qwen3-4B-UD               | `unsloth/Qwen3-4B-GGUF/Qwen3-4B-UD-Q3_K_XL.gguf`                                 |
| Qwen2.5-0.5B              | `Qwen/Qwen2.5-0.5B-Instruct-GGUF/qwen2.5-0.5b-instruct-q5_k_m.gguf`            |
| Phi-4-mini-instruct       | `unsloth/Phi-4-mini-instruct-GGUF/Phi-4-mini-instruct-Q3_K_M.gguf`             |
| Llama-3.2-3B-Instruct     | `bartowski/Llama-3.2-3B-Instruct-GGUF/Llama-3.2-3B-Instruct-Q4_K_M.gguf`          |
| DeepHermes-3-Llama-3-3B   | `NousResearch/DeepHermes-3-Llama-3-3B-Preview-GGUF/DeepHermes-3-Llama-3-3B-Preview-q4.gguf` |
| Gemma-3-4B-Instruct       | `lmstudio-community/gemma-3-4b-it-GGUF/gemma-3-4b-it-Q4_K_M.gguf`                |
| LLaVA-Phi-3-mini          | `xtuner/llava-phi-3-mini-gguf/llava-phi-3-mini-int4.gguf`                         | 
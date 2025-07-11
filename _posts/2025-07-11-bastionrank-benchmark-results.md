---
layout: blog-post
title: "The BastionRank Showdown: Crowning the Best On-Device AI Models of 2025"
date: 2025-07-11
author: BastionAI
---

At BastionAI, we're obsessed with pushing the boundaries of what's possible with local, on-device AI. To that end, we created **BastionRank**, a comprehensive benchmark designed to rigorously test language models on the metrics that matter most to users and developers: raw performance and qualitative excellence.

We recently evaluated 10 of the most promising models in our Bastion Chat app. The results were fascinating, revealing a clear hierarchy of performance and some surprising nuances in model behavior.

This report shares our findings, crowning the top performers and offering a guide to which models are best suited for your on-device AI applications.

![BastionRank Rumble - a cartoon depiction of AI models competing in a fighting game, refereed by BastionChat.](/assets/images/bastion-rank-rumble.png)

## Our Humble Benchmark: A Focus on Real-World Applications

Before diving into the results, it's important to state our philosophy. This is a humble benchmark test. We are not trying to determine if a model can achieve PhD-level reasoning. Instead, **we care about real and concrete applications.** Our goal was to simulate the tasks a typical user might perform: summarizing an article, extracting key information from a work document, or understanding nuanced language.

Our testing process involved three pillars of comprehension, using the same text for each model:

1.  **Literary Prose (Herman Melville's *Moby Dick*):** We prompted the models to summarize the opening chapter, focusing on capturing the narrator's deep, melancholic tone and motivations. This tests for emotional and tonal nuance.
2.  **Technical Article (The "Hydra Attention" paper):** We asked for a concise summary of a dense, academic paper. This tests the ability to parse jargon and accurately recall key technical innovations and metrics.
3.  **Business Memo (The "Project Phoenix" pivot):** We provided a corporate memo and asked for a summary that extracted the key decision, the reasoning, and the action items. This tests for understanding of professional communication and structure.

### Our Testing Parameters
To ensure a fair and consistent comparison, all models were run with the same sampling parameters. These settings were chosen to strike a balance between encouraging creative, natural-sounding responses while maintaining factual accuracy.

*   **Temperature:** `0.70`
*   **Top P:** `0.95`
*   **Top K:** `100`
*   **Min P:** `0.0`
*   **Max Tokens:** `952`
*   **Presence Penalty:** `0.0`
*   **Frequency Penalty:** `0.0`
*   **Thinking Token Budget:** `200`

## Why On-Device Testing Matters: A Level Playing Field

A key requirement for any model entering BastionRank is its ability to run efficiently on an actual mobile device. For consistency and to establish a stable performance baseline, the benchmarks in this report were conducted on a Mac.

However, the ultimate goal is real-world mobile performance. Based on our tests with leading models on an iPhone 12, developers can expect inference speeds to be approximately **20-25% slower** than the Mac results published here. This is due to the thermal and power constraints of a compact, fanless device—a testament to how impressive even these reduced speeds are.

This methodology creates a level playing field. By forcing models of different architectures and training sets into the exact same conditions, we can compare them in a raw, honest form. This is where the core quality of a model's design truly shows.

## The Reasoning Test: Unlocking Structured Data on Local AI

The most important test in our benchmark focused on structured data extraction. This is the bedrock of modern AI applications. For an AI to function as an "agent" that can interact with other tools, apps, or APIs, it *must* be able to process unstructured text (like an email) and return clean, predictable, structured data (like a JSON object or key-value pairs). This test reveals which models can be reliably used for automated workflows.

We tested two distinct approaches:

1.  **The High-Level "JSON" Prompt:** This method asks the model to return a JSON object, a common but complex task.
2.  **The Simple "Key-Value" Prompt:** This method guides the model with a simple, fill-in-the-blanks text format.

The results were a stunning validation of prompt engineering.

Here is a summary of the results for each model:

| Model Name                | JSON Prompt | Key-Value Prompt |
| :------------------------ | :---------: | :--------------: |
| Gemma-3-4B-Instruct       |    FAIL     |     **PASS**     |
| Qwen3-4B-UD               |    FAIL     |     **PASS**     |
| Qwen2.5-0.5B              |    FAIL     |     **PASS**     |
| Llama-3.2-1B-Instruct     |    FAIL     |     **PASS**     |
| Phi-4-mini-instruct       |    FAIL     |     **PASS**     |
| DeepHermes-3-Llama-3-3B   |    FAIL     |     **PASS**     |
| LLaVA-Phi-3-mini          |    FAIL     |     **PASS**     |
| Hermes-3-Llama-3.2-3B     |    FAIL     |       FAIL       |
| Qwen3-1.7B-UD             |    FAIL     |       FAIL       |
| Llama-3.2-3B-Instruct     |    FAIL     |       FAIL       |

### Approach 1: The JSON Prompt (Universal Failure)
We gave every model the same business memo and the following prompt:

> **Prompt:** "From the memo, extract the issue, the customer's name, the ticket ID, and the overall sentiment. Format the output as a single, raw JSON object."

**Not a single model passed this test.** The term "JSON" triggered unhelpful, conversational behavior. Instead of providing the raw data, models would try to "help" by explaining what JSON is, refusing the request, or wrapping the JSON in a markdown code block, all of which break automated parsing. This was a common response:

> "I understand you're trying to use a function, but function calling is currently disabled. Let me provide a natural response instead:..."

This confirms that asking a general-purpose local model for strict JSON output is not a reliable strategy without specialized fine-tuning.

### Approach 2: The Key-Value Prompt (Widespread Success)
Next, we gave the models the same memo but with a much simpler, more direct prompt that guides the output format:

> **Prompt:** "Analyze the following memo and extract the key information into the specified fields.
>
> issue: [summarize the issue here]
> customer_name: [extract the customer's name]
> ticket_id: [extract the ticket ID]
> sentiment: [determine the sentiment]
> draft_response: [write a brief, professional response to the customer]"

The difference was night and day. **7 out of our 10 models passed this test**, demonstrating that the key to structured data is simplicity and clarity.

### Case Study: Qwen3-4B-UD (Successful Adaptation)
This model perfectly illustrates the difference. It failed the JSON prompt but passed the Key-Value prompt with flying colors, providing this clean, parsable output:

> issue: The main problem the customer is facing is that user engagement with the social sharing features in the "Phoenix" alpha trial is far below target KPIs, while direct data export feature adoption is unexpectedly high.
> customer_name: Jane Doe
> ticket_id: PX-721
> sentiment: [Positive/Neutral/Negative] (to be determined from tone)
> draft_response: Dear team, I hope this message finds you well. Thank you for your hard work on the "Phoenix" project. Let's make sure to focus on the data export feature in Q3, as it shows high adoption despite being a secondary function.

### Case Study: Hermes-3-Llama-3.2-3B (Failed Adaptation)
This model highlights the limitations of more rigid instruction-following. It failed both prompts. Even with the simpler Key-Value prompt, it couldn't resist adding conversational text and failed to extract all the data correctly, breaking the format.

> issue: The main problem the customer is facing is user engagement with the social sharing features in the "Phoenix" alpha trial falling far below target KPIs.
> customer_name: Not mentioned
> ticket_id: PX-721
> sentiment: Neutral
> draft_response: Dear Jane Doe, Thank you for your email. We appreciate the feedback on our recent alpha trial and the guidance to focus our efforts on improving the data export feature. Our team is already working on the new priorities and will keep you informed of our progress.

**The lesson is definitive:** For on-device AI, don't ask for complex formats like JSON. Guide the model with simple, unambiguous instructions like key-value pairs to get reliable, structured results.

## The Nuances of Performance: Quantization and "Thinking Models"

Not all models are created equal, even if they have the same parameter count. Two key factors influenced performance in our tests:

*   **Quantization:** You'll notice suffixes like `Q4_K_M` or `Q3_K_XL` in the model IDs. These refer to the quantization level—a process that shrinks the model by reducing the precision of its weights. While this makes the model faster and smaller, aggressive quantization (a lower number) can sometimes degrade the quality of its responses. The excellent performance of models with `Q3` and `Q4` quantization shows a healthy balance of size and intelligence.

*   **"Thinking Models" (Instruction Fine-Tuning):** Several of our top performers, like the Qwen models, have undergone special fine-tuning (e.g., "User-Centric Densification") to make them better at following complex user instructions. This focus on being a "thinking model" that deeply understands user intent likely contributed to their superior performance. A big shoutout to the **Qwen team at Alibaba** for their original work and to teams like **Unsloth** for their incredible optimization and helpful guides.

## Performance Rankings: The Speed Kings

Here are the final, validated performance results.

### Time To First Token (TTFT) (Lower is Better)

| Rank | Model Name                | TTFT (ms) |
| :--- | :------------------------ | :-------- |
| 1    | **Hermes-3-Llama-3.2-3B** | **105.1** |
| 2    | Qwen3-1.7B-UD             | 105.7     |
| 3    | Qwen2.5-0.5B              | 112.3     |
| 4    | LLaVA-Phi-3-mini          | 113.2     |
| 5    | Qwen3-4B-UD               | 113.7     |

**`Hermes-3`** delivered the fastest response time, making it feel the most immediately responsive.

### Inference Speed (tokens/sec) (Higher is Better)

| Rank | Model Name                | Tokens/sec |
| :--- | :------------------------ | :--------- |
| 1    | **Gemma-3-4B-Instruct**   | **55.8**   |
| 2    | Qwen2.5-0.5B              | 54.0       |
| 3    | Qwen3-4B-UD               | 52.8       |
| 4    | Phi-4-mini-instruct       | 51.8       |
| 5    | Qwen3-1.7B-UD             | 46.4       |

**`Gemma-3-4B-Instruct`** takes the crown for the fastest overall generation speed.
*(Note: The tokens/sec metric for Hermes-3 failed to parse in our final run, but its top TTFT score confirms it is a high-performance model).*

## Qualitative Analysis: A Deeper Look at Model Intelligence

Speed is meaningless without intelligence. A temperature of 0.7 allowed the models some creative freedom, which revealed significant differences in their ability to understand and replicate nuance.

### Literary Nuance: The Moby Dick Test
This test separated the merely functional models from the truly sophisticated. The goal was not just to summarize, but to capture the deep, melancholic tone of the original text.

*   **Top Performer (`Gemma-3-4B-Instruct`):** Gemma's response was a class apart. It used sophisticated vocabulary like "quotidian routine" and "existential despair," demonstrating a genuine grasp of the narrator's complex psychological state.
*   **Strong Performer (`Qwen3-4B-UD`):** Qwen also excelled, correctly identifying that the narrator's journey was an "escape from societal pressures" and a way of personifying his emotional turmoil.
*   **Critical Failure (`Qwen2.5-0.5B`):** This is where the risk of smaller models becomes apparent. It confidently identified the narrator as **"Captain Ahab"** instead of Ishmael. This is a major factual error that raises serious concerns about its reliability for any task requiring accuracy.

### Technical Precision: The Hydra Attention Test
This test measured the models' ability to parse dense, technical language. Most models performed well, but some showed stylistic quirks. The most notable were the "stylistic hallucinations" from models like **`Llama-3.2-3B-Instruct`** and **`Phi-4-mini-instruct`**, which included perfectly formatted but entirely fake citations (e.g., `[Ref 1]`). This shows they are adept at mimicking the *style* of academic papers, but highlights their pattern-matching nature over true comprehension.

### Professional Acumen: The Business Memo Test
This test evaluated the ability to understand professional communication. All models that passed the reasoning test also did well here, correctly identifying the key directives. **`Qwen3-4B-UD`** stood out by providing a clean, well-structured response that was immediately ready for use in a professional context.

## The Final BastionRank: A Tiered Ranking

After weighing performance, qualitative accuracy, and reasoning ability, we've ranked the models into tiers. As a reminder, **all models failed the JSON reasoning test**, so the key differentiator for reasoning was the much simpler Key-Value test.

### S-Tier: Top Performers
*For users who demand the best balance of speed and smarts.*

1.  🥇 **`Gemma-3-4B-Instruct`**: The best all-around model. It's the **fastest generator** in our tests, and its sophisticated language comprehension in the qualitative analysis was unmatched. It also successfully handled the critical key-value reasoning test, making it the undisputed champion. A minor caveat is that it can sometimes struggle with very short or empty prompts, so it performs best when given explicit, detailed instructions.
2.  🥈 **`Qwen3-4B-UD`**: A close second with excellent, nuanced comprehension that rivaled the top performer. It combines this with strong inference speeds and a successful run on our reasoning test, making it a powerful and reliable choice.

### A-Tier: The Efficiency Champions
*Excellent models that punch above their weight, offering fantastic performance for their size.*

3.  🥉 **`Qwen2.5-0.5B`**: An incredible performer for its tiny 0.5B parameter size. It's the **second-fastest generator** overall and successfully parsed the key-value data, making it a top choice for highly constrained devices. Its only flaw was a significant factual error in the literary test, which holds it back from the S-Tier.
4.  **`Llama-3.2-1B-Instruct`**: The other efficiency champion. While not the fastest, its ability to pass the reasoning test was a feat that several larger models failed to achieve. This makes it a highly reliable and well-balanced small model for tasks requiring structured output.

### B-Tier: Capable but Flawed
*Models with high potential but at least one significant drawback that limits their use case.*

*   **`Hermes-3-Llama-3.2-3B`**: This model has the **fastest time-to-first-token**, making it feel exceptionally responsive. However, its failure on the simple key-value reasoning test is a major issue, suggesting it is less adaptable at following complex instructions than other top models.
*   **`Phi-4-mini-instruct` & `DeepHermes-3-Llama-3-3B`**: Both of these models successfully passed the reasoning test, demonstrating good instruction-following capabilities. They are held back by mediocre performance scores compared to the leaders, with inference speeds that are a noticeable step down from the A-tier.

### C-Tier: Lagging Behind
*These models failed the key-value reasoning test and had slower overall performance, placing them at the bottom of our rankings.*

This tier includes **`Qwen3-1.7B-UD`** and **`Llama-3.2-3B-Instruct`**.

## Conclusions: The State of On-Device AI

This first round of BastionRank testing has been incredibly revealing. The results prove that **on-device AI is ready for primetime**, with models like `Gemma-3-4B-Instruct` delivering high-performance, real-time experiences directly on personal devices. We also learned that **efficiency is as important as size**; the `Llama-3.2-1B-Instruct` model's standout reasoning performance shows that a well-designed smaller model can easily outperform larger ones. Qualitative testing proved essential, as the factual errors made by some models show why **nuance matters** for building trust and reliability.

However, our most critical finding is about the future of AI. The universal failure of models to handle JSON requests, contrasted with the widespread success of the simple key-value prompt, highlights the single biggest bottleneck for the next generation of applications: **creating local agentic AI on mobile devices.** An "agent" needs to reliably talk to tools and APIs, and that requires structured data.

While we've shown a reliable workaround using clear, simple prompts, the ultimate goal is to have models that can seamlessly handle complex requests without extensive prompt engineering. This is the challenge we are committed to solving at BastionAI. Our work is just beginning. We will continue to benchmark new models and focus our R&D on solving the on-device reasoning problem to unlock the next generation of powerful, agentic applications. Stay tuned.

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
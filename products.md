---
layout: default
title: "Products"
description: "Discover BastionAI's privacy-first AI solutions designed for security and innovation."
permalink: /products/
bastion_chat_features:
  - "100% Local Processing"
  - "Advanced AI Models"
  - "Voice Interaction"
  - "Document RAG Support"
bastion_chat_button:
  url: "/products/bastion-chat/"
  text: "Learn More"
  primary: true
key_features:
  - title: "100% Local Processing"
    icon: "🏠"
    description: "All AI computations happen on your device"
  - title: "Advanced Reasoning"
    icon: "🧠"
    description: "Powered by state-of-the-art language models"
  - title: "Voice Mode"
    icon: "🎤"
    description: "Natural speech interaction capabilities"
  - title: "High Performance"
    icon: "⚡"
    description: "Optimized for speed and efficiency"
---

{% include components/header.html 
   type="hero"
   title="Our Products"
   description="Privacy-first AI solutions that put you in control"
%}

<section class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">BastionChat</h2>
      <p class="section-subtitle">The ultimate privacy-focused AI chat experience</p>
    </div>
    
    <div class="products-grid">
      {% include components/product-card.html 
         logo="/assets/images/logos/bastion-chat-logo.png"
         title="BastionChat"
         description="A powerful local AI chat application that leverages advanced language models directly on your device. Experience the full potential of AI conversation without compromising your privacy or security."
         features=page.bastion_chat_features
         button=page.bastion_chat_button
      %}
    </div>
    
    {% include components/features-grid.html features=page.key_features %}
    
    <div class="chat-mockup">
      <div class="chat-header">
        <img src="/assets/images/logos/bastion-chat-logo.png" alt="BastionChat" class="chat-logo">
        <span>BastionChat</span>
        <span class="badge" style="margin-left: auto;">🟢 Local Model Active</span>
      </div>
      <div class="chat-message user">
        <div class="chat-message-content">How does local AI processing ensure my privacy?</div>
      </div>
      <div class="chat-message assistant">
        <div class="chat-message-content">Local AI processing means all computation happens directly on your device. Your conversations never leave your computer, ensuring complete privacy and eliminating data collection concerns.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">Technical Specifications</h2>
    </div>
    
    <div class="specs-grid">
      <div class="spec-item">
        <div class="spec-label">Model Support</div>
        <div class="spec-value">GGUF format, multiple quantization levels, dynamic loading</div>
      </div>
      <div class="spec-item">
        <div class="spec-label">Performance</div>
        <div class="spec-value">Optimized inference, memory-efficient, multi-threading</div>
      </div>
      <div class="spec-item">
        <div class="spec-label">Features</div>
        <div class="spec-value">Voice mode, Document RAG, latest models (Gemma 3, Qwen 3)</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">What's Next?</h2>
      <p class="section-subtitle">We're continuously working on expanding our product lineup with more privacy-first AI solutions. Stay tuned for updates!</p>
    </div>
  </div>
</section>

 
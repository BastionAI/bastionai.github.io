---
layout: default
title: "Home"
description: "BastionAI democratizes AI through local models - Your AI, Your Data, Your Control. Complete privacy with advanced capabilities."
hero_buttons:
  - url: "/products/"
    text: "Explore Products"
    primary: true
    large: true
  - url: "/products/bastion-chat/"
    text: "Try BastionChat"
    primary: true
    large: true
democratization_features:
  - title: "AI Democratization"
    icon: "🌍"
    description: "Breaking down barriers - advanced AI shouldn't be exclusive to tech giants"
  - title: "Complete Privacy"
    icon: "🏠"
    description: "Your conversations, your documents, your data - everything stays on your device"
  - title: "Local Processing"
    icon: "🔓"
    description: "All AI computations happen on your device - no cloud dependencies"
  - title: "Open Source Based"
    icon: "⚙️"
    description: "Built on open-source foundations, giving you freedom and transparency"
technical_features:
  - title: "Local Vector Database"
    icon: "🗄️"
    description: "Advanced RAG capabilities with local indexing of PDFs, web pages, and documents"
  - title: "Latest Model Support"
    icon: "🧠"
    description: "Run cutting-edge models like Gemma 3 and Qwen 3 directly on your device"
  - title: "Voice & Conversation Mode"
    icon: "🎤"
    description: "Natural speech interaction with context-aware dialogue capabilities"
  - title: "Custom AI Engine"
    icon: "⚡"
    description: "Tailor-made engine optimized for performance and efficiency on local hardware"
bastion_chat_highlights:
  - "Local model execution"
  - "Customizable parameters & prompts"
  - "Voice mode & conversation capabilities"
  - "Document RAG (PDF, web, text)"
  - "Latest models (Gemma 3, Qwen 3)"
bastion_chat_cta:
  url: "/products/bastion-chat/"
  text: "Explore BastionChat"
  primary: true
---

{% include components/header.html 
   type="hero"
   title="Your AI, Your Data, Your Control"
   description="BastionAI empowers users with advanced AI capabilities that run entirely on your device. Experience the full potential of AI conversation, document processing, and voice interaction without compromising your privacy or security."
   buttons=page.hero_buttons
%}

<section class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">Democratizing AI Technology</h2>
      <p class="section-subtitle">Making advanced AI accessible to everyone, not just tech giants</p>
    </div>
    
    {% include components/features-grid.html features=page.democratization_features %}
  </div>
</section>

<section class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">Advanced Local AI Engine</h2>
      <p class="section-subtitle">Custom-built engine based on open-source software with cutting-edge capabilities</p>
    </div>
    
    {% include components/features-grid.html features=page.technical_features %}
  </div>
</section>

<section class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">Experience BastionChat</h2>
      <p class="section-subtitle">The flagship product bringing AI democratization to life</p>
    </div>
    
    <div class="products-grid">
      {% include components/product-card.html 
         logo="/assets/images/logos/bastion-chat-logo.png"
         title="BastionChat"
         description="A revolutionary local AI chat application featuring advanced capabilities with complete privacy. Download models, customize parameters, and experience AI on your terms."
         features=page.bastion_chat_highlights
         button=page.bastion_chat_cta
      %}
    </div>
    
    <div class="chat-mockup">
      <div class="chat-header">
        <img src="/assets/images/logos/bastion-chat-logo.png" alt="BastionChat" class="chat-logo">
        <span>BastionChat</span>
        <span class="badge" style="margin-left: auto;">🟢 Local Model Active</span>
      </div>
      <div class="chat-message user">
        <div class="chat-message-content">Can you analyze this PDF document for me?</div>
      </div>
      <div class="chat-message assistant">
        <div class="chat-message-content">Absolutely! I can index and analyze PDF documents locally using RAG capabilities. Your document data never leaves your device. Just upload the PDF and I'll help you extract insights, summarize content, or answer questions about it.</div>
      </div>
      <div class="chat-message user">
        <div class="chat-message-content">That's amazing! How do I customize the AI parameters?</div>
      </div>
      <div class="chat-message assistant">
        <div class="chat-message-content">You have full control! Adjust temperature for creativity, modify prompts for specific use cases, and select from various downloadable models. The interface gives you granular control over every aspect of the AI experience.</div>
      </div>
    </div>
  </div>
</section>

 
---
layout: default
title: "Home"
description: "BastionAI democratizes AI through local models - Your AI, Your Data, Your Control. Complete privacy with advanced capabilities."
hero_buttons:
  - url: "/about/"
    text: "Learn More"
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
company_mission:
  - title: "Privacy-First Solutions"
    icon: "🛡️"
    description: "We build AI applications that prioritize user privacy and data sovereignty"
  - title: "Local AI Innovation"
    icon: "💡"
    description: "Developing cutting-edge local AI technologies and frameworks"
  - title: "User Empowerment"
    icon: "🚀"
    description: "Giving users complete control over their AI experience and data"
  - title: "Open Source Foundation"
    icon: "🔧"
    description: "Building on open-source principles for transparency and community collaboration"
bastion_chat_highlights:
  - "Available for iPhone, iPad, and Mac"
  - "Complete privacy with local processing"
  - "Advanced AI capabilities"
  - "Coming soon - Early access available"
bastion_chat_cta:
  url: "/products/bastion-chat/"
  text: "Learn About BastionChat"
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
      <h2 class="section-title">What We Do</h2>
      <p class="section-subtitle">Building the future of privacy-first AI applications and technologies</p>
    </div>
    
    {% include components/features-grid.html features=page.company_mission %}
  </div>
</section>

<section class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">Our First Product: BastionChat</h2>
      <p class="section-subtitle">The flagship application demonstrating AI democratization in action</p>
    </div>
    
    <div class="products-grid">
      {% include components/product-card.html 
         logo="/assets/images/logos/bastion-chat-logo.png"
         title="BastionChat"
         description="Our first step toward AI democratization - a privacy-first AI assistant that runs entirely on your device. Experience powerful AI conversations without compromising your privacy."
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

 
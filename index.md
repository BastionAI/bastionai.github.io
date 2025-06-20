---
layout: default
title: "BastionAI - Your AI, Your Data, Your Control"
description: "BastionAI empowers users with advanced AI capabilities that run entirely on your device. Experience the full potential of AI conversation, document processing, and voice interaction without compromising your privacy or security."

# Hero Section
hero_buttons:
  - url: "/products/"
    text: "Explore Products"
    primary: true
  - url: "/contact/"
    text: "Get Started"
    primary: false

# Timeline Data
timeline_phases:
  - id: "pre-cloud-ai"
    year: "1950s-2000s"
    title: "Pre-Cloud AI Era"
    subtitle: "Limited Local Systems"
    description: "Early AI systems operated on individual machines with constrained computational resources. Access was limited to institutions with significant infrastructure investments."
    color: "#9ca3af"
    icon: "🖥️"
    limitations:
      - "Limited computational power"
      - "High infrastructure costs"
      - "Restricted to large institutions"
      - "Isolated systems"
    
  - id: "cloud-ai"
    year: "2000s-2020s"
    title: "The Cloud AI Era"
    subtitle: "Centralized Power, Surrendered Control"
    description: "AI capabilities became concentrated in massive cloud data centers. Users gained access to powerful AI but at the cost of data sovereignty and privacy."
    color: "#3b82f6"
    icon: "☁️"
    limitations:
      - "Data privacy concerns"
      - "Internet dependency"
      - "Limited customization"
      - "Vendor lock-in"
    advantages:
      - "Massive computational power"
      - "Regular updates"
      - "Easy access"
      - "No local hardware requirements"
    
  - id: "edge-ai"
    year: "2020s"
    title: "Edge AI Evolution"
    subtitle: "Bridging Cloud and Local"
    description: "AI processing moved closer to users through edge computing, reducing latency and improving privacy while maintaining some cloud connectivity."
    color: "#f59e0b"
    icon: "📡"
    advantages:
      - "Reduced latency"
      - "Improved privacy"
      - "Hybrid capabilities"
      - "Better performance"
    limitations:
      - "Technical complexity"
      - "Limited model selection"
      - "Still requires infrastructure"
    
  - id: "bastion-ai"
    year: "2024+"
    title: "BastionAI Revolution"
    subtitle: "True AI Democratization"
    description: "Complete local AI processing with enterprise-grade capabilities. Users maintain full control over their data while accessing the latest AI innovations."
    color: "#059669"
    icon: "🛡️"
    highlight: true
    advantages:
      - "Complete data sovereignty"
      - "No internet dependency"
      - "Full customization control"
      - "Enterprise-grade security"
      - "Open source foundation"
      - "Multi-platform support"

# Use Cases Data
use_cases:
  - title: "Ocean Expeditions"
    description: "Navigate remote waters with AI-powered guidance when satellite internet is slow, expensive, or unavailable. Access navigation, weather analysis, and emergency protocols offline."
    image: "/assets/images/use-cases/ocean-expedition.jpg"
    alt: "Ocean expedition team on boat"
    badge: "Remote Operations"
    
  - title: "Emergency Response"
    description: "Life-saving medical guidance, first aid protocols, and survival information instantly available when networks are down. Critical decisions can't wait for connectivity."
    image: "/assets/images/use-cases/emergency-response.jpg"
    alt: "Emergency responder with medical equipment"
    badge: "Life Critical"
    
  - title: "Rural Healthcare"
    description: "Provide diagnostic assistance and medical knowledge to healthcare workers in remote clinics where reliable internet is a luxury, not a given."
    image: "/assets/images/use-cases/rural-healthcare.jpg"
    alt: "Doctor in rural clinic"
    badge: "Healthcare"
    
  - title: "Industrial Operations"
    description: "Support offshore oil rigs, mining operations, and remote manufacturing with AI-powered safety protocols and equipment diagnostics - no expensive satellite required."
    image: "/assets/images/use-cases/industrial-operations.jpg"
    alt: "Oil rig workers on offshore platform"
    badge: "Industrial Safety"
    
  - title: "Privacy-Critical Work"
    description: "Legal firms, financial services, and government agencies can leverage AI for document analysis and decision support without compromising sensitive data."
    image: "/assets/images/use-cases/privacy-critical.jpg"
    alt: "Lawyer working with confidential documents"
    badge: "Confidential"
    
  - title: "Adventure & Exploration"
    description: "Mountain climbers, researchers, and adventurers get AI assistance for route planning, weather analysis, and survival guidance in the world's most remote locations."
    image: "/assets/images/use-cases/mountain-climbing.jpg"
    alt: "Mountain climber in remote terrain"
    badge: "Extreme Conditions"

# Features Data
democratization_features:
  - title: "Privacy by Design"
    icon: "🔒"
    description: "Your data never leaves your device. Complete control over your information and AI interactions."
  - title: "Open Source Foundation"
    icon: "🔧"
    description: "Built on transparent, community-driven technologies that you can trust and verify."
  - title: "Cross-Platform Support"
    icon: "📱"
    description: "Seamless experience across iPhone, iPad, Mac, and other platforms."
  - title: "User Empowerment"
    icon: "🚀"
    description: "Giving users complete control over their AI experience and data"

company_mission:
  - title: "AI Democratization"
    icon: "🌟"
    description: "Making advanced AI accessible to everyone, not just tech giants"
  - title: "Privacy Protection"
    icon: "🛡️"
    description: "Ensuring user data remains private and secure through local processing"
  - title: "Open Innovation"
    icon: "🔧"
    description: "Building on open-source principles for transparency and community collaboration"

# BastionChat Product Data
bastion_chat_highlights:
  - "Chat with PDFs, documents, and web pages"
  - "Local document indexing and search"
  - "Instant summaries and insights extraction"
  - "Voice-to-text note processing"
  - "Multi-document analysis and comparison"
  - "Research assistant with citation tracking"
  - "Available for iPhone, iPad, and Mac"
  - "Everything stays on your device - guaranteed"

bastion_chat_cta:
  url: "/products/bastion-chat/"
  text: "Learn About BastionChat"
  primary: true
---

{% include components/header.html 
   type="hero"
   title=page.title
   description=page.description
   buttons=page.hero_buttons
%}

{% include components/timeline-section.html timeline_phases=page.timeline_phases %}

{% include components/use-cases-section.html use_cases=page.use_cases %}

<section class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">Democratizing AI for Everyone</h2>
      <p class="section-subtitle">Breaking down barriers to make advanced AI accessible, private, and user-controlled</p>
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
         description="Transform your documents, PDFs, and web content into an intelligent knowledge base - all processed locally on your iPhone, iPad, or Mac. Chat with your data, get instant insights, and never worry about your information leaving your device."
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
 
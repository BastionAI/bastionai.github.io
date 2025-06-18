---
layout: default
title: "Home"
description: "BastionAI democratizes AI through local models - Your AI, Your Data, Your Control. Complete privacy with advanced capabilities."
hero_buttons:
  - url: "/about/"
    text: "Learn More"
    primary: true
    large: true
timeline_phases:
  - id: "cloud-ai"
    year: "2010-2020"
    title: "Cloud AI Era"
    subtitle: "Centralized Power"
    icon: "☁️"
    description: "AI capabilities concentrated in massive data centers. Users surrender data and control to tech giants for AI services."
    limitations:
      - "Data privacy concerns"
      - "Vendor lock-in"
      - "Internet dependency"
      - "Limited customization"
    color: "#64748b"
  - id: "edge-ai"
    year: "2020-2024"
    title: "Edge AI Emergence"
    subtitle: "Distributed Computing"
    icon: "⚡"
    description: "AI processing moves closer to users. Some capabilities run locally, but still limited by device constraints and model access."
    limitations:
      - "Limited model selection"
      - "Complex setup required"
      - "Partial local processing"
      - "Technical expertise needed"
    color: "#3b82f6"
  - id: "bastion-ai"
    year: "2024+"
    title: "BastionAI Future"
    subtitle: "True AI Democratization"
    icon: "🚀"
    description: "Complete local AI with full user control. Advanced capabilities without compromising privacy or requiring technical expertise."
    advantages:
      - "Complete data sovereignty"
      - "Full model customization"
      - "No internet dependency"
      - "User-friendly interface"
    color: "#10b981"
    highlight: true
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

<section class="timeline-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">The Evolution of AI: From Cloud to Local</h2>
      <p class="section-subtitle">Witness the journey toward true AI democratization</p>
    </div>
    
    <div class="timeline-container">
      <div class="timeline-line"></div>
      
      {% for phase in page.timeline_phases %}
      <div class="timeline-item {% if phase.highlight %}timeline-highlight{% endif %}" data-phase="{{ phase.id }}">
        <div class="timeline-marker" style="background-color: {{ phase.color }}">
          <span class="timeline-icon">{{ phase.icon }}</span>
        </div>
        
        <div class="timeline-content">
          <div class="timeline-year">{{ phase.year }}</div>
          <h3 class="timeline-title">{{ phase.title }}</h3>
          <p class="timeline-subtitle">{{ phase.subtitle }}</p>
          <p class="timeline-description">{{ phase.description }}</p>
          
          {% if phase.limitations %}
          <div class="timeline-features limitations">
            <h4>Limitations:</h4>
            <ul>
              {% for limitation in phase.limitations %}
              <li>{{ limitation }}</li>
              {% endfor %}
            </ul>
          </div>
          {% endif %}
          
          {% if phase.advantages %}
          <div class="timeline-features advantages">
            <h4>Advantages:</h4>
            <ul>
              {% for advantage in phase.advantages %}
              <li>{{ advantage }}</li>
              {% endfor %}
            </ul>
          </div>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
    
    <div class="timeline-future">
      <h3>The Future is Local</h3>
      <p>BastionAI represents the next evolution in AI technology - where users have complete control over their AI experience without sacrificing advanced capabilities. Join us in democratizing AI for everyone.</p>
    </div>
  </div>
</section>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Intersection Observer for timeline animations
  const timelineItems = document.querySelectorAll('.timeline-item');
  const timelineLine = document.querySelector('.timeline-line');
  
  const observerOptions = {
    threshold: 0.3,
    rootMargin: '0px 0px -100px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
        
        // Add special effects for BastionAI phase
        if (entry.target.dataset.phase === 'bastion-ai') {
          setTimeout(() => {
            entry.target.classList.add('future-glow');
          }, 600);
        }
      }
    });
  }, observerOptions);
  
  timelineItems.forEach(item => {
    item.style.animationPlayState = 'paused';
    observer.observe(item);
  });
  
  // Click interactions for timeline items
  timelineItems.forEach(item => {
    const content = item.querySelector('.timeline-content');
    const marker = item.querySelector('.timeline-marker');
    
    content.addEventListener('click', () => {
      // Remove active class from all items
      timelineItems.forEach(otherItem => {
        otherItem.classList.remove('timeline-active');
      });
      
      // Add active class to clicked item
      item.classList.add('timeline-active');
      
      // Animate marker
      marker.style.transform = 'translate(-50%, -50%) scale(1.2)';
      setTimeout(() => {
        marker.style.transform = 'translate(-50%, -50%) scale(1)';
      }, 200);
      
      // Show phase details with animation
      const phaseId = item.dataset.phase;
      showPhaseDetails(phaseId);
    });
  });
  
  // Progressive line drawing animation
  let lineHeight = 0;
  const maxHeight = timelineLine.scrollHeight;
  
  const drawLine = () => {
    const scrollProgress = window.pageYOffset / (document.documentElement.scrollHeight - window.innerHeight);
    const timelineSection = document.querySelector('.timeline-section');
    const sectionTop = timelineSection.offsetTop;
    const sectionHeight = timelineSection.offsetHeight;
    const windowHeight = window.innerHeight;
    
    if (window.pageYOffset + windowHeight > sectionTop) {
      const progress = Math.min(1, (window.pageYOffset + windowHeight - sectionTop) / sectionHeight);
      timelineLine.style.height = `${progress * 100}%`;
    }
  };
  
  window.addEventListener('scroll', drawLine);
  drawLine(); // Initial call
  
  function showPhaseDetails(phaseId) {
    const details = {
      'cloud-ai': {
        title: 'The Cloud AI Era: Centralized Control',
        content: 'During this period, AI capabilities were concentrated in massive data centers owned by tech giants. Users had to surrender their data and accept limited customization for AI services.'
      },
      'edge-ai': {
        title: 'Edge AI: Moving Closer to Users',
        content: 'Edge AI emerged as a solution to latency and privacy concerns, bringing some processing closer to users. However, it still required technical expertise and offered limited model selection.'
      },
      'bastion-ai': {
        title: 'BastionAI: True AI Democratization',
        content: 'BastionAI represents the culmination of AI evolution - complete local processing with full user control, advanced capabilities, and privacy protection without requiring technical expertise.'
      }
    };
    
    // Create or update detail modal/tooltip
    let detailElement = document.querySelector('.timeline-detail');
    if (!detailElement) {
      detailElement = document.createElement('div');
      detailElement.className = 'timeline-detail';
      document.body.appendChild(detailElement);
    }
    
    const detail = details[phaseId];
    detailElement.innerHTML = `
      <div class="timeline-detail-content">
        <h4>${detail.title}</h4>
        <p>${detail.content}</p>
        <button class="timeline-detail-close">✕</button>
      </div>
    `;
    
    detailElement.style.display = 'block';
    setTimeout(() => detailElement.classList.add('show'), 10);
    
    // Close functionality
    const closeBtn = detailElement.querySelector('.timeline-detail-close');
    closeBtn.addEventListener('click', () => {
      detailElement.classList.remove('show');
      setTimeout(() => detailElement.style.display = 'none', 300);
    });
  }
});
</script>

<style>
.timeline-active .timeline-content {
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
  border-left: 4px solid #10b981;
}

.future-glow {
  animation: futureGlow 3s ease-in-out infinite;
}

@keyframes futureGlow {
  0%, 100% { filter: drop-shadow(0 0 5px rgba(16, 185, 129, 0.3)); }
  50% { filter: drop-shadow(0 0 20px rgba(16, 185, 129, 0.6)); }
}

.timeline-detail {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: none;
  z-index: 1000;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.timeline-detail.show {
  opacity: 1;
}

.timeline-detail-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 2rem;
  border-radius: 16px;
  max-width: 600px;
  width: 90%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.timeline-detail-content h4 {
  color: #1e293b;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.timeline-detail-content p {
  color: #475569;
  line-height: 1.6;
  margin-bottom: 0;
}

.timeline-detail-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #64748b;
  transition: color 0.2s ease;
}

.timeline-detail-close:hover {
  color: #1e293b;
}

.timeline-line {
  height: 0;
  transition: height 0.5s ease-out;
}
</style>

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

 
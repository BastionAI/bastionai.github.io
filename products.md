---
layout: page
title: "Products"
description: "Discover BastionAI's privacy-first AI solutions designed for security and innovation."
permalink: /products/
---

<div class="products-hero">
  <div class="container">
    <h1>Our Products</h1>
    <p class="lead">Privacy-first AI solutions that put you in control</p>
  </div>
</div>

<section class="products-section">
  <div class="container">
    
    <!-- BastionChat - Featured Product -->
    <div class="product-featured">
      <div class="product-content">
        <div class="product-info">
          <h2>BastionChat</h2>
          <p class="product-tagline">The ultimate privacy-focused AI chat experience</p>
          <p class="product-description">
            BastionChat is a powerful local AI chat application that leverages advanced language models 
            directly on your device. Experience the full potential of AI conversation without compromising 
            your privacy or security.
          </p>
          
          <div class="feature-highlights">
            <h3>Key Features</h3>
            <div class="features-grid">
              <div class="feature-item">
                <span class="feature-icon">🏠</span>
                <div>
                  <strong>100% Local Processing</strong>
                  <p>All AI computations happen on your device</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-icon">🧠</span>
                <div>
                  <strong>Advanced Reasoning</strong>
                  <p>Powered by state-of-the-art language models</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-icon">🎤</span>
                <div>
                  <strong>Voice Mode</strong>
                  <p>Natural speech interaction capabilities</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-icon">⚡</span>
                <div>
                  <strong>High Performance</strong>
                  <p>Optimized for speed and efficiency</p>
                </div>
              </div>
            </div>
          </div>
          
          <div class="product-actions">
            <a href="/products/bastion-chat" class="btn btn-primary btn-large">Learn More</a>
            <a href="#download" class="btn btn-secondary btn-large">Download</a>
          </div>
        </div>
        
        <div class="product-visual">
          <div class="chat-mockup">
            <div class="chat-header">
              <div class="chat-title">BastionChat</div>
              <div class="status-indicator">🟢 Local Model Active</div>
            </div>
            <div class="chat-messages">
              <div class="message user">
                <div class="message-content">How does local AI processing ensure my privacy?</div>
              </div>
              <div class="message assistant">
                <div class="message-content">Local AI processing means all computation happens directly on your device. Your conversations never leave your computer, ensuring complete privacy and eliminating data collection concerns.</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Technical Specifications -->
    <div class="tech-specs">
      <h3>Technical Capabilities</h3>
      <div class="specs-grid">
        <div class="spec-card">
          <h4>Model Support</h4>
          <ul>
            <li>GGUF model format</li>
            <li>Multiple quantization levels</li>
            <li>Dynamic model loading</li>
            <li>Model catalog integration</li>
          </ul>
        </div>
        <div class="spec-card">
          <h4>Performance</h4>
          <ul>
            <li>Optimized inference engine</li>
            <li>Memory-efficient processing</li>
            <li>Multi-threading support</li>
            <li>Hardware acceleration</li>
          </ul>
        </div>
        <div class="spec-card">
          <h4>Features</h4>
          <ul>
            <li>Voice interaction mode</li>
            <li>Document RAG (PDF, web, text)</li>
            <li>Conversation management</li>
            <li>Latest model support (Gemma 3, Qwen 3)</li>
          </ul>
        </div>
      </div>
    </div>
    
    <!-- Coming Soon -->
    <div class="coming-soon">
      <h3>What's Next?</h3>
      <p>We're continuously working on expanding our product lineup with more privacy-first AI solutions. Stay tuned for updates!</p>
    </div>
    
  </div>
</section>

<style>
.products-hero {
  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
  color: white;
  padding: 3rem 0;
  text-align: center;
}

.products-hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.lead {
  font-size: 1.25rem;
  opacity: 0.9;
}

.products-section {
  padding: 4rem 0;
}

.product-featured {
  margin-bottom: 4rem;
  background: #fff;
  border-radius: 1rem;
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
  overflow: hidden;
}

.product-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  padding: 3rem;
}

.product-tagline {
  font-size: 1.25rem;
  color: #6366f1;
  margin-bottom: 1rem;
  font-weight: 600;
}

.product-description {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 2rem;
  color: #6b7280;
}

.feature-highlights h3 {
  margin-bottom: 1.5rem;
  color: #374151;
}

.features-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.feature-icon {
  font-size: 1.5rem;
  margin-top: 0.25rem;
}

.feature-item strong {
  display: block;
  margin-bottom: 0.25rem;
  color: #374151;
}

.feature-item p {
  font-size: 0.9rem;
  color: #6b7280;
  margin: 0;
}

.product-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-large {
  padding: 1rem 2rem;
  font-size: 1.1rem;
}

.product-visual {
  display: flex;
  align-items: center;
  justify-content: center;
}

.chat-mockup {
  background: #f9fafb;
  border-radius: 1rem;
  border: 2px solid #e5e7eb;
  width: 100%;
  max-width: 400px;
}

.chat-header {
  background: #4f46e5;
  color: white;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 1rem 1rem 0 0;
}

.chat-title {
  font-weight: 600;
}

.status-indicator {
  font-size: 0.8rem;
  opacity: 0.9;
}

.chat-messages {
  padding: 1.5rem;
}

.message {
  margin-bottom: 1rem;
}

.message.user .message-content {
  background: #6366f1;
  color: white;
  margin-left: 2rem;
}

.message.assistant .message-content {
  background: #e5e7eb;
  color: #374151;
  margin-right: 2rem;
}

.message-content {
  padding: 0.75rem 1rem;
  border-radius: 1rem;
  font-size: 0.9rem;
  line-height: 1.4;
}

.tech-specs, .coming-soon {
  margin-top: 4rem;
  padding-top: 3rem;
  border-top: 2px solid #e5e7eb;
}

.tech-specs h3, .coming-soon h3 {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2rem;
  color: #374151;
}

.specs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.spec-card {
  background: #f9fafb;
  padding: 2rem;
  border-radius: 1rem;
  border: 1px solid #e5e7eb;
}

.spec-card h4 {
  margin-bottom: 1rem;
  color: #4f46e5;
}

.spec-card ul {
  list-style: none;
  padding: 0;
}

.spec-card li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #e5e7eb;
}

.spec-card li:last-child {
  border-bottom: none;
}

.coming-soon {
  text-align: center;
  background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
  padding: 3rem;
  border-radius: 1rem;
}

@media (max-width: 768px) {
  .product-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .product-actions {
    justify-content: center;
  }
  
  .specs-grid {
    grid-template-columns: 1fr;
  }
}
</style> 
---
layout: home
title: "Privacy-First AI Solutions"
description: "BastionAI creates products oriented to leverage the power of local models focusing on privacy, security, and innovation."
---

<div class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">Privacy-First AI Solutions</h1>
    <p class="hero-subtitle">
      BastionAI creates products oriented to leverage the power of local models 
      focusing on privacy, security, and innovation.
    </p>
    <div class="hero-buttons">
      <a href="/products" class="btn btn-primary">Explore Products</a>
      <a href="/products/bastion-chat" class="btn btn-secondary">Try BastionChat</a>
    </div>
  </div>
</div>

<section class="features-section">
  <div class="container">
    <h2>Why Choose BastionAI?</h2>
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <h3>Privacy First</h3>
        <p>Your data stays on your device. No cloud dependencies, no data collection.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🛡️</div>
        <h3>Security Focused</h3>
        <p>Built with security at the core, ensuring your AI interactions remain confidential.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🚀</div>
        <h3>Innovation Driven</h3>
        <p>Cutting-edge local AI models that deliver powerful capabilities without compromise.</p>
      </div>
    </div>
  </div>
</section>

<section class="products-preview">
  <div class="container">
    <h2>Our Products</h2>
    <div class="product-showcase">
      <div class="product-card featured">
        <h3>BastionChat</h3>
        <p>A powerful local AI chat application featuring advanced capabilities with complete privacy.</p>
        <ul class="feature-list">
          <li>Local model execution</li>
          <li>Advanced reasoning capabilities</li>
          <li>Multi-modal support</li>
          <li>Privacy-focused design</li>
        </ul>
        <a href="/products/bastion-chat" class="btn btn-primary">Learn More</a>
      </div>
    </div>
  </div>
</section>

<style>
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 4rem 0;
  text-align: center;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 0.75rem 2rem;
  border-radius: 0.5rem;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  display: inline-block;
}

.btn-primary {
  background-color: #fff;
  color: #667eea;
}

.btn-primary:hover {
  background-color: #f8f9ff;
  transform: translateY(-2px);
}

.btn-secondary {
  background-color: transparent;
  color: white;
  border: 2px solid white;
}

.btn-secondary:hover {
  background-color: white;
  color: #667eea;
}

.features-section, .products-preview {
  padding: 4rem 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.feature-card {
  text-align: center;
  padding: 2rem;
  border-radius: 1rem;
  background: #f8f9fa;
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.product-showcase {
  margin-top: 3rem;
  display: flex;
  justify-content: center;
}

.product-card {
  background: white;
  border-radius: 1rem;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  max-width: 500px;
  text-align: center;
}

.feature-list {
  text-align: left;
  margin: 1.5rem 0;
}

.feature-list li {
  margin-bottom: 0.5rem;
}

h2 {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2.5rem;
  color: #333;
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }
  
  .hero-buttons {
    flex-direction: column;
    align-items: center;
  }
  
  .btn {
    width: 200px;
  }
}
</style> 
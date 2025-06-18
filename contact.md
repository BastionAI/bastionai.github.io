---
layout: default
title: "Contact"
description: "Get in touch with the BastionAI team. We'd love to hear from you."
permalink: /contact/
---

{% include components/header.html 
   type="hero"
   title="Contact"
   description="We'd love to hear from you. Get in touch with questions, feedback, or collaboration opportunities."
%}

<section class="contact-section">
  <div class="container">
    <div class="contact-content">
      
      <div class="contact-methods">
        <h2>Get in Touch</h2>
        <p>
          Whether you have questions about our products, need technical support, or are interested 
          in collaborating with us, we're here to help.
        </p>
        
        <div class="contact-cards">
          <div class="contact-card">
            <div class="contact-icon">📧</div>
            <h3>Email</h3>
            <p>For general inquiries, support, or partnership opportunities</p>
            <a href="mailto:hello@bastionai.com" class="contact-link">hello@bastionai.com</a>
          </div>
          
          <div class="contact-card">
            <div class="contact-icon">🐙</div>
            <h3>GitHub</h3>
            <p>Follow our development, report issues, or contribute to our projects</p>
            <a href="https://github.com/bastionai" class="contact-link" target="_blank">github.com/bastionai</a>
          </div>
          
          <div class="contact-card">
            <div class="contact-icon">🛠️</div>
            <h3>Technical Support</h3>
            <p>Need help with BastionChat or other products?</p>
            <a href="mailto:support@bastionai.com" class="contact-link">support@bastionai.com</a>
          </div>
          
          <div class="contact-card">
            <div class="contact-icon">🤝</div>
            <h3>Partnerships</h3>
            <p>Interested in collaboration or business opportunities?</p>
            <a href="mailto:partnerships@bastionai.com" class="contact-link">partnerships@bastionai.com</a>
          </div>
        </div>
      </div>
      
      <div class="contact-form-section">
        <h2>Send us a Message</h2>
        <form class="contact-form" action="#" method="POST">
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" required>
          </div>
          
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
          </div>
          
          <div class="form-group">
            <label for="subject">Subject</label>
            <select id="subject" name="subject" required>
              <option value="">Select a topic</option>
              <option value="general">General Inquiry</option>
              <option value="support">Technical Support</option>
              <option value="feature">Feature Request</option>
              <option value="bug">Bug Report</option>
              <option value="partnership">Partnership</option>
              <option value="other">Other</option>
            </select>
          </div>
          
          <div class="form-group">
            <label for="message">Message</label>
            <textarea id="message" name="message" rows="6" required 
                      placeholder="Tell us how we can help you..."></textarea>
          </div>
          
          <div class="form-group">
            <button type="submit" class="btn btn-primary btn-large">Send Message</button>
          </div>
        </form>
        
        <div class="privacy-note">
          <p>
            <strong>Privacy Note:</strong> We respect your privacy. Your contact information 
            will only be used to respond to your inquiry and will never be shared with third parties.
          </p>
        </div>
      </div>
      
    </div>
  </div>
</section>

<section class="community-section">
  <div class="container">
    <h2>Join Our Community</h2>
    <p class="community-intro">
      Stay updated with the latest developments, connect with other users, and help shape 
      the future of privacy-first AI.
    </p>
    
    <div class="community-options">
      <div class="community-option">
        <div class="community-icon">📰</div>
        <h3>Newsletter</h3>
        <p>Get updates about new features, releases, and privacy-focused AI insights.</p>
        <button class="btn btn-secondary">Subscribe</button>
      </div>
      
      <div class="community-option">
        <div class="community-icon">💬</div>
        <h3>Discussions</h3>
        <p>Join conversations about local AI, privacy, and our products.</p>
        <a href="https://github.com/bastionai/discussions" class="btn btn-secondary" target="_blank">Join Discussions</a>
      </div>
      
      <div class="community-option">
        <div class="community-icon">📚</div>
        <h3>Documentation</h3>
        <p>Access guides, tutorials, and technical documentation.</p>
        <a href="/docs" class="btn btn-secondary">View Docs</a>
      </div>
    </div>
  </div>
</section>

<section class="faq-section">
  <div class="container">
    <h2>Frequently Asked Questions</h2>
    
    <div class="faq-grid">
      <div class="faq-item">
        <h3>How do I get started with BastionChat?</h3>
        <p>
          BastionChat is currently in development. You can follow our progress on GitHub 
          and sign up for our newsletter to be notified when the beta is available.
        </p>
      </div>
      
      <div class="faq-item">
        <h3>Is BastionChat really private?</h3>
        <p>
          Yes! BastionChat runs entirely on your device. Your conversations never leave 
          your computer, and we don't collect any usage data or personal information.
        </p>
      </div>
      
      <div class="faq-item">
        <h3>What platforms does BastionChat support?</h3>
        <p>
          Currently, BastionChat is being developed for macOS with Apple Silicon optimization. 
          We're exploring support for other platforms based on community interest.
        </p>
      </div>
      
      <div class="faq-item">
        <h3>How can I contribute to the project?</h3>
        <p>
          We welcome contributions! Visit our GitHub repository to see how you can help 
          with development, documentation, or testing.
        </p>
      </div>
      
      <div class="faq-item">
        <h3>Do you offer commercial licensing?</h3>
        <p>
          We're exploring various licensing options for commercial use. Contact us at 
          partnerships@bastionai.com to discuss your specific needs.
        </p>
      </div>
      
      <div class="faq-item">
        <h3>How do I report a bug or security issue?</h3>
        <p>
          For bugs, please use our GitHub issues. For security concerns, email us directly 
          at security@bastionai.com with details of the issue.
        </p>
      </div>
    </div>
  </div>
</section>

<style>
.contact-section {
  padding: 5rem 0;
}

.contact-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: start;
}

.contact-methods h2 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: #1f2937;
}

.contact-methods p {
  font-size: 1.1rem;
  color: #6b7280;
  margin-bottom: 3rem;
  line-height: 1.6;
}

.contact-cards {
  display: grid;
  gap: 1.5rem;
}

.contact-card {
  background: #f9fafb;
  padding: 2rem;
  border-radius: 1rem;
  border: 1px solid #e5e7eb;
  transition: all 0.3s ease;
}

.contact-card:hover {
  background: white;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  transform: translateY(-2px);
}

.contact-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.contact-card h3 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
  color: #374151;
}

.contact-card p {
  color: #6b7280;
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.contact-link {
  color: #059669;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease;
}

.contact-link:hover {
  color: #047857;
  text-decoration: underline;
}

.contact-form-section h2 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: #1f2937;
}

.contact-form {
  background: #f9fafb;
  padding: 2.5rem;
  border-radius: 1rem;
  border: 1px solid #e5e7eb;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #374151;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #059669;
  box-shadow: 0 0 0 3px rgba(5, 150, 105, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

.btn {
  padding: 0.75rem 2rem;
  border: none;
  border-radius: 0.5rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
  cursor: pointer;
  display: inline-block;
  text-align: center;
}

.btn-primary {
  background-color: #059669;
  color: white;
}

.btn-primary:hover {
  background-color: #047857;
  transform: translateY(-1px);
}

.btn-secondary {
  background-color: transparent;
  color: #059669;
  border: 2px solid #059669;
}

.btn-secondary:hover {
  background-color: #059669;
  color: white;
}

.btn-large {
  padding: 1rem 2rem;
  font-size: 1.1rem;
}

.privacy-note {
  margin-top: 2rem;
  padding: 1.5rem;
  background: #f0f9ff;
  border-radius: 0.5rem;
  border-left: 4px solid #0891b2;
}

.privacy-note p {
  margin: 0;
  font-size: 0.9rem;
  color: #0c4a6e;
}

.community-section {
  background: #f9fafb;
  padding: 5rem 0;
}

.community-section h2 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: #1f2937;
}

.community-intro {
  text-align: center;
  font-size: 1.1rem;
  color: #6b7280;
  max-width: 600px;
  margin: 0 auto 3rem;
}

.community-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.community-option {
  background: white;
  padding: 2.5rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.community-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.community-option h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #374151;
}

.community-option p {
  color: #6b7280;
  margin-bottom: 2rem;
}

.faq-section {
  padding: 5rem 0;
}

.faq-section h2 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: #1f2937;
}

.faq-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
}

.faq-item {
  background: #f9fafb;
  padding: 2rem;
  border-radius: 1rem;
  border: 1px solid #e5e7eb;
}

.faq-item h3 {
  font-size: 1.25rem;
  margin-bottom: 1rem;
  color: #059669;
}

.faq-item p {
  color: #6b7280;
  line-height: 1.6;
  margin: 0;
}

@media (max-width: 768px) {
  .contact-content {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  
  .contact-form {
    padding: 1.5rem;
  }
  
  .community-options {
    grid-template-columns: 1fr;
  }
  
  .faq-grid {
    grid-template-columns: 1fr;
  }
}
</style> 
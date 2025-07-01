---
layout: default
title: "Privacy Policy & Acknowledgments - Bastion Chat"
description: "Complete privacy policy and open-source acknowledgments for Bastion Chat"
permalink: /privacy-acknowledgments/
---

<section class="privacy-acknowledgments-header">
  <div class="container">
    <h1>Privacy Policy & Acknowledgments</h1>
    <p class="subtitle">Bastion Chat - Complete Privacy and Open Source Information</p>
  </div>
</section>

<section class="content-wrapper">
  <div class="container">
    <div class="content-grid">
      
      <!-- Table of Contents -->
      <div class="toc-sidebar">
        <h3>Contents</h3>
        <ul class="toc-list">
          <li><a href="#privacy-policy">Privacy Policy</a></li>
          <li><a href="#acknowledgments">Acknowledgments</a></li>
          <li><a href="#swift-dependencies">Swift Dependencies</a></li>
          <li><a href="#ai-models">AI Models & Licensing</a></li>
          <li><a href="#core-inference">Core Inference Engine</a></li>
        </ul>
      </div>

      <!-- Main Content -->
      <div class="main-content">
        
        <!-- Privacy Policy Section -->
        <section id="privacy-policy" class="content-section">
          <h2>Privacy Policy for Bastion Chat</h2>
          
          <div class="privacy-meta">
            <p><strong>Effective Date</strong>: January 25, 2025</p>
            <p><strong>Last Updated</strong>: January 25, 2025</p>
          </div>

          <h3>Overview</h3>
          <p>Bastion Chat is designed with privacy as our core principle. This Privacy Policy explains how we handle information in our AI chat assistant application.</p>

          <h3>Our Privacy Commitment</h3>
          <div class="privacy-highlight">
            <p><strong>We do not collect, store, transmit, or have access to any of your personal data, conversations, or documents.</strong></p>
          </div>

          <h3>Information We Do NOT Collect</h3>
          <div class="not-collected-list">
            <div class="not-collected-item">
              <span class="icon">❌</span>
              <div class="content">
                <strong>Chat Conversations</strong>
                <p>Your conversations with AI models remain entirely on your device</p>
              </div>
            </div>
            <div class="not-collected-item">
              <span class="icon">❌</span>
              <div class="content">
                <strong>Documents</strong>
                <p>Uploaded PDFs, text files, and web content stay local</p>
              </div>
            </div>
            <div class="not-collected-item">
              <span class="icon">❌</span>
              <div class="content">
                <strong>Voice Data</strong>
                <p>Speech recordings and transcriptions are processed locally</p>
              </div>
            </div>
            <div class="not-collected-item">
              <span class="icon">❌</span>
              <div class="content">
                <strong>Personal Information</strong>
                <p>No names, email addresses, or contact information collected</p>
              </div>
            </div>
            <div class="not-collected-item">
              <span class="icon">❌</span>
              <div class="content">
                <strong>Usage Analytics</strong>
                <p>No telemetry, crash reports, or usage statistics transmitted</p>
              </div>
            </div>
            <div class="not-collected-item">
              <span class="icon">❌</span>
              <div class="content">
                <strong>Device Information</strong>
                <p>No device IDs, IP addresses, or system information collected</p>
              </div>
            </div>
            <div class="not-collected-item">
              <span class="icon">❌</span>
              <div class="content">
                <strong>Location Data</strong>
                <p>No location tracking or geo-data collection</p>
              </div>
            </div>
          </div>

          <h3>How Bastion Chat Works</h3>
          <div class="how-it-works">
            <div class="work-item">
              <h4>🔒 100% Local Processing</h4>
              <ul>
                <li>All AI model inference happens on your device</li>
                <li>Conversations, document processing, and voice recognition occur locally</li>
                <li>No data is sent to external servers for processing</li>
              </ul>
            </div>
            <div class="work-item">
              <h4>📱 Local Storage Only</h4>
              <ul>
                <li>Chat history is stored in a local SQLite database on your device</li>
                <li>Documents are processed and stored locally using vector embeddings</li>
                <li>All user preferences and settings remain on your device</li>
              </ul>
            </div>
            <div class="work-item">
              <h4>🌐 Limited Network Usage</h4>
              <p>The app only connects to the internet for:</p>
              <ul>
                <li><strong>Model Downloads</strong>: Downloading AI models from Hugging Face repositories</li>
                <li><strong>Web Document Ingestion</strong>: When you explicitly choose to add a web URL to your knowledge base</li>
              </ul>
              <p>Network requests are made directly to:</p>
              <ul>
                <li><strong>Hugging Face (huggingface.co)</strong>: For downloading AI models</li>
                <li><strong>User-specified websites</strong>: Only when you provide a URL to add to your knowledge base</li>
              </ul>
              <p><strong>No data about you or your usage is transmitted during these connections.</strong></p>
            </div>
          </div>

          <h3>Permissions We Request</h3>
          <div class="permissions-list">
            <div class="permission-item">
              <h4>🎤 Microphone Access</h4>
              <ul>
                <li><strong>Purpose</strong>: Convert your voice to text for AI conversations</li>
                <li><strong>Processing</strong>: Speech recognition happens locally using iOS Speech Recognition</li>
                <li><strong>Storage</strong>: Voice data is processed in real-time and not stored</li>
              </ul>
            </div>
            <div class="permission-item">
              <h4>📸 Camera Access</h4>
              <ul>
                <li><strong>Purpose</strong>: Take photos for multimodal AI features that can analyze images</li>
                <li><strong>Processing</strong>: Image analysis happens locally on your device</li>
                <li><strong>Storage</strong>: Images are only stored if you explicitly choose to save them</li>
              </ul>
            </div>
            <div class="permission-item">
              <h4>📂 File Access</h4>
              <ul>
                <li><strong>Purpose</strong>: Allow you to upload documents (PDFs, text files) to your knowledge base</li>
                <li><strong>Processing</strong>: Document parsing and embedding generation happen locally</li>
                <li><strong>Storage</strong>: Documents are stored locally and processed for search</li>
              </ul>
            </div>
            <div class="permission-item">
              <h4>🌐 Network Access</h4>
              <ul>
                <li><strong>Purpose</strong>: Download AI models and optionally ingest web content you specify</li>
                <li><strong>Scope</strong>: Limited to model downloads and user-requested web content</li>
                <li><strong>Privacy</strong>: No personal data is transmitted</li>
              </ul>
            </div>
          </div>

          <h3>Data Security</h3>
          <div class="security-features">
            <div class="security-item">
              <h4>🔐 Device-Level Security</h4>
              <ul>
                <li>Data is protected by your device's built-in security (encryption at rest)</li>
                <li>Face ID/Touch ID integration for app-level authentication</li>
                <li>All processing happens within the app's sandboxed environment</li>
              </ul>
            </div>
            <div class="security-item">
              <h4>🛡️ No Cloud Vulnerabilities</h4>
              <ul>
                <li>No cloud storage means no risk of remote data breaches</li>
                <li>No external API keys or tokens stored</li>
                <li>No third-party analytics or tracking services</li>
              </ul>
            </div>
          </div>

          <h3>Your Rights</h3>
          <p>Since we don't collect your data:</p>
          <ul>
            <li><strong>No Data to Delete</strong>: All data is yours and remains on your device</li>
            <li><strong>No Data to Export</strong>: Your data never leaves your device unless you choose to back it up</li>
            <li><strong>Complete Control</strong>: You can delete the app to remove all associated data</li>
          </ul>

          <h3>Children's Privacy</h3>
          <p>Bastion Chat does not collect personal information from anyone, including children under 13. The app's privacy-first design ensures no data collection regardless of user age.</p>

          <h3>Changes to Privacy Policy</h3>
          <p>We will update this policy if our privacy practices change. Since we don't collect contact information, updates will be communicated through app updates.</p>

          <h3>Contact Information</h3>
          <p>For privacy-related questions:</p>
          <ul>
            <li><strong>GitHub Issues</strong>: Report concerns through our public repository</li>
            <li><strong>Documentation</strong>: Refer to our technical documentation for architecture details</li>
          </ul>

          <h3>Compliance</h3>
          <p>This privacy policy is designed to comply with:</p>
          <ul>
            <li><strong>Apple App Store Guidelines</strong></li>
            <li><strong>General Data Protection Regulation (GDPR)</strong></li>
            <li><strong>California Consumer Privacy Act (CCPA)</strong></li>
            <li><strong>Children's Online Privacy Protection Act (COPPA)</strong></li>
          </ul>
          <p>Since we don't collect personal data, compliance is achieved through our privacy-by-design architecture.</p>

          <div class="privacy-summary">
            <hr>
            <p><strong>Summary</strong>: Bastion Chat is built on the principle that your conversations, documents, and personal data should remain private and under your control. Our local-first architecture ensures your privacy is protected by design, not just by policy.</p>
            <p class="tagline"><em>Your AI, Your Data, Your Device.</em></p>
          </div>
        </section>

        <!-- Acknowledgments Section -->
        <section id="acknowledgments" class="content-section">
          <h2>Acknowledgments & Third-Party Licenses</h2>
          
          <p>Bastion Chat makes use of several open-source libraries and AI models. We gratefully acknowledge the contributions of these projects and their maintainers.</p>

          <h3 id="swift-dependencies">Swift Package Dependencies</h3>

          <div class="dependency-grid">
            <div class="dependency-item">
              <h4>NetworkImage</h4>
              <p><strong>Repository</strong>: <a href="https://github.com/gonzalezreal/NetworkImage">https://github.com/gonzalezreal/NetworkImage</a></p>
              <p><strong>License</strong>: MIT License</p>
              <p><strong>Purpose</strong>: Efficient image loading and caching</p>
              <p><strong>Author</strong>: Guille Gonzalez</p>
            </div>

            <div class="dependency-item">
              <h4>SwiftSoup</h4>
              <p><strong>Repository</strong>: <a href="https://github.com/scinfu/SwiftSoup">https://github.com/scinfu/SwiftSoup</a></p>
              <p><strong>License</strong>: MIT License</p>
              <p><strong>Purpose</strong>: HTML parsing for web content ingestion</p>
              <p><strong>Author</strong>: Nabil Chatbi</p>
            </div>

            <div class="dependency-item">
              <h4>swift-markdown-ui</h4>
              <p><strong>Repository</strong>: <a href="https://github.com/gonzalezreal/swift-markdown-ui">https://github.com/gonzalezreal/swift-markdown-ui</a></p>
              <p><strong>License</strong>: MIT License</p>
              <p><strong>Purpose</strong>: Markdown rendering in SwiftUI</p>
              <p><strong>Author</strong>: Guille Gonzalez</p>
            </div>

            <div class="dependency-item">
              <h4>swift-atomics</h4>
              <p><strong>Repository</strong>: <a href="https://github.com/apple/swift-atomics.git">https://github.com/apple/swift-atomics.git</a></p>
              <p><strong>License</strong>: Apache License 2.0</p>
              <p><strong>Purpose</strong>: Atomic operations for thread-safe programming</p>
              <p><strong>Author</strong>: Apple Inc.</p>
            </div>

            <div class="dependency-item">
              <h4>swift-cmark</h4>
              <p><strong>Repository</strong>: <a href="https://github.com/swiftlang/swift-cmark">https://github.com/swiftlang/swift-cmark</a></p>
              <p><strong>License</strong>: Multiple (BSD-style, see repository)</p>
              <p><strong>Purpose</strong>: CommonMark parsing</p>
              <p><strong>Author</strong>: Swift Project Authors</p>
            </div>
          </div>

          <h3 id="core-inference">Core Inference Engine</h3>

          <div class="dependency-item featured">
            <h4>llama.cpp</h4>
            <p><strong>Repository</strong>: <a href="https://github.com/ggerganov/llama.cpp">https://github.com/ggerganov/llama.cpp</a></p>
            <p><strong>License</strong>: MIT License</p>
            <p><strong>Purpose</strong>: High-performance LLM inference engine</p>
            <p><strong>Author</strong>: Georgi Gerganov and contributors</p>
            <p><strong>Note</strong>: Foundation for GGUF model inference and optimization</p>
          </div>

          <h3 id="ai-models">AI Models & Licensing</h3>

          <div class="models-disclaimer">
            <p><strong>Important:</strong> The following AI models are available for download through Bastion Chat. <strong>Users are responsible for compliance with individual model licenses.</strong></p>
          </div>

          <div class="model-families">
            <div class="model-family">
              <h4>Llama Models</h4>
              <p><strong>Models</strong>: Llama-3.2-1B-Instruct & Llama-3.2-3B-Instruct</p>
              <p><strong>License</strong>: Llama 3.2 Community License Agreement</p>
              <p><strong>Provider</strong>: Meta Platforms, Inc.</p>
              <p><strong>Usage</strong>: Instruction-following and general chat</p>
              <p><strong>License URL</strong>: <a href="https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct/blob/main/LICENSE.txt">View License</a></p>
            </div>

            <div class="model-family">
              <h4>Hermes Models</h4>
              <p><strong>Models</strong>: Hermes-3-Llama-3.2-3B</p>
              <p><strong>License</strong>: Based on Llama 3.2 (Llama 3.2 Community License)</p>
              <p><strong>Provider</strong>: NousResearch</p>
              <p><strong>Usage</strong>: Enhanced instruction-following and chat</p>
              <p><strong>Note</strong>: Fine-tuned version of Llama 3.2, subject to base model license</p>
            </div>

            <div class="model-family">
              <h4>Qwen Models</h4>
              <p><strong>Models</strong>: Qwen3-1.7B-UD, Qwen3-4B-UD, Qwen2.5-0.5B</p>
              <p><strong>License</strong>: Qwen License Agreement</p>
              <p><strong>Provider</strong>: Alibaba Cloud</p>
              <p><strong>Usage</strong>: Multilingual chat and reasoning</p>
              <p><strong>License URL</strong>: <a href="https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/blob/main/LICENSE">View License</a></p>
            </div>

            <div class="model-family">
              <h4>Phi Models</h4>
              <p><strong>Models</strong>: Phi-4-mini-instruct, LLaVA-Phi-3-mini</p>
              <p><strong>License</strong>: MIT License</p>
              <p><strong>Provider</strong>: Microsoft Corporation</p>
              <p><strong>Usage</strong>: Coding, math, and multimodal understanding</p>
              <p><strong>License URL</strong>: <a href="https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/LICENSE">View License</a></p>
            </div>

            <div class="model-family">
              <h4>Gemma Models</h4>
              <p><strong>Models</strong>: Gemma-3-4B-Instruct</p>
              <p><strong>License</strong>: Gemma Terms of Use</p>
              <p><strong>Provider</strong>: Google LLC</p>
              <p><strong>Usage</strong>: Multimodal understanding and generation</p>
              <p><strong>License URL</strong>: <a href="https://ai.google.dev/gemma/terms">View License</a></p>
            </div>
          </div>

          <h3>BERT Model for Embeddings</h3>

          <div class="dependency-item">
            <h4>all-MiniLM-L6-v2</h4>
            <p><strong>License</strong>: Apache License 2.0</p>
            <p><strong>Provider</strong>: Microsoft Corporation / Hugging Face</p>
            <p><strong>Repository</strong>: sentence-transformers/all-MiniLM-L6-v2</p>
            <p><strong>Purpose</strong>: Semantic embeddings for document search</p>
            <p><strong>Usage</strong>: Local embedding generation for RAG functionality</p>
            <p><strong>License URL</strong>: <a href="https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/LICENSE">View License</a></p>
          </div>

          <h3>Model Usage Terms</h3>

          <div class="usage-terms">
            <h4>Important Notes for Users:</h4>
            <ol>
              <li><strong>Model Downloads</strong>: Models are downloaded directly from their respective repositories</li>
              <li><strong>License Compliance</strong>: Users must comply with individual model licenses</li>
              <li><strong>Commercial Use</strong>: Check specific model licenses for commercial usage terms</li>
              <li><strong>Attribution</strong>: Some models may require attribution in commercial applications</li>
              <li><strong>Redistribution</strong>: Bastion Chat does not redistribute models; they are downloaded on-demand</li>
            </ol>

            <div class="responsibility-statement">
              <p><strong>The user is solely responsible for ensuring compliance with all applicable licenses when using AI models through Bastion Chat.</strong> The app facilitates access to these models but does not grant any additional rights beyond those specified in the original model licenses.</p>
            </div>
          </div>

          <h3>Additional Technologies</h3>

          <div class="additional-tech">
            <div class="tech-item">
              <h4>SQLite</h4>
              <p><strong>License</strong>: Public Domain</p>
              <p><strong>Purpose</strong>: Local database storage</p>
              <p><strong>Website</strong>: <a href="https://sqlite.org/">https://sqlite.org/</a></p>
            </div>

            <div class="tech-item">
              <h4>Apple Frameworks</h4>
              <p><strong>Frameworks</strong>: SwiftUI, Foundation, Combine, AVFoundation, Speech, CoreML</p>
              <p><strong>License</strong>: Apple Software License Agreement</p>
              <p><strong>Provider</strong>: Apple Inc.</p>
              <p><strong>Purpose</strong>: iOS app development and system integration</p>
            </div>
          </div>

          <div class="final-notes">
            <p><strong>Last Updated</strong>: January 25, 2025</p>
            <p><strong>Bastion Chat Version</strong>: 1.0.1</p>
            <p><em>We are grateful to all open-source contributors who make projects like Bastion Chat possible.</em></p>
          </div>
        </section>

      </div>
    </div>
  </div>
</section>

<style>
.privacy-acknowledgments-header {
  background: linear-gradient(135deg, #1e40af 0%, #7c3aed 100%);
  color: white;
  padding: 4rem 0 2rem;
  text-align: center;
}

.privacy-acknowledgments-header h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  font-weight: 800;
}

.subtitle {
  font-size: 1.25rem;
  opacity: 0.9;
  margin: 0;
}

.content-wrapper {
  padding: 3rem 0;
  background: #f8fafc;
}

.content-grid {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 3rem;
  max-width: 1200px;
  margin: 0 auto;
}

.toc-sidebar {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  height: fit-content;
  position: sticky;
  top: 2rem;
}

.toc-sidebar h3 {
  margin-bottom: 1rem;
  color: #374151;
  font-size: 1.125rem;
}

.toc-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.toc-list li {
  margin-bottom: 0.5rem;
}

.toc-list a {
  color: #6366f1;
  text-decoration: none;
  font-size: 0.9rem;
  padding: 0.5rem 0;
  display: block;
  border-radius: 0.25rem;
  transition: all 0.3s ease;
}

.toc-list a:hover {
  background: #f0f9ff;
  padding-left: 0.5rem;
}

.main-content {
  background: white;
  border-radius: 1rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}

.content-section {
  padding: 3rem;
  border-bottom: 1px solid #e5e7eb;
}

.content-section:last-child {
  border-bottom: none;
}

.content-section h2 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: #1f2937;
  font-weight: 800;
}

.content-section h3 {
  font-size: 1.5rem;
  margin: 2rem 0 1rem 0;
  color: #374151;
  font-weight: 700;
  border-bottom: 2px solid #e5e7eb;
  padding-bottom: 0.5rem;
}

.content-section h4 {
  font-size: 1.125rem;
  margin: 1.5rem 0 0.75rem 0;
  color: #4b5563;
  font-weight: 600;
}

.privacy-meta {
  background: #f0f9ff;
  padding: 1rem;
  border-radius: 0.5rem;
  margin-bottom: 2rem;
  border-left: 4px solid #3b82f6;
}

.privacy-meta p {
  margin: 0.25rem 0;
  font-size: 0.9rem;
  color: #1e40af;
}

.privacy-highlight {
  background: #dcfce7;
  padding: 1.5rem;
  border-radius: 0.75rem;
  margin: 1.5rem 0;
  border: 1px solid #16a34a;
}

.privacy-highlight p {
  margin: 0;
  font-size: 1.125rem;
  color: #166534;
  text-align: center;
}

.not-collected-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.not-collected-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem;
  background: #fef2f2;
  border-radius: 0.5rem;
  border: 1px solid #fecaca;
}

.not-collected-item .icon {
  font-size: 1.25rem;
  margin-top: 0.125rem;
}

.not-collected-item .content strong {
  display: block;
  color: #991b1b;
  margin-bottom: 0.25rem;
  font-weight: 600;
}

.not-collected-item .content p {
  margin: 0;
  color: #7f1d1d;
  font-size: 0.9rem;
  line-height: 1.4;
}

.how-it-works {
  margin: 1.5rem 0;
}

.work-item {
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: #f0f9ff;
  border-radius: 0.75rem;
  border: 1px solid #dbeafe;
}

.work-item h4 {
  color: #1e40af;
  margin-bottom: 1rem;
  font-size: 1.125rem;
}

.permissions-list {
  margin: 1.5rem 0;
}

.permission-item {
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  background: #fefce8;
  border-radius: 0.75rem;
  border: 1px solid #fef08a;
}

.permission-item h4 {
  color: #a16207;
  margin-bottom: 0.75rem;
}

.security-features {
  margin: 1.5rem 0;
}

.security-item {
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  background: #f0fdf4;
  border-radius: 0.75rem;
  border: 1px solid #dcfce7;
}

.security-item h4 {
  color: #166534;
  margin-bottom: 0.75rem;
}

.privacy-summary {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 2px solid #e5e7eb;
}

.privacy-summary p {
  text-align: center;
  font-size: 1.125rem;
  line-height: 1.6;
  color: #374151;
}

.privacy-summary .tagline {
  font-size: 1.25rem;
  font-weight: 600;
  color: #4f46e5;
  margin-top: 1rem;
}

.dependency-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.dependency-item {
  background: #f8fafc;
  padding: 1.5rem;
  border-radius: 0.75rem;
  border: 1px solid #e5e7eb;
}

.dependency-item.featured {
  background: #f0f9ff;
  border-color: #3b82f6;
}

.dependency-item h4 {
  color: #374151;
  margin-bottom: 1rem;
  font-size: 1.25rem;
}

.dependency-item p {
  margin: 0.5rem 0;
  font-size: 0.9rem;
  line-height: 1.5;
}

.dependency-item a {
  color: #3b82f6;
  text-decoration: none;
}

.dependency-item a:hover {
  text-decoration: underline;
}

.models-disclaimer {
  background: #fef3c7;
  padding: 1.5rem;
  border-radius: 0.75rem;
  border: 1px solid #fbbf24;
  margin: 1.5rem 0;
}

.models-disclaimer p {
  margin: 0;
  color: #92400e;
  font-weight: 500;
}

.model-families {
  margin: 2rem 0;
}

.model-family {
  background: #f5f3ff;
  padding: 1.5rem;
  border-radius: 0.75rem;
  border: 1px solid #e9d5ff;
  margin-bottom: 1.5rem;
}

.model-family h4 {
  color: #6b21a8;
  margin-bottom: 1rem;
}

.model-family p {
  margin: 0.5rem 0;
  font-size: 0.9rem;
  line-height: 1.5;
}

.model-family a {
  color: #3b82f6;
  text-decoration: none;
}

.model-family a:hover {
  text-decoration: underline;
}

.usage-terms {
  background: #f0fdf4;
  padding: 2rem;
  border-radius: 0.75rem;
  border: 1px solid #dcfce7;
  margin: 2rem 0;
}

.usage-terms h4 {
  color: #166534;
  margin-bottom: 1rem;
}

.usage-terms ol {
  padding-left: 1.5rem;
  margin: 1rem 0;
}

.usage-terms li {
  margin-bottom: 0.5rem;
  line-height: 1.6;
}

.responsibility-statement {
  background: #fef2f2;
  padding: 1.5rem;
  border-radius: 0.5rem;
  border-left: 4px solid #ef4444;
  margin-top: 1.5rem;
}

.responsibility-statement p {
  margin: 0;
  color: #991b1b;
  font-weight: 500;
}

.additional-tech {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.tech-item {
  background: #f9fafb;
  padding: 1.5rem;
  border-radius: 0.75rem;
  border: 1px solid #e5e7eb;
}

.tech-item h4 {
  color: #374151;
  margin-bottom: 1rem;
}

.tech-item p {
  margin: 0.5rem 0;
  font-size: 0.9rem;
  line-height: 1.5;
}

.tech-item a {
  color: #3b82f6;
  text-decoration: none;
}

.tech-item a:hover {
  text-decoration: underline;
}

.final-notes {
  background: #f8fafc;
  padding: 2rem;
  border-radius: 0.75rem;
  border-top: 3px solid #6366f1;
  margin-top: 2rem;
  text-align: center;
}

.final-notes p {
  margin: 0.5rem 0;
  color: #6b7280;
}

.final-notes em {
  color: #4f46e5;
  font-weight: 500;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
  .privacy-acknowledgments-header h1 {
    font-size: 2rem;
  }
  
  .content-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .toc-sidebar {
    position: static;
    order: 2;
    margin-top: 2rem;
  }
  
  .content-section {
    padding: 2rem 1.5rem;
  }
  
  .content-section h2 {
    font-size: 2rem;
  }
  
  .not-collected-list,
  .dependency-grid,
  .additional-tech {
    grid-template-columns: 1fr;
  }
  
  .dependency-item,
  .model-family,
  .tech-item {
    padding: 1rem;
  }
}
</style> 
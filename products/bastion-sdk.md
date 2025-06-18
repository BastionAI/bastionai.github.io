---
layout: default
title: "BastionSDK - Local AI for Swift Developers"
description: "A Swift Package for running open source LLM frameworks locally on Apple platforms using familiar OpenAI-compatible APIs. Build privacy-first AI apps for iOS and macOS."
permalink: /products/bastion-sdk/
---

{% include components/header.html type="hero" title="BastionSDK" subtitle="Local AI for Swift Developers" description="A powerful Swift Package that brings open source LLM frameworks to iOS and macOS with OpenAI-compatible APIs. Build privacy-first AI applications that run entirely on-device." %}

<div class="content-section">
  <div class="container">
    <div class="feature-grid">
      <div class="feature-card">
        <div class="feature-icon">🚀</div>
        <h3>OpenAI-Compatible API</h3>
        <p>Familiar Swift API structure mimicking OpenAI libraries. Easy migration from cloud to local AI with minimal code changes.</p>
      </div>
      
      <div class="feature-card">
        <div class="feature-icon">📱</div>
        <h3>Apple Platform Native</h3>
        <p>Built specifically for iOS and macOS with Metal GPU acceleration. Optimized for Apple Silicon and mobile devices.</p>
      </div>
      
      <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <h3>Privacy by Design</h3>
        <p>All AI processing happens locally on device. No data ever leaves your user's device - complete privacy guarantee.</p>
      </div>
      
      <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h3>Hardware Acceleration</h3>
        <p>Leverages Apple's Neural Engine, Metal GPU, and CPU optimizations. Fast inference on iPhone, iPad, and Mac devices.</p>
      </div>
      
      <div class="feature-card">
        <div class="feature-icon">🛠️</div>
        <h3>Production Ready</h3>
        <p>Streaming and non-streaming completion, chat templates, GBNF grammar support, and robust error handling.</p>
      </div>
      
      <div class="feature-card">
        <div class="feature-icon">🔧</div>
        <h3>Developer Friendly</h3>
        <p>Async/await support, comprehensive documentation, and Swift Package Manager integration. Just add and use.</p>
      </div>
    </div>
  </div>
</div>

<div class="content-section bg-light">
  <div class="container">
    <div class="text-center">
      <h2>Your AI, Your Rules</h2>
      <p class="lead">Build AI-powered iOS and macOS apps without compromising on privacy or performance</p>
    </div>
    
    <div class="two-column">
      <div class="column">
        <h3>Core Features</h3>
        <ul class="feature-list">
                     <li><strong>OpenAI-Compatible Swift API</strong> - BastionChatEngine, ChatCompletionRequest, familiar patterns</li>
           <li><strong>Local LLM Inference</strong> - Multiple model engine support including CoreML and open source frameworks</li>
          <li><strong>Model Management</strong> - Async model loading and unloading with resource management</li>
          <li><strong>Streaming Support</strong> - Real-time token streaming with interruptible generation</li>
          <li><strong>Chat Templates</strong> - Robust template application using model's built-in templates</li>
          <li><strong>Advanced Parameters</strong> - Temperature, Top-K, Top-P, penalties, stop sequences</li>
          <li><strong>GBNF Grammar</strong> - Constrained output generation for structured data</li>
          <li><strong>Token Statistics</strong> - Usage tracking for non-streaming completions</li>
        </ul>
      </div>
      
      <div class="column">
                 <h3>Technical Architecture</h3>
         <div class="architecture-diagram">
           <div class="layer">
             <strong>Swift API Layer</strong>
             <span>BastionSDK - Your application interface</span>
           </div>
           <div class="arrow">↓</div>
           <div class="layer">
             <strong>Model Engine Layer</strong>
             <span>CoreML, Open Source Frameworks, Native Engines</span>
           </div>
           <div class="arrow">↓</div>
           <div class="layer">
             <strong>Hardware Acceleration</strong>
             <span>Metal GPU, Neural Engine, CPU optimization</span>
           </div>
         </div>
        
                 <h4>Platform Support</h4>
         <ul>
           <li><strong>iOS 15.0+</strong> - iPhone and iPad with Neural Engine</li>
           <li><strong>macOS 12.0+</strong> - Apple Silicon and Intel Macs</li>
           <li><strong>Multiple Engines</strong> - CoreML, Metal GPU, CPU optimization</li>
         </ul>
      </div>
    </div>
  </div>
</div>

<div class="content-section">
  <div class="container">
    <h2>Quick Start Guide</h2>
    
    <div class="code-example">
      <h3>1. Add BastionSDK to Your Project</h3>
      <pre><code>// Add to your Package.swift dependencies
.package(url: "https://github.com/BastionAI/BastionSDK.git", from: "1.0.0")</code></pre>
    </div>
    
         <div class="code-example">
       <h3>2. Basic Usage</h3>
       <pre><code>import BastionSDK
 import Foundation
 
 // Initialize the engine
 let engine = BastionChatEngine()
 
 // Configure model engine (CoreML, Open Source, etc.)
 let config = ModelConfiguration(
     engine: .coreML,        // or .openSource, .metal
     contextSize: 4096,
     temperature: 0.7,
     useHardwareAcceleration: true
 )
 
 // Load your model
 try await engine.loadModel(
     modelPath: "Models/your_model.mlpackage", // or .gguf for open source
     configuration: config
 )
 
 // Create chat completion
 let messages = [
     ChatMessage(role: .system, content: "You are a helpful assistant."),
     ChatMessage(role: .user, content: "Hello! How are you?")
 ]
 
 let request = ChatCompletionRequest(
     model: "my-model",
     messages: messages,
     temperature: 0.7,
     maxTokens: 150,
     stream: true
 )
 
 // Stream response
 let stream = try await engine.streamChatCompletion(request: request)
 for try await chunk in stream {
     if let content = chunk.choices.first?.delta.content {
         print(content, terminator: "")
     }
 }</code></pre>
    </div>
  </div>
</div>

<div class="content-section bg-light">
  <div class="container">
    <h2>Advanced Features</h2>
    
    <div class="three-column">
      <div class="column">
        <h3>Streaming & Non-Streaming</h3>
        <p>Support for both real-time streaming responses and traditional completion requests. Interruptible streaming allows users to stop generation at any time.</p>
      </div>
      
             <div class="column">
         <h3>Model Engine Flexibility</h3>
         <p>Support for multiple model engines including Apple CoreML, open source frameworks, and optimized native engines. Choose the best option for your use case.</p>
       </div>
      
      <div class="column">
        <h3>GBNF Grammar</h3>
        <p>Constrained output generation using GBNF grammar rules. Perfect for generating structured data, JSON, or following specific formats.</p>
      </div>
    </div>
    
    <div class="three-column">
             <div class="column">
         <h3>Hardware Acceleration</h3>
         <p>Leverage Apple's Neural Engine, Metal GPU, and CPU optimizations. Automatic hardware selection for optimal performance on each device.</p>
       </div>
      
      <div class="column">
        <h3>Robust Error Handling</h3>
        <p>Comprehensive error types and handling for model loading, inference failures, and resource management. Production-ready reliability.</p>
      </div>
      
      <div class="column">
        <h3>Resource Management</h3>
        <p>Efficient memory usage with async model loading/unloading. Proper cleanup and resource management for mobile environments.</p>
      </div>
    </div>
  </div>
</div>

<div class="content-section">
  <div class="container">
    <h2>Development Status</h2>
    
    <div class="status-grid">
      <div class="status-item completed">
        <div class="status-icon">✅</div>
        <h4>Core Engine</h4>
        <p>Model loading, unloading, and basic inference</p>
      </div>
      
      <div class="status-item completed">
        <div class="status-icon">✅</div>
        <h4>Streaming Support</h4>
        <p>Real-time token streaming with interruption</p>
      </div>
      
      <div class="status-item completed">
        <div class="status-icon">✅</div>
        <h4>Chat Templates</h4>
        <p>Built-in template support via open source engines</p>
      </div>
      
             <div class="status-item completed">
         <div class="status-icon">✅</div>
         <h4>Hardware Acceleration</h4>
         <p>Neural Engine, Metal GPU, CPU optimization</p>
       </div>
      
      <div class="status-item in-progress">
        <div class="status-icon">🚧</div>
        <h4>SwiftUI Integration</h4>
        <p>First available version targets SwiftUI apps</p>
      </div>
      
      <div class="status-item planned">
        <div class="status-icon">📋</div>
        <h4>Additional Platforms</h4>
        <p>Future support for watchOS and tvOS</p>
      </div>
    </div>
  </div>
</div>

<div class="content-section bg-light">
  <div class="container">
    <h2>Use Cases</h2>
    
    <div class="use-case-grid">
      <div class="use-case">
        <h3>📱 Personal AI Assistants</h3>
        <p>Build privacy-first AI assistants that run entirely on iPhone. No data leaves the device, perfect for personal productivity apps.</p>
      </div>
      
      <div class="use-case">
        <h3>💬 Offline Chat Apps</h3>
        <p>Create chat applications that work without internet connectivity. Perfect for remote areas or security-sensitive environments.</p>
      </div>
      
      <div class="use-case">
        <h3>📝 Content Creation</h3>
        <p>Writing assistants, code completion, and creative tools that respect user privacy while providing intelligent suggestions.</p>
      </div>
      
      <div class="use-case">
        <h3>🏥 Healthcare Apps</h3>
        <p>Medical and healthcare applications that can process sensitive data locally without HIPAA compliance concerns.</p>
      </div>
      
      <div class="use-case">
        <h3>🎓 Educational Tools</h3>
        <p>Learning applications that work in schools without internet dependency. Personalized tutoring that stays private.</p>
      </div>
      
      <div class="use-case">
        <h3>🏢 Enterprise Solutions</h3>
        <p>Business apps that can process confidential data locally. Perfect for air-gapped environments and sensitive workflows.</p>
      </div>
    </div>
  </div>
</div>

<div class="content-section">
  <div class="container">
    <div class="cta-section">
      <h2>Ready to Build Local AI Apps?</h2>
      <p>Join the privacy-first AI revolution. Start building iOS and macOS apps that respect user privacy while delivering powerful AI capabilities.</p>
      
      <div class="cta-buttons">
        <a href="mailto:bastionaisolutions@gmail.com?subject=BastionSDK%20Early%20Access&body=I'm%20interested%20in%20getting%20early%20access%20to%20BastionSDK%20for%20iOS%20development." class="btn btn-primary">Request Early Access</a>
        <a href="mailto:bastionaisolutions@gmail.com?subject=BastionSDK%20Documentation&body=I'd%20like%20to%20learn%20more%20about%20BastionSDK%20documentation%20and%20examples." class="btn btn-secondary">View Documentation</a>
      </div>
      
      <p class="note">Currently in active development. First version available for SwiftUI applications.</p>
    </div>
  </div>
</div>

<style>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  text-align: center;
  transition: transform 0.2s, box-shadow 0.2s;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  color: #111827;
  margin-bottom: 1rem;
}

.architecture-diagram {
  background: #f9fafb;
  padding: 1.5rem;
  border-radius: 8px;
  margin: 1rem 0;
}

.layer {
  background: white;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #d1d5db;
  margin-bottom: 0.5rem;
}

.layer strong {
  display: block;
  color: #059669;
  margin-bottom: 0.25rem;
}

.arrow {
  text-align: center;
  font-size: 1.5rem;
  color: #6b7280;
  margin: 0.5rem 0;
}

.code-example {
  margin: 2rem 0;
}

.code-example pre {
  background: #1f2937;
  color: #f9fafb;
  padding: 1.5rem;
  border-radius: 8px;
  overflow-x: auto;
  font-size: 0.875rem;
  line-height: 1.6;
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.status-item {
  display: flex;
  align-items: center;
  padding: 1.5rem;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.status-item.completed {
  background: #f0fdf4;
  border-color: #bbf7d0;
}

.status-item.in-progress {
  background: #fffbeb;
  border-color: #fed7aa;
}

.status-item.planned {
  background: #f8fafc;
  border-color: #e2e8f0;
}

.status-icon {
  font-size: 1.5rem;
  margin-right: 1rem;
}

.use-case-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.use-case {
  padding: 1.5rem;
  border-left: 4px solid #059669;
  background: white;
  border-radius: 0 8px 8px 0;
}

.use-case h3 {
  color: #111827;
  margin-bottom: 1rem;
}

.cta-section {
  text-align: center;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
  border-radius: 16px;
  margin: 3rem 0;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin: 2rem 0;
  flex-wrap: wrap;
}

.note {
  color: #6b7280;
  font-style: italic;
  margin-top: 1rem;
}

@media (max-width: 768px) {
  .feature-grid {
    grid-template-columns: 1fr;
  }
  
  .cta-buttons {
    flex-direction: column;
    align-items: center;
  }
  
  .cta-buttons .btn {
    width: 100%;
    max-width: 300px;
  }
}
</style> 
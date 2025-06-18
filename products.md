---
layout: default
title: "Products"
description: "Discover BastionAI's privacy-first AI solutions designed for security and innovation."
permalink: /products/
bastion_chat_features:
  - "iOS, iPadOS, and macOS app"
  - "100% local AI processing"
  - "Advanced voice interaction"
  - "Complete privacy protection"
bastion_chat_button:
  url: "/products/bastion-chat/"
  text: "Learn More"
  primary: true
---

{% include components/header.html 
   type="hero"
   title="Our Products"
   description="Privacy-first AI solutions that put you in control"
%}

<section class="content-section">
  <div class="container">
    <div class="products-grid">
      {% include components/product-card.html 
         logo="/assets/images/logos/bastion-chat-logo.png"
         title="BastionChat"
         description="Privacy-first AI assistant for iPhone, iPad, and Mac. Experience powerful AI conversations with complete local processing - no cloud, no tracking, no compromises."
         features=page.bastion_chat_features
         button=page.bastion_chat_button
      %}
    </div>
  </div>
</section>

<section class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">Coming Soon</h2>
      <p class="section-subtitle">We're working on more privacy-first AI solutions. Stay tuned for updates!</p>
    </div>
  </div>
</section>

 
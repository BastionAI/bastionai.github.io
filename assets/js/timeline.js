document.addEventListener('DOMContentLoaded', function() {
  // Intersection Observer for timeline animations
  const timelineItems = document.querySelectorAll('.timeline-item');
  const timelineLine = document.querySelector('.timeline-line');
  
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        console.log('Timeline item entering view:', entry.target.dataset.phase);
        entry.target.style.animationPlayState = 'running';
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        
        // Add special effects for BastionAI phase
        if (entry.target.dataset.phase === 'bastion-ai') {
          setTimeout(() => {
            entry.target.classList.add('future-glow');
          }, 800);
        }
      }
    });
  }, observerOptions);
  
  timelineItems.forEach((item, index) => {
    item.style.animationPlayState = 'paused';
    item.style.opacity = '0';
    item.style.transform = 'translateY(30px)';
    console.log(`Timeline item ${index}:`, item.dataset.phase);
    observer.observe(item);
  });
  
  // Click interactions for timeline items
  timelineItems.forEach(item => {
    const content = item.querySelector('.timeline-content');
    const marker = item.querySelector('.timeline-marker');
    
    if (content && marker) {
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
    }
  });
  
  // Progressive line drawing animation
  const drawLine = () => {
    const timelineSection = document.querySelector('.timeline-section');
    const timelineFuture = document.querySelector('.timeline-future');
    const timelineContainer = document.querySelector('.timeline-container');
    
    if (timelineSection && timelineLine && timelineFuture && timelineContainer) {
      const windowHeight = window.innerHeight;
      const scrollTop = window.pageYOffset;
      const viewportMiddle = scrollTop + (windowHeight / 2);
      
      // Key positions
      const sectionTop = timelineSection.offsetTop;
      const sectionBottom = sectionTop + timelineSection.offsetHeight;
      const futureTop = timelineFuture.offsetTop;
      const containerTop = timelineContainer.offsetTop;
      
      // Total line length (from container start to middle of future section)
      const lineMaxHeight = futureTop - containerTop + (timelineFuture.offsetHeight / 2);
      
      // Start drawing when section enters viewport
      const startPoint = sectionTop - 200;
      // Complete when future section middle aligns with viewport middle
      const endPoint = futureTop + (timelineFuture.offsetHeight / 2);
      
      if (viewportMiddle > startPoint) {
        // Calculate progress based on viewport middle position
        const progressDistance = viewportMiddle - startPoint;
        const totalDistance = endPoint - startPoint;
        const progress = Math.min(1, progressDistance / totalDistance);
        
        // Apply easing for smoother animation
        const easedProgress = progress < 0.5 
          ? 2 * progress * progress 
          : 1 - Math.pow(-2 * progress + 2, 3) / 2;
        
        const targetHeight = lineMaxHeight * easedProgress;
        timelineLine.style.height = `${targetHeight}px`;
      } else {
        timelineLine.style.height = '0px';
      }
    }
  };
  
  window.addEventListener('scroll', drawLine);
  drawLine(); // Initial call
  
  function showPhaseDetails(phaseId) {
    const details = {
      'pre-cloud-ai': {
        title: 'Pre-Cloud AI Era: On-Premises Systems',
        content: 'Early AI systems ran on local servers and individual computers with limited computational resources. Expert systems, robotics, and early machine learning required significant infrastructure investment, limiting access to large institutions.'
      },
      'cloud-ai': {
        title: 'The Cloud AI Era: Centralized Control',
        content: 'During this period, AI capabilities were concentrated in massive data centers owned by tech giants. Users had to surrender their data and accept limited customization for AI services.'
      },
      'edge-ai': {
        title: 'Edge AI: Moving Closer to Users',
        content: 'Edge AI emerged as a solution to latency and privacy concerns, bringing some processing closer to users. However, it still required technical expertise and offered limited model selection.'
      },
      'bastion-ai': {
        title: 'BastionAI: Privacy-First AI Solutions',
        content: 'BastionAI prioritizes privacy and security with flexible deployment options. While we champion local processing for maximum data sovereignty, we also support hybrid and cloud-native approaches when they align with privacy requirements.'
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
    if (detail) {
      detailElement.innerHTML = `
        <div class="timeline-detail-content">
          <h4>${detail.title}</h4>
          <p>${detail.content}</p>
          <button class="timeline-detail-close">✕</button>
        </div>
      `;
      
      detailElement.style.display = 'block';
      
      // Close button functionality
      const closeButton = detailElement.querySelector('.timeline-detail-close');
      if (closeButton) {
        closeButton.addEventListener('click', () => {
          detailElement.style.display = 'none';
        });
      }
    }
  }
}); 
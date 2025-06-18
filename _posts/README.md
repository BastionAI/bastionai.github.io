# Blog Posts Management Guide

This directory contains all blog posts for the BastionAI website. The blog system is designed to be maintainable and easy to use.

## File Structure

```
_posts/
├── README.md (this file)
├── 2024-12-28-future-of-local-ai-privacy-matters.md
└── YYYY-MM-DD-post-slug.md (future posts)
```

## Adding a New Blog Post

### 1. Create the Post File
Create a new file in the `_posts` directory with the format: `YYYY-MM-DD-post-slug.md`

### 2. Front Matter Template
Use this template for new blog posts:

```yaml
---
layout: blog-post
title: "Your Post Title"
subtitle: "Optional subtitle for more context"
description: "Meta description for SEO and social sharing (160 chars max)"
date: YYYY-MM-DD
author: "Author Name"
author_title: "Author Title (e.g., Founder & CEO, BastionAI)"
category: "Category Name"
tags: ["Tag1", "Tag2", "Tag3"]
permalink: /blog/your-post-slug/
toc: true  # Set to false if you don't want table of contents
---
```

### 3. Add to Blog Index
Update `blog.md` in the root directory to include your new post in the `blog_posts` array:

```yaml
blog_posts:
  - title: "Your Post Title"
    category: "Category Name"
    author: "Author Name"
    date: YYYY-MM-DD
    url: "/blog/your-post-slug/"
    description: "Brief description for the blog grid"
    tags: ["Tag1", "Tag2", "Tag3"]
    reading_time: X  # estimated reading time in minutes
    featured: false  # set to true to make it featured
```

## Categories
Use these standardized categories:
- AI Democratization
- Enterprise Architecture
- Technology Vision
- Technical Deep Dive
- Privacy & Security
- Product Updates

## Tags
Common tags to maintain consistency:
- Local AI
- Privacy
- Data Sovereignty
- Azure
- Enterprise AI
- Vector Databases
- RAG
- AI Ethics
- Technology Access
- Open Source

## Writing Guidelines

### Content Structure
1. **Introduction** - Hook the reader and set context
2. **Main Sections** - Use H2 headers for major sections
3. **Subsections** - Use H3 and H4 as needed
4. **Conclusion** - Summarize key points and call to action

### SEO Best Practices
- Use descriptive, keyword-rich titles
- Include meta descriptions under 160 characters
- Use header hierarchy (H2, H3, H4) properly
- Internal linking to other BastionAI pages when relevant

### Voice and Tone
- Authoritative but approachable
- Technical depth balanced with accessibility
- First-person perspective from Freddy's expertise
- Focus on practical insights and real-world applications

## Features Available

### Table of Contents
Set `toc: true` in front matter to automatically generate a table of contents from H2, H3, and H4 headers.

### Related Posts
Related posts are automatically shown based on matching categories.

### Social Sharing
Open Graph metadata is automatically generated from front matter.

### Reading Time
Reading time is calculated automatically and displayed in post meta.

## Local Development

To preview blog posts locally:
1. Ensure Jekyll is installed
2. Run `bundle exec jekyll serve`
3. Navigate to `http://localhost:4000/blog/`

## Publication Workflow

1. Create post file in `_posts/`
2. Add entry to `blog.md` front matter
3. Test locally
4. Commit and push to deploy

This system makes it easy to maintain a consistent blog while allowing for rich content and good SEO performance. 
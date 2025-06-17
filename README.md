# BastionAI Official Website

Welcome to the official website for BastionAI, a company focused on creating privacy-first AI solutions that leverage the power of local models.

## 🌐 Live Site

Visit our website at: [https://bastionai.github.io](https://bastionai.github.io)

## 🏢 About BastionAI

BastionAI creates products oriented to leverage the power of local models focusing on privacy, security, and innovation. We believe that the future of AI lies not in centralized cloud services, but in empowering users with powerful AI capabilities that run entirely on their own devices.

### Our Products

- **BastionChat**: A powerful local AI chat application featuring advanced capabilities with complete privacy
  - 100% local processing - no cloud dependencies
  - Voice mode and conversation capabilities
  - Document RAG support (PDF, web, text files)
  - Latest model support including Gemma 3 and Qwen 3 (thinking)

## 🛠 Technical Stack

This website is built using:

- **Jekyll** - Static site generator
- **GitHub Pages** - Hosting and deployment
- **GitHub Actions** - Automated CI/CD pipeline
- **Responsive Design** - Mobile-first approach
- **Modern CSS** - Custom styling with gradients and animations

## 📁 Site Structure

```
bastionai.github.io/
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── index.md                 # Homepage
├── products.md              # Products overview
├── about.md                 # About BastionAI
├── contact.md               # Contact information
├── products/
│   └── bastion-chat.md      # BastionChat detailed page
└── .github/
    └── workflows/
        └── deploy.yml       # GitHub Actions deployment
```

## 🚀 Local Development

To run this website locally:

### Prerequisites

- Ruby 3.1 or higher
- Bundler gem

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/bastionai/bastionai.github.io.git
   cd bastionai.github.io
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Serve the site locally:
   ```bash
   bundle exec jekyll serve
   ```

4. Open your browser and visit: `http://localhost:4000`

### Development Commands

```bash
# Serve with live reload
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build

# Serve with drafts
bundle exec jekyll serve --drafts

# Clean build artifacts
bundle exec jekyll clean
```

## 📦 Deployment

The site is automatically deployed to GitHub Pages using GitHub Actions when changes are pushed to the `main` branch.

### Deployment Process

1. **Automatic**: Push to `main` branch triggers GitHub Actions
2. **Manual**: Use the "Actions" tab in GitHub to manually trigger deployment
3. **Preview**: Pull requests automatically build preview versions

### GitHub Pages Setup

To enable GitHub Pages for this repository:

1. Go to Settings → Pages
2. Set Source to "GitHub Actions"
3. The site will be available at `https://bastionai.github.io`

## 🎨 Design Features

- **Modern UI**: Clean, professional design with smooth animations
- **Privacy Focus**: Design elements emphasize security and privacy
- **Responsive**: Optimized for desktop, tablet, and mobile devices
- **Fast Loading**: Optimized images and efficient CSS
- **SEO Friendly**: Proper meta tags and structured data

## 📝 Content Management

### Adding New Pages

1. Create a new `.md` file in the root directory
2. Add proper front matter:
   ```yaml
   ---
   layout: page
   title: "Page Title"
   description: "Page description for SEO"
   permalink: /page-url/
   ---
   ```
3. Add the page to navigation in `_config.yml`

### Adding New Products

1. Create a new file in the `products/` directory
2. Update the products overview page
3. Add links from the homepage and navigation

## 🔧 Customization

### Colors and Branding

The site uses a consistent color scheme focused on privacy and security:

- **Primary Blue**: `#667eea` - Trust and reliability
- **Purple Accent**: `#764ba2` - Innovation and creativity
- **Green**: `#059669` - Security and growth
- **Gray Tones**: Various grays for text and backgrounds

### Typography

- **Headings**: System fonts for performance
- **Body Text**: Optimized for readability
- **Code**: Monospace font for technical content

## 🤝 Contributing

We welcome contributions to improve our website:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test locally with `bundle exec jekyll serve`
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/improvement`)
7. Create a Pull Request

### Content Guidelines

- Use clear, concise language
- Maintain focus on privacy and security benefits
- Include technical details where appropriate
- Ensure mobile responsiveness
- Test all links and functionality

## 📊 Analytics and SEO

The site includes:

- **SEO optimization**: Meta tags, structured data
- **Sitemap**: Automatically generated
- **Performance**: Optimized for fast loading
- **Accessibility**: WCAG 2.1 compliance efforts

## 📞 Support

For website-related issues:

- **Technical Issues**: Create an issue in this repository
- **Content Updates**: Submit a pull request
- **General Questions**: Contact us at hello@bastionai.com

## 📄 License

This website content is proprietary to BastionAI. The Jekyll theme and code structure can be used as reference for open-source projects.

## 🔮 Roadmap

Planned improvements:

- [ ] Blog section for AI privacy insights
- [ ] Interactive product demos
- [ ] Documentation portal
- [ ] Community features
- [ ] Multi-language support

---

**BastionAI** - Privacy-First AI Solutions

Visit us at [bastionai.github.io](https://bastionai.github.io)
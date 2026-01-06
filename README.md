# Chicago Application Website

This directory contains a Jekyll-based static website for presenting the University of Chicago application materials.

## Building the Site Locally

### Prerequisites

- Ruby (2.7 or higher)
- Bundler (`gem install bundler`)

### Setup

```bash
cd website
bundle install
```

### Local Development

To build and serve the site locally:

```bash
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`

To build without serving:

```bash
bundle exec jekyll build
```

The built site will be in the `_site/` directory.

## Deployment

### GitHub Pages

This site is configured to work with GitHub Pages. To deploy:

1. Push the `website/` directory to a GitHub repository
2. Enable GitHub Pages in repository settings
3. Set the source to the `website/` directory

Alternatively, you can push just the `website/` directory to a separate repository.

### Manual Deployment

After building with `jekyll build`, the contents of `_site/` can be deployed to any static hosting service:

- Netlify
- Vercel
- AWS S3
- Any web server

## Site Structure

- `index.md` - Homepage with overview and navigation
- `cover_letter.md` - Cover letter content
- `teaching_statement.md` - Teaching statement content
- `syllabi/` - All course syllabi (markdown and PDF)
- `assets/css/custom.css` - Custom styling (Chicago maroon theme)
- `_config.yml` - Jekyll configuration
- `_includes/` - Custom HTML includes
- `_site/` - Built site (generated, not tracked in git)

## Design Features

- **Chicago maroon color scheme** (#800000) with gradients
- **Responsive design** for mobile and desktop
- **Professional typography** with improved readability
- **Interactive syllabi cards** with hover effects
- **PDF download buttons** with gradient styling
- **Section-based navigation** for easy browsing

## Customization

To modify the design, edit:

- `assets/css/custom.css` - All custom styles
- `_config.yml` - Site metadata and configuration
- Individual markdown files for content

## Theme

The site uses the **Minima** Jekyll theme as a base, with extensive customization via `custom.css`.

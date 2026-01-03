# Deployment Guide for GitHub Pages

Follow these steps to publish your application website on GitHub Pages.

## Quick Start (3 steps)

### 1. Create a GitHub Repository

```bash
# From the website folder
cd /Users/utkuturk/chicago_application/website

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: UChicago application materials"

# Create a new repository on GitHub (e.g., uchicago-application)
# Then connect and push:
git remote add origin https://github.com/utkuturk/uchicago-application.git
git branch -M main
git push -u origin main
```

### 2. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Scroll to **Pages** (left sidebar)
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**

### 3. Wait and Visit

- GitHub will build your site (takes 1-2 minutes)
- Your site will be live at: `https://utkuturk.github.io/uchicago-application/`
- You'll see a green checkmark when deployment succeeds

---

## Alternative: Using the Website Folder Only

If you want to keep your main repo private but make the website public:

```bash
# Option A: Subtree push
git subtree push --prefix website origin gh-pages

# Option B: Separate repo for website
cd website
git init
git add .
git commit -m "Application website"
git remote add origin https://github.com/utkuturk/uchicago-application.git
git push -u origin main
```

---

## Customization

### Change Theme

Edit `_config.yml` to use a different GitHub Pages theme:

```yaml
# Options: minima, slate, cayman, midnight, architect, etc.
theme: cayman
```

[Browse themes →](https://pages.github.com/themes/)

### Custom Domain

If you want to use a custom domain (e.g., `uchicago.utkuturk.com`):

1. Add a `CNAME` file to the website folder:
   ```
   uchicago.utkuturk.com
   ```
2. Configure DNS at your domain registrar:
   - Type: CNAME
   - Name: uchicago
   - Value: utkuturk.github.io

### Add Navigation

The `_config.yml` already includes navigation. To customize:

```yaml
header_pages:
  - index.md
  - cover_letter.md
  - teaching_statement.md
```

---

## Local Testing

Before pushing, test locally:

```bash
cd website

# Install dependencies (first time only)
bundle install

# Serve locally
bundle exec jekyll serve

# Visit http://localhost:4000
```

---

## Troubleshooting

### Site not showing up?
- Check Settings → Pages shows "Your site is published"
- Wait 2-3 minutes after pushing
- Hard refresh browser (Cmd+Shift+R)

### Styling looks broken?
- Make sure `_config.yml` has the correct `theme`
- Check that files are in the root of your repo (or configured folder)

### Jekyll build fails?
- Check the Actions tab for error messages
- Ensure all markdown files have proper front matter:
  ```yaml
  ---
  title: Page Title
  ---
  ```

---

## Pro Tips

### Add a Custom Homepage Layout

Create `_layouts/home.html` to customize the landing page:

```html
---
layout: default
---

<div class="home">
  {{ content }}

  <h2>Sample Syllabi</h2>
  <ul>
    {% for syllabus in site.syllabi %}
      <li><a href="{{ syllabus.url }}">{{ syllabus.title }}</a></li>
    {% endfor %}
  </ul>
</div>
```

### Add Front Matter to Each Page

Add to the top of each markdown file:

```yaml
---
title: "Introduction to Psycholinguistics"
layout: page
---
```

### Enable Comments

Add Disqus or Utterances by editing `_config.yml`:

```yaml
disqus:
  shortname: your-disqus-shortname
```

---

## Sharing Your Website

Once live, share the link:

**Direct Link:**
```
https://utkuturk.github.io/uchicago-application/
```

**In Cover Letter:**
> "Complete syllabi and additional materials are available at: https://utkuturk.github.io/uchicago-application/"

**In Email:**
> "Please visit my application website for interactive syllabi and detailed teaching materials: [link]"

---

## Updates and Maintenance

To update the website:

```bash
# Make changes to markdown files
# Then commit and push
git add .
git commit -m "Update: [what you changed]"
git push

# GitHub will automatically rebuild and redeploy
```

---

## Questions?

- GitHub Pages docs: https://docs.github.com/en/pages
- Jekyll docs: https://jekyllrb.com/docs/
- Minima theme: https://github.com/jekyll/minima

Good luck with your application! 🎓

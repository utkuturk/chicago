# University of Chicago Application Materials

This repository contains application materials for Utku Türk's application to the Instructional Faculty position at the University of Chicago.

## 📂 Repository Structure

```
website/
├── index.md                    # Landing page
├── cover_letter.md            # Cover letter
├── teaching_statement.md      # Teaching statement
├── syllabi/                   # Sample course syllabi (7 courses)
│   ├── intro_psycholing.md
│   ├── quant_methods.md
│   ├── intro_ai_language.md
│   ├── advanced_nlp_ai.md
│   ├── linguistic_illusions.md
│   ├── morphology_production.md
│   └── bayesian_modeling.md
└── profile/                   # Professional profiles
    ├── index.md              # Profile navigation guide
    ├── research.md
    ├── teaching.md
    ├── technical.md
    └── narrative.md
```

## 🌐 Viewing the Website

### Option 1: GitHub Pages
1. Push this folder to a GitHub repository
2. Go to Settings → Pages
3. Select source: `main` branch, `/website` folder (or root if you push only website content)
4. Your site will be available at `https://[username].github.io/[repo-name]/`

### Option 2: Local Preview
Install a local markdown viewer or use:
```bash
# Using Python's built-in server
cd website
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Option 3: Jekyll (recommended for GitHub Pages)
For better styling, add a `_config.yml`:
```yaml
title: "Utku Türk - UChicago Application"
theme: minima
```

## 📚 Course Syllabi Overview

### Psycholinguistics (3 courses)
- **Intro to Psycholinguistics**: Apprenticeship model, hands-on experiments
- **Linguistic Illusions**: Debate-focused graduate seminar
- **Morphology in Production**: Studio/maker space model

### Quantitative Methods (2 courses)
- **Quantitative Methods**: Simulation-first approach to statistics
- **Bayesian Cognitive Modeling**: Theory-driven probabilistic modeling

### AI/NLP (2 courses)
- **Machine Learning for Language**: Beginner-friendly, build from scratch
- **Advanced NLP & AI**: Research-level interpretability methods

## 🎓 About the Applicant

**Utku Türk**
PhD Candidate, Linguistics
University of Maryland, College Park

**Research Areas:**
- Sentence production and morphological planning
- Agreement attraction in comprehension
- Computational linguistics and treebanking
- Bayesian statistics and experimental methods

**Contact:**
- Email: utkuturk@umd.edu
- Website: [utkuturk.com](https://utkuturk.com)
- GitHub: [@utkuturk](https://github.com/utkuturk)

## 🔧 Technical Notes

All materials are in Markdown format for easy viewing on GitHub and conversion to HTML for websites. The syllabi maintain consistent structure while each having a unique pedagogical identity.

### File Naming Convention
- Syllabi: `[course_name].md` (descriptive, lowercase with underscores)
- Profiles: `[type].md` (research, teaching, technical, narrative)
- Core docs: `[document_type].md` (cover_letter, teaching_statement)

## 📄 License

These materials are provided for review as part of a job application. Please contact the author for permissions regarding reuse or distribution.

---

*Last updated: January 2026*

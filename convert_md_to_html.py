#!/usr/bin/env python3
"""
Convert markdown files to HTML for the University of Chicago application website.
"""

import re
from pathlib import Path

# HTML template for main pages
MAIN_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Utku Türk</title>
    <link rel="stylesheet" href="{css_path}css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="{base_path}index.html" class="logo">Utku Türk</a>
            <ul class="nav-menu">
                <li><a href="{base_path}index.html">Home</a></li>
                <li><a href="{base_path}cover_letter.html">Cover Letter</a></li>
                <li><a href="{base_path}teaching_statement.html">Teaching Statement</a></li>
                <li class="dropdown">
                    <a href="#" class="dropbtn">Course Packages <span>▾</span></a>
                    <div class="dropdown-content">
                        <a href="{base_path}package1.html">Package 1: Psycholinguistics</a>
                        <a href="{base_path}package2.html">Package 2: AI & NLP</a>
                    </div>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropbtn">Syllabi <span>▾</span></a>
                    <div class="dropdown-content">
                        <a href="{base_path}syllabi/intro_psycholing.html">Intro to Psycholinguistics</a>
                        <a href="{base_path}syllabi/bayesian_modeling.html">Bayesian Cognitive Modeling</a>
                        <a href="{base_path}syllabi/morphology_production.html">Morphology in Production</a>
                        <a href="{base_path}syllabi/intro_ai_language.html">Machine Learning for Language</a>
                        <a href="{base_path}syllabi/advanced_nlp_ai.html">Advanced NLP & AI</a>
                        <a href="{base_path}syllabi/quant_methods.html">Quantitative Methods</a>
                        <a href="{base_path}syllabi/linguistic_illusions.html">Linguistic Illusions</a>
                    </div>
                </li>
            </ul>
        </div>
    </nav>

    <main class="container">
{content}
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h3>Utku Türk</h3>
                    <p>PhD Candidate in Linguistics<br>University of Maryland, College Park</p>
                </div>
                <div>
                    <h3>Connect</h3>
                    <p>
                        <a href="mailto:utkuturk@umd.edu">utkuturk@umd.edu</a><br>
                        <a href="https://utkuturk.com" target="_blank">Personal Website →</a><br>
                        <a href="https://github.com/utkuturk" target="_blank">GitHub</a> |
                        <a href="https://scholar.google.com/citations?hl=tr&user=wa7LG9gAAAAJ" target="_blank">Google Scholar</a>
                    </p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>Application materials for Instructional Professor position in Linguistics and Cognitive Science | University of Chicago</p>
                <p class="copyright">Last updated: January 2026</p>
            </div>
        </div>
    </footer>

    <script src="{base_path}js/main.js"></script>
</body>
</html>"""


def convert_markdown_to_html(md_content):
    """Convert basic markdown to HTML."""
    html = md_content
    
    # Remove YAML frontmatter
    html = re.sub(r'^---\n.*?\n---\n', '', html, flags=re.DOTALL)
    
    # Convert headers
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Convert bold and italic
    html = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Convert links
    html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Convert horizontal rules
    html = re.sub(r'^---$', r'<hr>', html, flags=re.MULTILINE)
    
    # Convert tables
    html = convert_tables(html)
    
    # Convert lists
    html = convert_lists(html)
    
    # Wrap paragraphs
    html = wrap_paragraphs(html)
    
    return html


def convert_tables(html):
    """Convert markdown tables to HTML tables."""
    lines = html.split('\n')
    result = []
    in_table = False
    table_lines = []
    
    for line in lines:
        if '|' in line and not line.strip().startswith('<'):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
        else:
            if in_table:
                result.append(process_table(table_lines))
                in_table = False
                table_lines = []
            result.append(line)
    
    if in_table:
        result.append(process_table(table_lines))
    
    return '\n'.join(result)


def process_table(lines):
    """Process markdown table lines into HTML table."""
    if len(lines) < 2:
        return '\n'.join(lines)
    
    # Skip separator line
    header_line = lines[0]
    data_lines = [l for l in lines[2:] if l.strip()]
    
    html = '<table class="syllabus-table">\n<thead>\n<tr>\n'
    
    # Process header
    headers = [h.strip() for h in header_line.split('|') if h.strip()]
    for header in headers:
        html += f'<th>{header}</th>\n'
    html += '</tr>\n</thead>\n<tbody>\n'
    
    # Process data rows
    for line in data_lines:
        cells = [c.strip() for c in line.split('|') if c.strip()]
        html += '<tr>\n'
        for cell in cells:
            html += f'<td>{cell}</td>\n'
        html += '</tr>\n'
    
    html += '</tbody>\n</table>\n'
    return html


def convert_lists(html):
    """Convert markdown lists to HTML lists."""
    lines = html.split('\n')
    result = []
    in_ul = False
    in_ol = False
    
    for line in lines:
        stripped = line.strip()
        
        # Unordered list
        if stripped.startswith('*   ') or stripped.startswith('- '):
            if not in_ul:
                result.append('<ul>')
                in_ul = True
            content = stripped[4:] if stripped.startswith('*   ') else stripped[2:]
            result.append(f'<li>{content}</li>')
        # Ordered list
        elif re.match(r'^\d+\.\s+', stripped):
            if not in_ol:
                result.append('<ol>')
                in_ol = True
            content = re.sub(r'^\d+\.\s+', '', stripped)
            result.append(f'<li>{content}</li>')
        else:
            if in_ul:
                result.append('</ul>')
                in_ul = False
            if in_ol:
                result.append('</ol>')
                in_ol = False
            result.append(line)
    
    if in_ul:
        result.append('</ul>')
    if in_ol:
        result.append('</ol>')
    
    return '\n'.join(result)


def wrap_paragraphs(html):
    """Wrap text in paragraph tags."""
    lines = html.split('\n')
    result = []
    in_paragraph = False
    paragraph_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # Skip if it's already HTML
        if stripped.startswith('<') or not stripped:
            if in_paragraph:
                result.append('<p>' + ' '.join(paragraph_lines) + '</p>')
                in_paragraph = False
                paragraph_lines = []
            result.append(line)
        else:
            if not in_paragraph:
                in_paragraph = True
                paragraph_lines = []
            paragraph_lines.append(stripped)
    
    if in_paragraph:
        result.append('<p>' + ' '.join(paragraph_lines) + '</p>')
    
    return '\n'.join(result)


def create_section_wrapper(content, add_hero=False, title="", pdf_link=""):
    """Wrap content in section tags."""
    if add_hero:
        hero = f'''        <header class="hero">
            <h1>{title}</h1>
            <p class="subtitle">Utku Türk | University of Chicago Application</p>'''
        if pdf_link:
            hero += f'\n            <a href="{pdf_link}" class="btn btn-download">Download PDF</a>'
        hero += '\n        </header>\n\n'
        return hero + '        <section class="section">\n' + content + '\n        </section>'
    return '        <section class="section">\n' + content + '\n        </section>'


def main():
    base_dir = Path('/Users/utkuturk/chicago_application/website')
    
    # Files to convert
    files_to_convert = [
        ('package1_psycholinguistics.md', 'package1.html', 'Package 1: Psycholinguistics', '', ''),
        ('package2_ai_nlp.md', 'package2.html', 'Package 2: AI & NLP', '', ''),
        ('syllabi/intro_psycholing.md', 'syllabi/intro_psycholing.html', 'Introduction to Psycholinguistics', '../', '../'),
        ('syllabi/bayesian_modeling.md', 'syllabi/bayesian_modeling.html', 'Bayesian Cognitive Modeling', '../', '../'),
        ('syllabi/morphology_production.md', 'syllabi/morphology_production.html', 'Morphology in Production', '../', '../'),
        ('syllabi/intro_ai_language.md', 'syllabi/intro_ai_language.html', 'Machine Learning for Language', '../', '../'),
        ('syllabi/advanced_nlp_ai.md', 'syllabi/advanced_nlp_ai.html', 'Advanced NLP & AI', '../', '../'),
        ('syllabi/quant_methods.md', 'syllabi/quant_methods.html', 'Quantitative Methods', '../', '../'),
        ('syllabi/linguistic_illusions.md', 'syllabi/linguistic_illusions.html', 'Linguistic Illusions', '../', '../'),
    ]
    
    for md_file, html_file, title, base_path, css_path in files_to_convert:
        md_path = base_dir / md_file
        html_path = base_dir / html_file
        
        if not md_path.exists():
            print(f"Skipping {md_file} - file not found")
            continue
        
        print(f"Converting {md_file} -> {html_file}")
        
        # Read markdown
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert to HTML
        html_content = convert_markdown_to_html(md_content)
        
        # Wrap in section
        wrapped_content = create_section_wrapper(html_content)
        
        # Apply template
        final_html = MAIN_TEMPLATE.format(
            title=title,
            content=wrapped_content,
            base_path=base_path,
            css_path=css_path
        )
        
        # Write HTML
        html_path.parent.mkdir(parents=True, exist_ok=True)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"  ✓ Created {html_file}")
    
    print("\nConversion complete!")


if __name__ == '__main__':
    main()

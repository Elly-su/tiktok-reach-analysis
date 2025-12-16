"""
Convert Markdown to PDF using markdown2 and pdfkit
First install: pip install markdown pdfkit
"""

import markdown
import os

# Read the markdown file
with open('FINAL_SUBMISSION_REPORT.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.8;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
        }}
        h1 {{
            color: #333;
            margin-top: 30px;
            margin-bottom: 20px;
        }}
        h2 {{
            color: #444;
            margin-top: 25px;
            margin-bottom: 15px;
        }}
        h3 {{
            color: #555;
            margin-top: 20px;
            margin-bottom: 12px;
        }}
        p {{
            margin-bottom: 15px;
            line-height: 1.8;
        }}
        ul, ol {{
            margin-bottom: 20px;
            line-height: 2.0;
        }}
        li {{
            margin-bottom: 10px;
        }}
        strong {{
            display: block;
            margin-top: 15px;
            margin-bottom: 8px;
        }}
        img {{
            max-width: 100%;
            height: auto;
            margin: 20px 0;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
        }}
        pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 20px 0;
            line-height: 1.6;
        }}
        hr {{
            margin: 30px 0;
            border: 0;
            border-top: 1px solid #ddd;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #f4f4f4;
        }}
    </style>
</head>
<body>
{markdown.markdown(md_content, extensions=['extra', 'codehilite', 'nl2br', 'tables'])}
</body>
</html>
"""

# Save as HTML
with open('FINAL_SUBMISSION_REPORT.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file created: FINAL_SUBMISSION_REPORT.html")
print("\nTo convert to PDF:")
print("1. Open the HTML file in your browser")
print("2. Press Ctrl+P")
print("3. Select 'Save as PDF'")
print("4. Click Save")

import os
import re
import subprocess
import tempfile
import markdown

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap');

  @page {{
    size: A4;
    margin: 16mm 14mm 16mm 14mm;
  }}

  *, *::before, *::after {{
    box-sizing: border-box;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    font-size: 9pt;
    line-height: 1.55;
    margin: 0;
    padding: 0;
  }}

  h1, h2, h3, h4, h5, h6 {{
    color: #0f172a;
    font-weight: 700;
    margin-top: 1.3em;
    margin-bottom: 0.4em;
    page-break-after: avoid;
    break-after: avoid;
  }}

  h1 {{
    font-size: 17pt;
    font-weight: 800;
    line-height: 1.25;
    border-bottom: 2.5px solid #1e40af;
    padding-bottom: 6px;
    margin-top: 0;
    color: #1e3a8a;
  }}

  h2 {{
    font-size: 12.5pt;
    font-weight: 700;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 4px;
    margin-top: 1.4em;
    color: #1e40af;
  }}

  h3 {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #334155;
    margin-top: 1.1em;
  }}

  h4 {{
    font-size: 9.5pt;
    font-weight: 600;
    color: #475569;
  }}

  p {{
    margin-top: 0;
    margin-bottom: 0.7em;
    text-align: justify;
  }}

  a {{
    color: #2563eb;
    text-decoration: none;
    font-weight: 500;
  }}

  blockquote {{
    margin: 0.8em 0;
    padding: 8px 14px;
    background: #f8fafc;
    border-left: 4px solid #3b82f6;
    border-radius: 0 6px 6px 0;
    color: #334155;
    font-size: 8.5pt;
  }}

  blockquote p:last-child {{
    margin-bottom: 0;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 8pt;
    page-break-inside: avoid;
    break-inside: avoid;
    background: #ffffff;
    border-radius: 6px;
    overflow: hidden;
  }}

  th, td {{
    padding: 6px 8px;
    text-align: left;
    border: 1px solid #cbd5e1;
    vertical-align: middle;
  }}

  th {{
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    font-size: 8pt;
    border-bottom: 2px solid #94a3b8;
  }}

  tr:nth-child(even) {{
    background-color: #f8fafc;
  }}

  /* Code Blocks & Inlines */
  code {{
    font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
    font-size: 8pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
  }}

  pre {{
    background-color: #0f172a;
    color: #f8fafc;
    padding: 10px 12px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 7.5pt;
    line-height: 1.4;
    margin: 0.8em 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  pre code {{
    background-color: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: 7.5pt;
  }}

  /* Box Diagram for System Architecture */
  .diagram-box {{
    background: #f8fafc;
    border: 1.5px solid #94a3b8;
    border-radius: 8px;
    padding: 12px;
    margin: 1em 0;
    page-break-inside: avoid;
    break-inside: avoid;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    line-height: 1.4;
    color: #0f172a;
  }}

  /* Math Blocks */
  .math-block {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3px solid #2563eb;
    padding: 6px 12px;
    margin: 0.6em 0;
    border-radius: 4px;
    font-family: 'Plus Jakarta Sans', serif;
    font-style: italic;
    font-size: 8.5pt;
    page-break-inside: avoid;
  }}

  /* Badges & Keyboards */
  kbd {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    padding: 1px 5px;
    border: 1px solid #94a3b8;
    border-bottom-width: 2px;
    border-radius: 4px;
    background: #ffffff;
    color: #1e293b;
    font-weight: 600;
  }}

  /* Alerts styling */
  .alert {{
    padding: 8px 12px;
    border-radius: 6px;
    margin: 0.8em 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  .alert-important {{
    background-color: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 4px solid #3b82f6;
    color: #1e40af;
  }}
  .alert-caution {{
    background-color: #fff1f2;
    border: 1px solid #fecdd3;
    border-left: 4px solid #e11d48;
    color: #9f1239;
  }}
  .alert-tip {{
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
    color: #166534;
  }}

  /* Lists */
  ul, ol {{
    padding-left: 18px;
    margin-top: 0.2em;
    margin-bottom: 0.6em;
  }}

  li {{
    margin-bottom: 0.25em;
  }}

  hr {{
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 1.2em 0;
  }}

  .doc-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 6px;
    margin-bottom: 14px;
    font-size: 7.5pt;
    font-weight: 600;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .doc-footer {{
    margin-top: 24px;
    padding-top: 8px;
    border-top: 1px solid #cbd5e1;
    font-size: 7pt;
    color: #64748b;
    text-align: center;
    font-weight: 500;
  }}
</style>
</head>
<body>
  <div class="doc-header">
    <span>COMPFEST 18 AI Innovation Challenge (AIC) • Universitas Indonesia</span>
    <span>SuratJalan.AI (ResiVision) • BINUS University</span>
  </div>
  {content}
  <div class="doc-footer">
    SuratJalan.AI • Smart Logistics & B2B Proof-of-Delivery Audit • Fasilkom Universitas Indonesia
  </div>
</body>
</html>
"""

def render_math_and_clean(text):
    # Convert GitHub Alert boxes
    text = re.sub(
        r'>\s*\[!IMPORTANT\]\s*\n(>.*(?:\n>.*)*)',
        lambda m: '<div class="alert alert-important">' + markdown.markdown(m.group(1).replace('>', '').strip()) + '</div>',
        text
    )
    text = re.sub(
        r'>\s*\[!CAUTION\]\s*\n(>.*(?:\n>.*)*)',
        lambda m: '<div class="alert alert-caution">' + markdown.markdown(m.group(1).replace('>', '').strip()) + '</div>',
        text
    )
    text = re.sub(
        r'>\s*\[!TIP\]\s*\n(>.*(?:\n>.*)*)',
        lambda m: '<div class="alert alert-tip">' + markdown.markdown(m.group(1).replace('>', '').strip()) + '</div>',
        text
    )

    # Convert LaTeX block formulas $$ ... $$
    def math_block_repl(m):
        raw = m.group(1).strip()
        cleaned = clean_latex_symbols(raw)
        return f'<div class="math-block">{cleaned}</div>'

    text = re.sub(r'\$\$(.*?)\$\$', math_block_repl, text, flags=re.DOTALL)

    # Convert inline LaTeX $ ... $
    def inline_math_repl(m):
        raw = m.group(1).strip()
        cleaned = clean_latex_symbols(raw)
        return f'<i>{cleaned}</i>'

    text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', inline_math_repl, text)

    # Convert Mermaid code blocks to styled ASCII / visual representation
    def mermaid_repl(m):
        raw = m.group(1).strip()
        return f'<div class="diagram-box"><strong>Arsitektur Diagram:</strong><br><pre style="background:transparent;color:#0f172a;padding:0;margin:4px 0;">{raw}</pre></div>'

    text = re.sub(r'```mermaid\s*([\s\S]*?)```', mermaid_repl, text)

    return text

def clean_latex_symbols(s):
    replacements = [
        (r'\\Delta', 'Δ'),
        (r'\\sum_{i=1}\^{N}', '∑ (i=1..N)'),
        (r'\\sum', '∑'),
        (r'\\times', '×'),
        (r'\\rightarrow', '→'),
        (r'\\ge', '≥'),
        (r'\\le', '≤'),
        (r'\\approx', '≈'),
        (r'\\pm', '±'),
        (r'\\circ', '°'),
        (r'\\text\{top\}', 'top'),
        (r'\\text\{left\}', 'left'),
        (r'\\text\{height\}', 'height'),
        (r'\\text\{width\}', 'width'),
        (r'\\text\{Claim\}', 'Claim'),
        (r'\\text\{Total Claim\}', 'Total Claim'),
        (r'\\text\{Total Claim IDR\}', 'Total Claim IDR'),
        (r'\\text\{Price\}', 'Price'),
        (r'\\text\{Received\}', 'Received'),
        (r'\\text\{Ordered\}', 'Ordered'),
        (r'\\text\{received\}', 'received'),
        (r'\\text\{ordered\}', 'ordered'),
        (r'\\text\{unit\}', 'unit'),
        (r'\\text\{s\}', 's'),
        (r'\\text\{C\}', 'C'),
        (r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1 / \2)'),
        (r'\\quad', ' &nbsp; '),
        (r'\\,', ' '),
        (r'\\_', '_'),
        (r'\{', ''),
        (r'\}', ''),
        (r'\\', ''),
    ]
    for pattern, repl in replacements:
        s = re.sub(pattern, repl, s)
    return s

def convert_md_to_pdf(md_path, pdf_path, title="SuratJalan.AI Document"):
    if not os.path.exists(md_path):
        print(f"Error: {md_path} not found.")
        return False

    with open(md_path, "r", encoding="utf-8") as f:
        raw_md = f.read()

    processed_md = render_math_and_clean(raw_md)
    html_body = markdown.markdown(
        processed_md,
        extensions=[
            "tables",
            "fenced_code",
            "toc",
            "nl2br",
            "sane_lists"
        ]
    )

    full_html = HTML_TEMPLATE.format(title=title, content=html_body)

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8") as tmp_html:
        tmp_html.write(full_html)
        tmp_html_path = tmp_html.name

    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path}",
        tmp_html_path
    ]

    print(f"Rendering PDF: {md_path} -> {pdf_path}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    try:
        os.remove(tmp_html_path)
    except Exception:
        pass

    if result.returncode == 0 and os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
        print(f"[SUCCESS] {pdf_path} ({os.path.getsize(pdf_path):,} bytes)")
        return True
    else:
        print(f"[FAILED] Failed to generate PDF: {result.stderr}")
        return False

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    docs_to_convert = [
        (
            os.path.join(base_dir, "docs", "PROPOSAL_LENGKAP_COMPFEST_18.md"),
            os.path.join(base_dir, "docs", "submission", "PROPOSAL_INOVASI.pdf"),
            "SuratJalan.AI - Proposal Inovasi AIC COMPFEST 18"
        ),
        (
            os.path.join(base_dir, "docs", "submission", "VIDEO_PITCH_SCRIPT.md"),
            os.path.join(base_dir, "docs", "submission", "VIDEO_PITCH_SCRIPT.pdf"),
            "SuratJalan.AI - Video Pitch Script & Production Blueprint"
        ),
        (
            os.path.join(base_dir, "docs", "submission", "DELIVERABLES_CHECKLIST.md"),
            os.path.join(base_dir, "docs", "submission", "DELIVERABLES_CHECKLIST.pdf"),
            "SuratJalan.AI - COMPFEST 18 Deliverables Checklist"
        ),
        (
            os.path.join(base_dir, "README.md"),
            os.path.join(base_dir, "docs", "submission", "README_SURATJALAN_AI.pdf"),
            "SuratJalan.AI - Comprehensive Technical Documentation"
        ),
    ]

    for md_file, pdf_file, title in docs_to_convert:
        convert_md_to_pdf(md_file, pdf_file, title)

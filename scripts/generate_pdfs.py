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
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,500;1,600&family=JetBrains+Mono:wght@400;500;600&display=swap');

  @page {{
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
  }}

  *, *::before, *::after {{
    box-sizing: border-box;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    font-size: 8.8pt;
    line-height: 1.55;
    margin: 0;
    padding: 0;
    orphans: 3;
    widows: 3;
  }}

  h1, h2, h3, h4, h5, h6 {{
    color: #0f172a;
    font-weight: 700;
    margin-top: 1.2em;
    margin-bottom: 0.35em;
    page-break-after: avoid;
    break-after: avoid;
  }}

  h1 {{
    font-size: 16pt;
    font-weight: 800;
    line-height: 1.25;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 6px;
    margin-top: 0;
    color: #1e3a8a;
    letter-spacing: -0.01em;
  }}

  h2 {{
    font-size: 12pt;
    font-weight: 700;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 4px;
    margin-top: 1.3em;
    color: #1e40af;
  }}

  h3 {{
    font-size: 10pt;
    font-weight: 700;
    color: #334155;
    margin-top: 1em;
  }}

  h4 {{
    font-size: 9pt;
    font-weight: 600;
    color: #475569;
  }}

  p {{
    margin-top: 0;
    margin-bottom: 0.65em;
    text-align: justify;
  }}

  a {{
    color: #1d4ed8;
    text-decoration: none;
    font-weight: 500;
  }}

  blockquote {{
    margin: 0.7em 0;
    padding: 8px 14px;
    background: #f8fafc;
    border-left: 3.5px solid #2563eb;
    border-radius: 0 6px 6px 0;
    color: #334155;
    font-size: 8.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  blockquote p:last-child {{
    margin-bottom: 0;
  }}

  /* Page Break Utilities */
  .page-break {{
    page-break-before: always;
    break-before: always;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 0.9em 0;
    font-size: 8pt;
    page-break-inside: avoid;
    break-inside: avoid;
    background: #ffffff;
    border-radius: 4px;
    overflow: hidden;
  }}

  th, td {{
    padding: 5.5px 8px;
    text-align: left;
    border: 1px solid #cbd5e1;
    vertical-align: middle;
  }}

  th {{
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    font-size: 8pt;
    border-bottom: 1.5px solid #94a3b8;
  }}

  tr:nth-child(even) {{
    background-color: #f8fafc;
  }}

  /* Code Blocks & Inlines */
  code {{
    font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
    font-size: 7.8pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #e2e8f0;
  }}

  pre {{
    background-color: #0f172a;
    color: #f8fafc;
    padding: 9px 12px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 7.2pt;
    line-height: 1.38;
    margin: 0.7em 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  pre code {{
    background-color: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: 7.2pt;
  }}

  /* Mermaid Graphs & Diagrams */
  .mermaid {{
    text-align: center;
    margin: 14px auto;
    page-break-inside: avoid;
    break-inside: avoid;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px;
  }}

  .mermaid svg {{
    max-width: 100% !important;
    height: auto !important;
  }}

  /* Math Blocks & Formulas */
  .math-block {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3.5px solid #1e40af;
    padding: 8px 14px;
    margin: 0.6em 0;
    border-radius: 4px;
    font-size: 9.2pt;
    color: #0f172a;
    font-weight: 500;
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  .math-block i, p i, li i, td i, span i {{
    font-family: 'Plus Jakarta Sans', -apple-system, serif;
    font-style: italic;
    color: #0f172a;
  }}

  sub, sup {{
    font-size: 75%;
    line-height: 0;
    position: relative;
    vertical-align: baseline;
  }}
  sup {{ top: -0.5em; }}
  sub {{ bottom: -0.25em; }}

  /* Badges & Keyboards */
  kbd {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.2pt;
    padding: 1px 4px;
    border: 1px solid #94a3b8;
    border-bottom-width: 2px;
    border-radius: 3px;
    background: #ffffff;
    color: #1e293b;
    font-weight: 600;
  }}

  /* Alerts styling */
  .alert {{
    padding: 7px 11px;
    border-radius: 5px;
    margin: 0.7em 0;
    font-size: 8.2pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  .alert-important {{
    background-color: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 3.5px solid #2563eb;
    color: #1e40af;
  }}
  .alert-caution {{
    background-color: #fff1f2;
    border: 1px solid #fecdd3;
    border-left: 3.5px solid #e11d48;
    color: #9f1239;
  }}
  .alert-tip {{
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 3.5px solid #16a34a;
    color: #166534;
  }}

  /* Lists & TOC */
  ul, ol {{
    padding-left: 16px;
    margin-top: 0.2em;
    margin-bottom: 0.5em;
  }}

  li {{
    margin-bottom: 0.2em;
  }}

  /* Pretty TOC styling */
  .toc-container {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px 16px;
    margin: 0.8em 0 1.2em 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  .toc-container ul {{
    list-style-type: none;
    padding-left: 0;
  }}
  .toc-container ul li {{
    padding: 2px 0;
    font-weight: 600;
    color: #1e3a8a;
  }}
  .toc-container ul li ul {{
    list-style-type: disc;
    padding-left: 18px;
    margin-top: 2px;
    margin-bottom: 4px;
  }}
  .toc-container ul li ul li {{
    font-weight: 400;
    color: #334155;
  }}

  hr {{
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 1em 0;
  }}

  .doc-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.2px solid #cbd5e1;
    padding-bottom: 5px;
    margin-bottom: 12px;
    font-size: 7.2pt;
    font-weight: 600;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }}

  .doc-footer {{
    margin-top: 20px;
    padding-top: 6px;
    border-top: 1.2px solid #cbd5e1;
    font-size: 6.8pt;
    color: #64748b;
    text-align: center;
    font-weight: 500;
  }}
</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', () => {{
    mermaid.initialize({{ startOnLoad: true, theme: 'neutral', securityLevel: 'loose' }});
  }});
</script>
</head>
<body>
  <div class="doc-header">
    <span>COMPFEST 18 AI Innovation Challenge (AIC) • Universitas Indonesia</span>
    <span>SuratJalan.AI (ResiVision) • BINUS University</span>
  </div>
  {content}
  <div class="doc-footer">
    SuratJalan.AI • Smart Logistics & B2B Proof-of-Delivery Audit • Bina Nusantara University
  </div>
</body>
</html>
"""

def clean_emojis_and_ascii(text):
    # Regex to remove emojis
    emoji_pattern = re.compile(
        "[\U00010000-\U0010ffff\u2600-\u26ff\u2700-\u27bf\u2300-\u23ff\u2b50\u2b06\u2934\u25b6\u25c0\u2b05\u2190-\u21ff]+",
        flags=re.UNICODE
    )
    text = emoji_pattern.sub('', text)

    # Clean any leftover raw box-drawing characters
    box_chars = ['┌', '┐', '└', '┘', '├', '┤', '┬', '┴', '┼', '─', '│', '═', '║', '╔', '╗', '╚', '╝', '╠', '╣', '╦', '╩', '╬']
    for ch in box_chars:
        text = text.replace(ch, '')

    return text

def format_math_latex(raw_str):
    s = raw_str.strip()

    # 1. Clean arrows, circles, and percents in text
    s = re.sub(r'\\rightarrow', '→', s)
    s = re.sub(r'\\circ', '°', s)
    s = re.sub(r'\^°', '°', s)
    s = re.sub(r'\\quad', ' &nbsp;&nbsp;&nbsp;&nbsp; ', s)
    s = re.sub(r'\\,', ' ', s)

    # 2. Coordinates formulas
    s = re.sub(r'\\text\{top\}_\{?\\?%\}?', 'top<sub>%</sub>', s)
    s = re.sub(r'\\text\{left\}_\{?\\?%\}?', 'left<sub>%</sub>', s)
    s = re.sub(r'\\text\{height\}_\{?\\?%\}?', 'height<sub>%</sub>', s)
    s = re.sub(r'\\text\{width\}_\{?\\?%\}?', 'width<sub>%</sub>', s)
    s = re.sub(r'\\%', '%', s)

    # Clean fraction patterns
    s = re.sub(r'\\left\(\s*\\frac\{y_\{?\\min\}?\}\{1000\}\s*\\right\)', '(<i>y</i><sub>min</sub> / 1000)', s)
    s = re.sub(r'\\left\(\s*\\frac\{x_\{?\\min\}?\}\{1000\}\s*\\right\)', '(<i>x</i><sub>min</sub> / 1000)', s)
    s = re.sub(r'\\left\(\s*\\frac\{y_\{?\\max\}?\s*-\s*y_\{?\\min\}?\}\{1000\}\s*\\right\)', '((<i>y</i><sub>max</sub> − <i>y</i><sub>min</sub>) / 1000)', s)
    s = re.sub(r'\\left\(\s*\\frac\{x_\{?\\max\}?\s*-\s*x_\{?\\min\}?\}\{1000\}\s*\\right\)', '((<i>x</i><sub>max</sub> − <i>x</i><sub>min</sub>) / 1000)', s)
    s = re.sub(r'\\frac\{y_\{?\\min\}?\}\{1000\}', '(<i>y</i><sub>min</sub> / 1000)', s)
    s = re.sub(r'\\frac\{x_\{?\\min\}?\}\{1000\}', '(<i>x</i><sub>min</sub> / 1000)', s)
    s = re.sub(r'\\frac\{y_\{?\\max\}?\s*-\s*y_\{?\\min\}?\}\{1000\}', '((<i>y</i><sub>max</sub> − <i>y</i><sub>min</sub>) / 1000)', s)
    s = re.sub(r'\\frac\{x_\{?\\max\}?\s*-\s*x_\{?\\min\}?\}\{1000\}', '((<i>x</i><sub>max</sub> − <i>x</i><sub>min</sub>) / 1000)', s)

    # 3. Discrepancy & Claims
    s = re.sub(r'\\text\{Claim\}_\{?i\}?', 'Claim<sub><i>i</i></sub>', s)
    s = re.sub(r'\\text\{Price\}_\{?\\text\{unit\},\s*i\}?', 'Price<sub>unit, <i>i</i></sub>', s)
    s = re.sub(r'\\text\{Total Claim\s*\(IDR\)\}', 'Total Claim (IDR)', s)
    s = re.sub(r'\\text\{Total Claim\s*IDR\}', 'Total Claim (IDR)', s)
    s = re.sub(r'\\text\{Total Claim\}', 'Total Claim', s)
    s = re.sub(r'\\sum_\{i=1\}\^\{?N\}?', '∑<sub><i>i</i>=1</sub><sup><i>N</i></sup>', s)
    s = re.sub(r'\\sum', '∑', s)
    s = re.sub(r'\\Delta\s*Q_\{?i\}?', 'Δ<i>Q</i><sub><i>i</i></sub>', s)
    s = re.sub(r'\\Delta\s*Q', 'Δ<i>Q</i>', s)
    s = re.sub(r'Q_\{?\\text\{received\},\s*i\}?', '<i>Q</i><sub>received, <i>i</i></sub>', s)
    s = re.sub(r'Q_\{?\\text\{ordered\},\s*i\}?', '<i>Q</i><sub>ordered, <i>i</i></sub>', s)

    # 4. Coordinates array [y_min, x_min, ...]
    s = re.sub(r'y_\{?\\min\}?', '<i>y</i><sub>min</sub>', s)
    s = re.sub(r'x_\{?\\min\}?', '<i>x</i><sub>min</sub>', s)
    s = re.sub(r'y_\{?\\max\}?', '<i>y</i><sub>max</sub>', s)
    s = re.sub(r'x_\{?\\max\}?', '<i>x</i><sub>max</sub>', s)

    # 5. Operators & standard words
    s = re.sub(r'\\times', '×', s)
    s = re.sub(r'\\ge\b', '≥', s)
    s = re.sub(r'\\le\b', '≤', s)
    s = re.sub(r'\\approx', '≈', s)
    s = re.sub(r'\\pm', '±', s)
    s = re.sub(r'\\text\{([^}]+)\}', r'\1', s)
    s = s.replace('{', '').replace('}', '').replace('\\', '')
    s = re.sub(r'(?<=\w)\s*-\s*(?=\w)', ' − ', s)
    s = re.sub(r'\s*-\s*', ' − ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def render_math_and_clean(text):
    text = clean_emojis_and_ascii(text)

    # Clean any timestamps
    text = re.sub(r'2026-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+\-]\d{2}:\d{2}', '', text)

    # Convert Mermaid code blocks to pre.mermaid elements for vector SVG rendering
    def mermaid_repl(m):
        raw = m.group(1).strip()
        return f'<pre class="mermaid">\n{raw}\n</pre>'

    text = re.sub(r'```mermaid\s*([\s\S]*?)```', mermaid_repl, text)

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
        formatted = format_math_latex(raw)
        return f'<div class="math-block">{formatted}</div>'

    text = re.sub(r'\$\$(.*?)\$\$', math_block_repl, text, flags=re.DOTALL)

    # Convert inline LaTeX $ ... $
    def inline_math_repl(m):
        raw = m.group(1).strip()
        formatted = format_math_latex(raw)
        return f'<span>{formatted}</span>'

    text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', inline_math_repl, text)

    # Add chapter page breaks before major BAB headings
    text = re.sub(r'\n(## (?:BAB [I|V|X]+|DAFTAR PUSTAKA|RINGKASAN EKSEKUTIF))', r'\n<div class="page-break"></div>\n\1', text)

    # Wrap Table of Contents in a pretty container
    def toc_repl(m):
        toc_body = markdown.markdown(m.group(1).strip())
        return f'## DAFTAR ISI PROPOSAL\n<div class="toc-container">{toc_body}</div>\n'

    text = re.sub(r'## DAFTAR ISI PROPOSAL\s*([\s\S]*?)(?=\n---\n|\n## )', toc_repl, text)

    return text

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
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=4000",
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

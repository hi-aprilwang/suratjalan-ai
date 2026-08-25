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
    margin: 18mm 14mm 18mm 14mm;
    @bottom-right {{
      content: counter(page) " / " counter(pages);
      font-size: 8pt;
      font-family: 'Plus Jakarta Sans', sans-serif;
      color: #64748b;
    }}
  }}

  *, *::before, *::after {{
    box-sizing: border-box;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    font-size: 9.5pt;
    line-height: 1.55;
    margin: 0;
    padding: 0;
  }}

  h1, h2, h3, h4, h5, h6 {{
    color: #0f172a;
    font-weight: 700;
    margin-top: 1.4em;
    margin-bottom: 0.5em;
    page-break-after: avoid;
    break-after: avoid;
  }}

  h1 {{
    font-size: 19pt;
    font-weight: 800;
    line-height: 1.2;
    border-bottom: 2.5px solid #2563eb;
    padding-bottom: 8px;
    margin-top: 0;
    color: #1e3a8a;
  }}

  h2 {{
    font-size: 13.5pt;
    font-weight: 700;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 5px;
    margin-top: 1.6em;
    color: #1e40af;
  }}

  h3 {{
    font-size: 11pt;
    font-weight: 700;
    color: #334155;
    margin-top: 1.2em;
  }}

  h4 {{
    font-size: 10pt;
    font-weight: 600;
    color: #475569;
  }}

  p {{
    margin-top: 0;
    margin-bottom: 0.8em;
  }}

  a {{
    color: #2563eb;
    text-decoration: none;
    font-weight: 500;
  }}

  blockquote {{
    margin: 1em 0;
    padding: 10px 16px;
    background: #f8fafc;
    border-left: 4px solid #3b82f6;
    border-radius: 0 8px 8px 0;
    color: #334155;
    font-size: 9pt;
  }}

  blockquote p:last-child {{
    margin-bottom: 0;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1.2em 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
    background: #ffffff;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}

  th, td {{
    padding: 7px 10px;
    text-align: left;
    border: 1px solid #cbd5e1;
    vertical-align: top;
  }}

  th {{
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    font-size: 8.5pt;
    border-bottom: 2px solid #94a3b8;
  }}

  tr:nth-child(even) {{
    background-color: #f8fafc;
  }}

  /* Code Blocks & Inlines */
  code {{
    font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 2px 5px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
  }}

  pre {{
    background-color: #0f172a;
    color: #f8fafc;
    padding: 12px 14px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 8pt;
    line-height: 1.45;
    margin: 1em 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  pre code {{
    background-color: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: 8pt;
  }}

  /* Badges & Keyboards */
  kbd {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    padding: 2px 6px;
    border: 1px solid #94a3b8;
    border-bottom-width: 2px;
    border-radius: 4px;
    background: #ffffff;
    color: #1e293b;
    font-weight: 600;
  }}

  /* Alerts styling */
  .alert {{
    padding: 10px 14px;
    border-radius: 8px;
    margin: 1em 0;
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
    padding-left: 20px;
    margin-top: 0.3em;
    margin-bottom: 0.8em;
  }}

  li {{
    margin-bottom: 0.3em;
  }}

  li input[type="checkbox"] {{
    margin-right: 6px;
  }}

  hr {{
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 1.5em 0;
  }}

  /* Header & Footer Branding */
  .doc-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 8px;
    margin-bottom: 16px;
    font-size: 7.5pt;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .doc-footer {{
    margin-top: 30px;
    padding-top: 10px;
    border-top: 1px solid #e2e8f0;
    font-size: 7.5pt;
    color: #94a3b8;
    text-align: center;
  }}
</style>
</head>
<body>
  <div class="doc-header">
    <span>COMPFEST 18 AI Innovation Challenge (AIC) • Universitas Indonesia</span>
    <span>SuratJalan.AI (ResiVision)</span>
  </div>
  {content}
  <div class="doc-footer">
    SuratJalan.AI • Smart Logistics & B2B Supply Chain Automation • Fasilkom UI
  </div>
</body>
</html>
"""

def clean_markdown_for_html(md_text):
    # Convert GitHub Alert boxes
    md_text = re.sub(
        r'>\s*\[!IMPORTANT\]\s*\n(>.*(?:\n>.*)*)',
        lambda m: '<div class="alert alert-important">' + markdown.markdown(m.group(1).replace('>', '').strip()) + '</div>',
        md_text
    )
    md_text = re.sub(
        r'>\s*\[!CAUTION\]\s*\n(>.*(?:\n>.*)*)',
        lambda m: '<div class="alert alert-caution">' + markdown.markdown(m.group(1).replace('>', '').strip()) + '</div>',
        md_text
    )
    md_text = re.sub(
        r'>\s*\[!TIP\]\s*\n(>.*(?:\n>.*)*)',
        lambda m: '<div class="alert alert-tip">' + markdown.markdown(m.group(1).replace('>', '').strip()) + '</div>',
        md_text
    )
    return md_text

def convert_md_to_pdf(md_path, pdf_path, title="SuratJalan.AI Document"):
    if not os.path.exists(md_path):
        print(f"Error: {md_path} not found.")
        return False

    with open(md_path, "r", encoding="utf-8") as f:
        raw_md = f.read()

    processed_md = clean_markdown_for_html(raw_md)
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
            os.path.join(base_dir, "docs", "Proposal_Draft.md"),
            os.path.join(base_dir, "docs", "submission", "PROPOSAL_INOVASI.pdf"),
            "SuratJalan.AI - Proposal Inovasi AIC COMPFEST 18"
        ),
        (
            os.path.join(base_dir, "README.md"),
            os.path.join(base_dir, "docs", "submission", "README_SURATJALAN_AI.pdf"),
            "SuratJalan.AI - Comprehensive Technical Documentation"
        ),
    ]

    for md_file, pdf_file, title in docs_to_convert:
        convert_md_to_pdf(md_file, pdf_file, title)

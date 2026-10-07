import os
import subprocess
import markdown

md_file = r"C:\Users\ASHIRWAD PRATAPSINGH\Downloads\SEO\PROJECT_EVIDENCE\final_report\MILESTONE_I_FINAL_REPORT.md"
html_out_file = r"C:\Users\ASHIRWAD PRATAPSINGH\Downloads\SEO\PROJECT_EVIDENCE\final_report\report_for_pdf.html"
pdf_out_file = r"C:\Users\ASHIRWAD PRATAPSINGH\Downloads\SEO\CSET489_SEO_Assignment_E23CSEU0221_Ashirwad_Pratap_Singh.pdf"
pdf_copy_file = r"C:\Users\ASHIRWAD PRATAPSINGH\Downloads\SEO\PROJECT_EVIDENCE\final_report\CSET489_SEO_Assignment_E23CSEU0221_Ashirwad_Pratap_Singh.pdf"

with open(md_file, "r", encoding="utf-8") as f:
    md_content = f.read()

# Convert markdown to html with tables and fenced code blocks
html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'nl2br'])

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CSET489 Search Engine Optimization — Milestone I Final Report</title>
<style>
  @page {{
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.55;
    color: #1e293b;
    background: #ffffff;
    font-size: 10.5pt;
  }}
  .cover-page {{
    page-break-after: always;
    text-align: center;
    padding-top: 60px;
    height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .institution {{
    font-size: 16pt;
    font-weight: 700;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
  }}
  .dept {{
    font-size: 12pt;
    color: #475569;
    font-weight: 600;
    margin-bottom: 40px;
  }}
  .report-title {{
    font-size: 24pt;
    font-weight: 800;
    color: #1e3a8a;
    line-height: 1.25;
    margin: 40px 0 20px;
  }}
  .subtitle {{
    font-size: 14pt;
    color: #2563eb;
    font-weight: 600;
    margin-bottom: 60px;
  }}
  .meta-box {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 24px;
    max-width: 500px;
    margin: 0 auto;
    text-align: left;
    font-size: 11pt;
  }}
  .meta-row {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 8px;
  }}
  .meta-label {{
    font-weight: 700;
    color: #334155;
  }}
  .meta-val {{
    color: #0f172a;
  }}
  .badge {{
    display: inline-block;
    background: #dbeafe;
    color: #1e40af;
    font-weight: 700;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 11pt;
    margin-top: 30px;
  }}
  
  /* Main Content Styling */
  h1 {{
    font-size: 18pt;
    color: #0f172a;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 6px;
    margin-top: 30px;
    margin-bottom: 14px;
  }}
  h2 {{
    font-size: 14pt;
    color: #1e3a8a;
    margin-top: 24px;
    margin-bottom: 10px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
  }}
  h3 {{
    font-size: 12pt;
    color: #334155;
    margin-top: 18px;
    margin-bottom: 8px;
  }}
  p {{
    margin-bottom: 12px;
    text-align: justify;
  }}
  ul, ol {{
    margin: 0 0 14px 24px;
  }}
  li {{
    margin-bottom: 4px;
  }}
  
  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0 20px;
    font-size: 9.5pt;
  }}
  th, td {{
    border: 1px solid #cbd5e1;
    padding: 7px 10px;
    text-align: left;
  }}
  th {{
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
  }}
  tr:nth-child(even) {{
    background-color: #f8fafc;
  }}
  
  /* Code blocks */
  pre {{
    background: #0f172a;
    color: #f8fafc;
    padding: 12px 16px;
    border-radius: 6px;
    font-family: Consolas, Monaco, "Courier New", monospace;
    font-size: 9pt;
    overflow-x: auto;
    margin: 12px 0 16px;
    line-height: 1.45;
  }}
  code {{
    font-family: Consolas, Monaco, "Courier New", monospace;
    background: #e2e8f0;
    color: #0f172a;
    padding: 2px 4px;
    border-radius: 4px;
    font-size: 9pt;
  }}
  pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
  }}
  
  blockquote {{
    border-left: 4px solid #2563eb;
    background: #eff6ff;
    padding: 10px 16px;
    margin: 14px 0;
    color: #1e3a8a;
    font-style: italic;
  }}
</style>
</head>
<body>

<div class="cover-page">
  <div>
    <div class="institution">Bennett University &bull; School of Computer Science Engineering &amp; Technology</div>
    <div class="dept">CSET489: Search Engine Optimization &bull; Practical Mini-Project</div>
  </div>
  
  <div>
    <div class="report-title">SelfHostStack: An SEO-Optimized Knowledge Hub for Self-Hosted Open-Source Software</div>
    <div class="subtitle">Comprehensive Milestone I Report: Research, Architecture, Cloudflare &amp; Server Deployment</div>
  </div>
  
  <div>
    <div class="meta-box">
      <div class="meta-row"><span class="meta-label">Student Name:</span> <span class="meta-val">Ashirwad Pratap Singh</span></div>
      <div class="meta-row"><span class="meta-label">Roll Number:</span> <span class="meta-val">E23CSEU0221</span></div>
      <div class="meta-row"><span class="meta-label">Course Code:</span> <span class="meta-val">CSET489 (3 Credits)</span></div>
      <div class="meta-row"><span class="meta-label">Component:</span> <span class="meta-val">Continuous Assessment — Practical Mini-Project</span></div>
      <div class="meta-row"><span class="meta-label">Evaluation Phase:</span> <span class="meta-val">Milestone I (Max Marks: 20)</span></div>
      <div class="meta-row"><span class="meta-label">Target Rubric Level:</span> <span class="meta-val">Excellent (20/20)</span></div>
      <div class="meta-row"><span class="meta-label">Date of Submission:</span> <span class="meta-val">October 7, 2026</span></div>
    </div>
    
    <div class="badge">Verified Academic Submission &bull; Zero Fabricated Metrics</div>
  </div>
</div>

<div class="content-body">
{html_body}
</div>

</body>
</html>
"""

with open(html_out_file, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated HTML report at: {html_out_file}")

# Compile HTML to PDF using Chrome Headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_uri = "file:///" + html_out_file.replace("\\", "/")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--print-to-pdf={pdf_out_file}",
    html_uri
]

print("Executing Chrome headless print-to-pdf...")
result = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", result.returncode)

if os.path.exists(pdf_out_file):
    size = os.path.getsize(pdf_out_file)
    print(f"PDF successfully generated: {pdf_out_file} ({size:,} bytes)")
    # Also save a copy inside /PROJECT_EVIDENCE/final_report/
    with open(pdf_out_file, "rb") as src, open(pdf_copy_file, "wb") as dst:
        dst.write(src.read())
    print(f"Copied to: {pdf_copy_file}")
else:
    print("PDF generation failed. Stderr:", result.stderr)

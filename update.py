import re

# Read citations.txt
with open(r"c:\Users\oskar\projects\humanoidlr\citations.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Remove stray page numbers
text = re.sub(r'\n\d+\n', '\n', text)

# Extract citations and remove numbers like [1]
lines = [line.strip() for line in text.split('\n') if line.strip()]
citations = []
current = ""

for line in lines:
    if re.match(r'^\[\d+\]\s*(.*)', line):
        if current:
            citations.append(current)
        current = re.sub(r'^\[\d+\]\s*', '', line)
    else:
        current += " " + line
if current:
    citations.append(current)

# Build HTML block
html_citations = ""
for i, c in enumerate(citations):
    html_citations += f'          <p class="citation" style="margin-bottom: 12px; font-size: 0.9em; line-height: 1.4;">{c}</p>\n'
    
citations_section = f"""
<!-- Citations Section -->
<section class="section">
  <div class="container is-max-desktop">
    <h2 class="title is-3 has-text-centered">References</h2>
    <!-- 400px shows approximately 6-7 citations at a time -->
    <div class="citations-container" style="max-height: 400px; overflow-y: auto; padding: 20px; border: 1px solid #dbdbdb; border-radius: 6px; background-color: #fafafa; text-align: left;">
{html_citations}
    </div>
  </div>
</section>
<!-- End Citations Section -->
"""

# Update index.html
with open(r"c:\Users\oskar\projects\humanoidlr\index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

index_html = index_html.replace('<!-- End video carousel -->', '<!-- End video carousel -->\n\n' + citations_section)

with open(r"c:\Users\oskar\projects\humanoidlr\index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
print("Updated index.html successfully.")

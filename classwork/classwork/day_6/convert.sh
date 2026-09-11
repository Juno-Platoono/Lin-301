# 1) Make a tiny Markdown source
echo "# Hello!" > demo.md
echo "This is a *line* and **text**." >> demo.md

# 2) Convert MD → HTML
pandoc demo.md -o demo.html

# 3) Convert MD → DOCX and → ODT
pandoc demo.md -o demo.docx
pandoc demo.md -o demo.odt
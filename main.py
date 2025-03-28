import os
import PyPDF2
from markdownify import markdownify as md

# Create output directory if not exists
os.makedirs("outputs", exist_ok=True)

def pdf_to_markdown(pdf_path, output_md_path):
    """Converts a PDF file to a Markdown file."""
    text = ""

    # Extract text from PDF
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n\n"

    # Convert text to Markdown
    markdown_text = md(text)

    # Save as .md file
    with open(output_md_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_text)

    print(f"✅ Converted: {pdf_path} → {output_md_path}")

# Process all PDFs in the 'pdfs' folder
pdf_folder = "pdfs"
output_folder = "outputs"

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        md_path = os.path.join(output_folder, filename.replace(".pdf", ".md"))
        pdf_to_markdown(pdf_path, md_path)

print("🎉 All PDFs converted to Markdown!")

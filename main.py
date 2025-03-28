import os
import requests

# Replace with your actual LlamaParse API key
API_KEY = ""

# API endpoint
LLAMA_PARSE_URL = "https://api.llamaindex.ai/v1/parse"

# Ensure the output folder exists
os.makedirs("outputs", exist_ok=True)

def pdf_to_markdown(pdf_path, output_md_path):
    """Converts a PDF file to Markdown using LlamaParse API."""
    
    # Read the PDF file
    with open(pdf_path, "rb") as pdf_file:
        files = {"file": pdf_file}
        headers = {"Authorization": f"Bearer {API_KEY}"}

        # Send request to LlamaParse API
        response = requests.post(LLAMA_PARSE_URL, headers=headers, files=files)

    if response.status_code == 200:
        markdown_text = response.json().get("markdown", "")

        # Save the Markdown file
        with open(output_md_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_text)

        print(f"✅ Converted: {pdf_path} → {output_md_path}")
    else:
        print(f"❌ Failed to convert {pdf_path}. Error: {response.text}")

# Process all PDFs in the 'pdfs' folder
pdf_folder = "pdfs"
output_folder = "outputs"

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        md_path = os.path.join(output_folder, filename.replace(".pdf", ".md"))
        pdf_to_markdown(pdf_path, md_path)

print("🎉 All PDFs converted to Markdown using LlamaParse API!")

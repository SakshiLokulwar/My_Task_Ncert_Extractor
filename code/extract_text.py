import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_txt_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()

    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(full_text)

# Run for Chapter 6
extract_text_from_pdf("pdfs/hesc106.pdf", "raw_text/chapter6_raw.txt")

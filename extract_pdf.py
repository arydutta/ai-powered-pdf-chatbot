from pypdf import PdfReader
def extract_text_from_pdf(pdf_path: str) -> str :
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() 
    return text

content = extract_text_from_pdf("blank_test_pdf.pdf")
print(content[:40])
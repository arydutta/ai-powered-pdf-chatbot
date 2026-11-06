from pypdf import PdfReader
def extract_text_from_pdf(pdf_path: str) -> str :
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or " "
    return text

content = extract_text_from_pdf("sample_test_document.pdf")
#print(content[:40])
target = input("Enter the keyword to search in the pdf : ")
if target.lower() in content.lower():
    print(f"The keyword '{target}' is present in the pdf.")
else:
    print(f"The keyword '{target}' is not present in the pdf.")

def search_pdf(content: str, target: str) -> list[str]:
    results= []
    for line in content.splitlines():
        if target.lower() in line.lower():
            results.append(line)
    return results

matches = search_pdf(content, target)
# for match in matches:
#     print(match)
print(f"Found {len(matches)} matches")
#print(len(matches))

def create_chunk(text: str, chunk_size: int) -> list[str]:
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks

chunks = create_chunk(content, 100)
print(f"Created {len(chunks)} chunks")
for chunk in chunks:
    print(chunk)    

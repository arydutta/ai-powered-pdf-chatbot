from pypdf import PdfReader
from embedding import create_embeddings


# PDF Extraction
def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or " "

    return text


# Keyword Search
def search_pdf(content: str, target: str) -> list[str]:
    results = []

    for line in content.splitlines():
        if target.lower() in line.lower():
            results.append(line)

    return results


# Chunking
def create_chunk(text: str, chunk_size: int) -> list[str]:
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


# MAIN
content = extract_text_from_pdf(
    "2312.10997v5.pdf"
)

target = input(
    "Enter the keyword to search in the pdf: "
)

if target.lower() in content.lower():
    print(f"The keyword '{target}' is present in the pdf.")
else:
    print(f"The keyword '{target}' is not present in the pdf.")


matches = search_pdf(content, target)

print(f"Found {len(matches)} matches")


chunks = create_chunk(content, 500)

print(f"Created {len(chunks)} chunks")


vectors = create_embeddings(chunks)

print("Embedding Shape:", vectors.shape)

print("\nFirst Chunk:")
print(chunks[0])

print("\nFirst Embedding (first 10 values):")
print(vectors[0][:10])
from pdf_reader import extract_text_from_pdf
from keyword_search import search_pdf
from chunking import create_chunks
from embedding import create_embeddings


def main():

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

    print(f"\nFound {len(matches)} matches")

    chunks = create_chunks(content, 500)

    print(f"Created {len(chunks)} chunks")

    vectors = create_embeddings(chunks)

    print("Embedding Shape:", vectors.shape)

    print("\nFirst Chunk:")
    print(chunks[0])

    print("\nFirst Embedding (first 10 values):")
    print(vectors[0][:10])


if __name__ == "__main__":
    main()
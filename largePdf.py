pdfs = [
    {
        "name": "python.pdf",
        "pages": 120,
        "author": "Aryan"
    },
    {
        "name": "ai.pdf",
        "pages": 45,
        "author": "John"
    },
    {
        "name": "chatbot.pdf",
        "pages": 80,
        "author": "Sarah"
    }
]

def is_large_pdf(pages: int) -> bool:
    return pages > 50

for pdf in pdfs:
    if is_large_pdf(pdf["pages"]):
        print(f"{pdf['name']} -> Long Pdf")
    else:
        print(f"{pdf['name']} -> Short Pdf")

print("+++++++++++++++++++++")

# pdf_info = {
#     "name": "chatbot.pdf",
#     "pages": 80,
#     "author": "Aryan"
# }
# print(pdf_info["name"])
# print(pdf_info["pages"])
# print(pdf_info["author"])
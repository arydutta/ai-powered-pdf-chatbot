pdfName: str = "test.pdf"
pdfPageCount: int = 120
pdfFileList: list[str] = ['python.pdf', 'ai.pdf', 'chatbot.pdf']
pdfPagesList : list[int] = [120, 45, 80]
print("Pdf Name is :",pdfName)
print("Number of pages are :",pdfPageCount)
if pdfPageCount > 50 :
    print("Long Pdf")
else :
    print("Short Pdf")

print("+++++++++++++++++++++")
for pdf_file in pdfFileList:
    print(pdf_file)
print("+++++++++++++++++++++")
def classify_pdf(pdfPageCount: int, pdfName: str) :
    if pdfPageCount > 50 :
        print(f"{pdfName} -> Long Pdf")
    else :
        print(f"{pdfName} -> Short Pdf")

for page_count in pdfPagesList:
    classify_pdf(page_count)

print("+++++++++++++++++++++")
def is_large_pdf(page_count: int) -> bool:  
    if page_count > 50:
        return True
    else: 
        return False

print(is_large_pdf(120))
print(is_large_pdf(45))
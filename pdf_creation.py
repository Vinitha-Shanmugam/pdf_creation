# from reportlab.pdfgen import canvas
#
#
# def create_pdf(file_path):
#     # Create a PDF document
#     pdf = canvas.Canvas(file_path)
#
#     # Set the title of the PDF
#     pdf.setTitle("My First PDF")
#
#     # Add content to the PDF
#     pdf.drawString(100, 800, "Hello, this is my first PDF!")
#
#     # Save the PDF to the specified file path
#     pdf.save()
#
#
# if __name__ == "__main__":
#     # Specify the file path for the PDF
#     pdf_file_path = "my_first_pdf.pdf"
#
#     # Create the PDF
#     create_pdf(pdf_file_path)
#
#     print(f"PDF created successfully at: {pdf_file_path}")
from reportlab.lib.pagesizes import A4, A3
# from reportlab.pdfgen import canvas
#
#
# def create_pdf(file_path, page_number):
#     pdf = canvas.Canvas(file_path)
#     pdf.setTitle(f"My PDF - Page {page_number}")
#     pdf.drawString(100, 800, f"Hello, this is page {page_number} of my PDF!")
#     pdf.save()
#
#
# if __name__ == "__main__":
#     for page_num in range(1, 6):
#         pdf_file_path = f"my_pdf_page_{page_num}.pdf"
#         create_pdf(pdf_file_path, page_num)
#         print(f"PDF page {page_num} created successfully at: {pdf_file_path}")

from reportlab.pdfgen import canvas


def create_multi_page_pdf(file_path, num_pages, pagesize):
    pdf = canvas.Canvas(file_path)

    for page_number in range(1, num_pages + 1):
        pdf.setTitle(f"My Multi-Page PDF - Page {page_number}")
        pdf.drawString(100, 800, f"Hello, this is page {page_number} of my multi-page PDF!")

        if page_number < num_pages:
            pdf.showPage()  # Start a new page if not the last page

    pdf.save()


# if __name__ == "__main__":
num_pages = 5
pdf_file_path = "my_multi_page_pdf.pdf"
pagesize=A3
create_multi_page_pdf(pdf_file_path, num_pages,pagesize)

print(f"Multi-page PDF created successfully at: {pdf_file_path}")

# from pdf2image import convert_from_path
# from pytesseract import image_to_string
#
#
# def convert_pdf_to_img(pdf_file):
#     """
#     @desc: this function converts a PDF into Image
#
#     @params:
#         - pdf_file: the file to be converted
#
#     @returns:
#         - an interable containing image format of all the pages of the PDF
#     """
#     return convert_from_path(pdf_file)
#
#
# def convert_image_to_text(file):
#     """
#     @desc: this function extracts text from image
#
#     @params:
#         - file: the image file to extract the content
#
#     @returns:
#         - the textual content of single image
#     """
#     text = image_to_string(file, lang='eng')  # Change 'eng' to the appropriate language code
#     return text
#
#
# def get_text_from_any_pdf(pdf_file):
#     images = convert_pdf_to_img(pdf_file)
#     final_text = ""
#     for pg, img in enumerate(images):
#         final_text += convert_image_to_text(img)
#         # print("Page n°{}".format(pg))
#         # print(convert_image_to_text(img))
#
#     return final_text
#
#
# path_to_pdf = r"C:\Users\Vrdella\Documents\PDF\scanned.pdf"
# print(get_text_from_any_pdf(path_to_pdf))
# import re
#
# from pdfminer.high_level import extract_pages,extract_text
# # for page_layout in extract_pages(r"C:\Users\Vrdella\Documents\PDF\scanned.pdf"):
# #     for element in page_layout:
# #         print(element)
# text=extract_text(r"C:\Users\Vrdella\Downloads\sv600_c_excellent.pdf")
# print(text)
# pattern=re.compile(r"[a-zA]+,{1}\s{1}")
# matches=pattern.findall(text)
# names=[n[:-2] for n in matches]
# print(names)

import fitz
import PIL.Image
import io
import pytesseract


def extract_text_from_image(image_data):
    img = PIL.Image.open(io.BytesIO(image_data))
    text = pytesseract.image_to_string(img)
    return text


pdf_path = r"C:\Users\Vrdella\Downloads\sv600_c_excellent.pdf"
pdf = fitz.open(pdf_path)
counter = 1

for page_num in range(len(pdf)):
    page = pdf[page_num]
    images = page.get_images()

    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img['image']
        extension = base_img['ext']

        # Save the image
        img_path = f"image{counter}.{extension}"
        with open(img_path, "wb") as img_file:
            img_file.write(image_data)

        # Extract text from the image using OCR
        text = extract_text_from_image(image_data)
        print(f"Text extracted from {img_path}:\n{text}")

        counter += 1

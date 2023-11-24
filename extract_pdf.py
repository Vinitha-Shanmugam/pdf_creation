import os
import PyPDF2
import docx
import fitz  # PyMuPDF
import msgpack
import PIL.Image
import io
import pytesseract


def has_images(pdf_path):
    pdf_document = fitz.open(pdf_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        images = page.get_images(full=True)
        if images:
            return True
    return False


def extract_text_from_scanned_pdf(file_path):
    text = ''
    pdf_document = fitz.open(file_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]

        # Extract images from the scanned PDF
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            image = pdf_document.extract_image(img[0])
            image_data = image["image"]

            # Use OCR to extract text from the image
            img_text = pytesseract.image_to_string(PIL.Image.open(io.BytesIO(image_data)))
            text += img_text

    return text


def extract_text_from_editable_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text


def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text


def save_as_msgpack(extracted_texts, output_msgpack_path):
    with open(output_msgpack_path, 'wb') as output_file:
        packed_data = msgpack.packb(extracted_texts)
        output_file.write(packed_data)


def read_msgpack(input_msgpack_path):
    try:
        with open(input_msgpack_path, 'rb') as msgpack_file:
            data = msgpack.unpackb(msgpack_file.read())
        return data
    except FileNotFoundError:
        return {}


def main(file_path):
    # Determine the directory of the input file
    file_directory = os.path.dirname(file_path)

    # Read existing data from MessagePack file in the same directory as the input file
    existing_data = read_msgpack(os.path.join(file_directory, 'output_texts.msgpack'))

    extracted_texts = existing_data.copy()  # Use a copy to avoid modifying the original data

    if file_path.lower().endswith('.pdf'):
        if has_images(file_path):
            text = extract_text_from_scanned_pdf(file_path)
        else:
            text = extract_text_from_editable_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        print("Unsupported file format.")
        return

    # Add new data to the dictionary
    extracted_texts[os.path.basename(file_path)] = text

    # Store the updated extracted texts in MessagePack format in the same directory as the input file
    output_msgpack_path = os.path.join(file_directory, 'output_texts.msgpack')
    save_as_msgpack(extracted_texts, output_msgpack_path)
    print("MessagePack data saved to:", output_msgpack_path)

    # Read MessagePack File
    read_data = read_msgpack(output_msgpack_path)
    print("Read MessagePack data:", read_data)


if __name__ == "__main__":
    file_path = r"C:\Users\Vrdella\Documents\PDF\sv600_c_excellent.pdf"
    main(file_path)


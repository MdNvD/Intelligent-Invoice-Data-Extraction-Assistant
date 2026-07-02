import pytesseract
from pdf2image import convert_from_path

# Path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Poppler path
POPPLER_PATH = r"C:\Users\Mohammed Navith\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"


def extract_text_using_ocr(pdf_path):
    """
    Extract text from scanned/image PDFs using OCR.
    """

    images = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    text = ""

    for image in images:
        text += pytesseract.image_to_string(image)

    return text
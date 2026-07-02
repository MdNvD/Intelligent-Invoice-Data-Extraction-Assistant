import fitz
from ocr_reader import extract_text_using_ocr


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF.
    If no embedded text is found, automatically use OCR.
    """

    text = ""

    try:
        document = fitz.open(pdf_path)

        for page in document:
            text += page.get_text()

        document.close()

        # If PyMuPDF extracted text, return it
        if text.strip():
            print("✓ Text extracted using PyMuPDF.")
            return text

        print("No embedded text found.")
        print("Switching to OCR...")

        text = extract_text_using_ocr(pdf_path)

        print("✓ Text extracted using OCR.")

        return text

    except Exception as e:
        print(f"Error reading PDF: {e}")
        print("Using OCR...")

        return extract_text_using_ocr(pdf_path)
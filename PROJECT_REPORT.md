# Intelligent Invoice Data Extraction Assistant

## Introduction

The Intelligent Invoice Data Extraction Assistant is an AI-powered application developed to automate invoice processing by extracting key information from both **digital** and **scanned PDF invoices**. The application first attempts to extract embedded text using **PyMuPDF**. If no embedded text is found, it automatically switches to **Tesseract OCR** to extract text from scanned invoices. The extracted text is then processed by **Google Gemini AI**, which identifies important invoice fields and exports the structured data into **CSV** and **Excel** formats.

---

## Objectives

- Automate invoice data extraction
- Reduce manual data entry and human errors
- Improve processing speed and accuracy
- Support both digital and scanned PDF invoices
- Export structured invoice information into CSV and Excel
- Demonstrate the integration of AI and OCR technologies

---

## Methodology

1. Select the invoice PDF (Digital or Scanned)
2. Read the PDF using **PyMuPDF**
3. Check whether embedded text is available
4. If embedded text is unavailable, automatically perform OCR using **Tesseract OCR**
5. Send the extracted text to **Google Gemini AI**
6. Receive structured invoice data in JSON format
7. Convert the extracted data into a Pandas DataFrame
8. Export the data into CSV and Excel files

---

## Modules

### PDF Reader Module

Reads digital PDF invoices using **PyMuPDF** and extracts embedded text.

### OCR Module

Automatically detects scanned PDF invoices and extracts text using **Tesseract OCR** with **pdf2image** and **Poppler**.

### AI Extraction Module

Processes the extracted text using **Google Gemini AI** to identify important invoice fields such as Invoice Number, Vendor Name, Invoice Date, Amount, and Reference.

### CSV Export Module

Exports the extracted invoice information into CSV format using **Pandas**.

### Excel Export Module

Exports the extracted invoice information into Excel format using **OpenPyXL** through Pandas.

---

## Advantages

- Supports both digital and scanned PDF invoices
- Automatic OCR fallback for scanned documents
- AI-powered intelligent invoice field extraction
- Reduces manual effort and human errors
- Faster invoice processing
- Easy to maintain due to modular architecture
- Generates both CSV and Excel reports

---

## Limitations

- Requires an internet connection to access Google Gemini API
- Depends on Gemini API availability and quota limits
- OCR accuracy depends on the quality of scanned documents
- Complex or low-quality invoice layouts may slightly reduce extraction accuracy

---

## Conclusion

The Intelligent Invoice Data Extraction Assistant demonstrates an effective combination of **Artificial Intelligence**, **Optical Character Recognition (OCR)**, and **PDF processing** to automate invoice data extraction. By supporting both digital and scanned invoices, the system provides a flexible and intelligent solution that reduces manual work, improves productivity, and exports structured invoice information into CSV and Excel formats for further business processing.
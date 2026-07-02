# 🤖 Intelligent Invoice Data Extraction Assistant

An AI-powered invoice processing system built using **Python**, **Google Gemini AI**, **PyMuPDF**, **Tesseract OCR**, and **Pandas**. The application automatically extracts important invoice details from both **digital** and **scanned PDF invoices** and exports the extracted information into **CSV** and **Excel** files.

---

# 📌 Project Overview

The **Intelligent Invoice Data Extraction Assistant** is a Proof of Concept (POC) developed to automate invoice processing for finance teams. Instead of manually reading invoices and entering data into spreadsheets, the application intelligently extracts important business information using **Google Gemini AI**.

The application first attempts to extract text directly using **PyMuPDF**. If the PDF is a scanned document with no embedded text, it automatically switches to **Tesseract OCR** to extract the text before sending it to Gemini AI for intelligent data extraction.

This project demonstrates the practical use of:

- Artificial Intelligence (AI)
- Natural Language Processing (NLP)
- Optical Character Recognition (OCR)
- PDF Processing
- Business Process Automation
- Python Programming

---

# 🎯 Objective

The objective of this project is to automate invoice data extraction, reduce manual effort, improve accuracy, and increase productivity for finance departments by supporting both digital and scanned invoices.

---

# ❗ Problem Statement

Finance departments receive invoices from multiple vendors in different formats every day. Some invoices are digitally generated while others are scanned copies.

Manually reading these invoices and entering information into spreadsheets is time-consuming and prone to human error.

This project solves the problem by automatically detecting the invoice type, extracting text using either **PyMuPDF** or **Tesseract OCR**, and using **Google Gemini AI** to identify important invoice information.

---

# ✨ Features

- 📄 Read digital PDF invoices
- 📄 Read scanned PDF invoices
- 📑 Extract text using PyMuPDF
- 🔍 Automatic detection of scanned PDFs
- 📝 OCR support using Tesseract OCR
- 🤖 Intelligent invoice field extraction using Google Gemini AI
- 📊 Export extracted data to CSV
- 📈 Export extracted data to Excel
- 🔄 Automatic fallback from PyMuPDF to OCR
- 🗂 Modular project structure
- ⚠ Error handling with retry mechanism
- 🔐 Secure API key management using `.env`

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Programming Language |
| Google Gemini API | AI-based invoice information extraction |
| PyMuPDF | Extract text from digital PDF invoices |
| Tesseract OCR | Extract text from scanned PDF invoices |
| pdf2image | Convert PDF pages into images for OCR |
| Poppler | Render PDF pages for OCR |
| Pandas | Data processing |
| OpenPyXL | Excel file generation |
| Python Dotenv | Environment variable management |
| VS Code | Development Environment |
| Git & GitHub | Version Control |

---

# 🏗 Project Architecture

```text
                  Invoice PDF
            (Digital / Scanned)
                      │
                      ▼
             PDF Reader (PyMuPDF)
                      │
         ┌────────────┴────────────┐
         │                         │
         ▼                         ▼
 Embedded Text Found       No Embedded Text
         │                         │
         ▼                         ▼
  Extract Text         OCR Reader (Tesseract OCR)
         │                         │
         └────────────┬────────────┘
                      ▼
            Extracted Invoice Text
                      │
                      ▼
              Google Gemini AI
                      │
                      ▼
          Structured JSON Response
                      │
                      ▼
             Pandas DataFrame
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
     CSV Export             Excel Export
```

---

# 📁 Project Structure

```text
Intelligent-Invoice-Extractor
│
├── invoices/
│   ├── sample_invoice.pdf
│   └── sample_invoice_for_ocr.pdf
│
├── output/
│
├── ScreenShots/
│
├── src/
│   ├── main.py
│   ├── pdf_reader.py
│   ├── ocr_reader.py
│   ├── gemini_service.py
│   ├── csv_exporter.py
│   └── utils.py
│
├── .env.example
├── .gitignore
├── PROJECT_REPORT.md
├── README.md
└── requirements.txt
```

---

# ⚙ Installation

## 1. Clone the repository

```bash
git clone https://github.com/MdNvD/Intelligent-Invoice-Data-Extraction-Assistant.git
```

## 2. Navigate into the project

```bash
cd Intelligent-Invoice-Data-Extraction-Assistant
```

## 3. Create a virtual environment

```bash
python -m venv venv
```

## 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

## 5. Install required packages

```bash
pip install -r requirements.txt
```

## 6. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶ How to Run

Run the application using:

```bash
python src/main.py
```

The application allows you to choose between:

```
1. Digital PDF (PyMuPDF)
2. Scanned PDF (OCR)
```

---

# 🔄 Workflow

```text
Invoice PDF (Digital / Scanned)
              │
              ▼
Read PDF using PyMuPDF
              │
      ┌───────┴────────┐
      │                │
      ▼                ▼
Text Found        No Text Found
      │                │
      ▼                ▼
 Continue        Run Tesseract OCR
      │                │
      └────────┬────────┘
               ▼
      Extract Invoice Text
               │
               ▼
       Google Gemini AI
               │
               ▼
    Extract Invoice Details
               │
               ▼
      Export CSV & Excel
```

---

# 📊 Extracted Fields

The application extracts the following invoice information:

- Invoice Number
- Vendor Name
- Invoice Date
- Amount
- Reference

---

# 📄 Sample Output

```text
============================================================
Extracted Invoice Details
============================================================

Invoice Number : INV-3517
Vendor Name    : SAHA GOLD (FZE)
Invoice Date   : 30 Apr 2026
Amount          : 1,575.00
Reference       : Audit 2025
```

Generated Files

```text
output/
│
├── invoices.csv
└── invoices.xlsx
```

---

# 📷 Screenshots

### Project Structure

![Project Structure](ScreenShots/Screenshot%202026-07-02%20144913.png)

### Terminal Output

![Terminal Output](ScreenShots/Screenshot%202026-07-02%20144946.png)

### Excel Output

![Excel Output](ScreenShots/Screenshot%202026-07-02%20150832.png)

### OCR Processing

![OCR Processing](ScreenShots/Screenshot%202026-07-02%20150927.png)

---

# 🚀 Future Enhancements

- Batch processing of multiple invoices
- Database integration (MySQL/PostgreSQL)
- Flask/Django Web Application
- Docker containerization
- Cloud deployment (AWS/Azure/GCP)
- OCR accuracy improvement using image preprocessing
- AI-based invoice validation
- Support for JPG, PNG, and other document formats
- Invoice classification using AI
- Email-based invoice processing

---

# ⚠ Note

This application requires a valid **Google Gemini API Key**.

For security reasons, the API key is **not included** in this repository.

Create your own `.env` file using `.env.example` before running the project.

For scanned PDF invoices, **Tesseract OCR** and **Poppler** must also be installed on your system.

---

# 📦 Requirements

```text
google-genai
PyMuPDF
pandas
openpyxl
python-dotenv
pytesseract
pdf2image
Pillow
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 👨‍💻 Author

**Mohammed Navith**

B.Tech Computer Science and Engineering

GitHub: https://github.com/MdNvD

---

# 📜 License

This project was developed as an educational Proof of Concept (POC) to demonstrate the integration of **Artificial Intelligence**, **Optical Character Recognition (OCR)**, **Python**, and **Business Process Automation** for intelligent invoice data extraction.
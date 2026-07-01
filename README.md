# 🤖 Intelligent Invoice Data Extraction Assistant

An AI-powered invoice processing system built using **Python**, **Google Gemini AI**, **PyMuPDF**, and **Pandas**. This application automatically extracts important invoice details from PDF documents and exports the extracted information into **CSV** and **Excel** files.

---

## 📌 Project Overview

The **Intelligent Invoice Data Extraction Assistant** is a Proof of Concept (POC) developed to automate invoice processing for finance teams. Instead of manually reading invoices and entering data into spreadsheets, the application uses **Google Gemini AI** to understand invoice content and extract key business information.

This project demonstrates the practical use of:

- Artificial Intelligence (AI)
- Natural Language Processing (NLP)
- PDF Processing
- Business Process Automation
- Python Programming

---

## 🎯 Objective

The objective of this project is to automate invoice data extraction, reduce manual effort, improve accuracy, and increase productivity for finance departments.

---

## ❗ Problem Statement

Finance departments receive numerous invoices from different vendors every day. Since invoice layouts vary from one vendor to another, manually extracting and entering invoice information into Excel is time-consuming and prone to human error.

This project solves the problem by using **Google Gemini AI** to intelligently identify and extract important invoice fields.

---

## ✨ Features

- 📄 Read invoice PDF files
- 📑 Extract text using PyMuPDF
- 🤖 Intelligent invoice field extraction using Google Gemini AI
- 📊 Export extracted data to CSV
- 📈 Export extracted data to Excel
- 🗂 Modular project structure
- ⚠ Error handling and validation
- 🔐 Secure API key management using `.env`

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Programming Language |
| Google Gemini API | AI-based invoice data extraction |
| PyMuPDF | PDF text extraction |
| Pandas | Data processing |
| OpenPyXL | Excel file generation |
| Python Dotenv | Environment variable management |
| VS Code | Development Environment |
| Git & GitHub | Version Control |

---

## 🏗 Project Architecture

```text
                 Invoice PDF
                      │
                      ▼
           PDF Reader (PyMuPDF)
                      │
                      ▼
            Extract Invoice Text
                      │
                      ▼
             Google Gemini AI
                      │
                      ▼
          Structured JSON Response
                      │
                      ▼
             CSV / Excel Export
```

---

## 📁 Project Structure

```text
Intelligent-Invoice-Extractor
│
├── invoices/
│   └── sample_invoice.pdf
│
├── output/
│
├── ScreenShots/
│
├── src/
│   ├── main.py
│   ├── pdf_reader.py
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

## ⚙ Installation

### 1. Clone the repository

```bash
git clone https://github.com/MdNvD/Intelligent-Invoice-Data-Extraction-Assistant.git
```

### 2. Navigate into the project

```bash
cd Intelligent-Invoice-Data-Extraction-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

### 5. Install required packages

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

Create a file named `.env` in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶ How to Run

Run the application using:

```bash
python src/main.py
```

---

## 🔄 Workflow

```text
Invoice PDF
      │
      ▼
Read PDF
      │
      ▼
Extract Text
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

## 📊 Extracted Fields

The application extracts the following information:

- Invoice Number
- Vendor Name
- Invoice Date
- Amount
- Reference

---

## 📄 Sample Output

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

```
output/
│
├── invoices.csv
└── invoices.xlsx
```

---

## 📷 Screenshots

### Project Structure

Add your VS Code project screenshot here.

```
ScreenShots/
```

### Terminal Output

Add your terminal execution screenshot here.

### Excel Output

Add your generated Excel output screenshot here.

---

## 🚀 Future Enhancements

- Batch processing of multiple invoices
- OCR support for scanned PDF invoices
- Database integration (MySQL/PostgreSQL)
- Flask/Django Web Application
- Docker containerization
- Cloud deployment
- AI validation of extracted invoice fields
- Support for additional invoice formats

---

## ⚠ Note

This application requires a valid **Google Gemini API Key**.

For security reasons, the API key is **not included** in this repository.

Create your own `.env` file using `.env.example` before running the project.

---

## 📦 Requirements

```
google-genai
PyMuPDF
pandas
openpyxl
python-dotenv
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Mohammed Navith**

B.Tech Computer Science and Engineering

GitHub: https://github.com/MdNvD

---

## 📜 License

This project was developed as an educational Proof of Concept (POC) for learning Artificial Intelligence, Python, and Business Process Automation.

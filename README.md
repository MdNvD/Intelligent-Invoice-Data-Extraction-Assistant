# Intelligent Invoice Data Extraction Assistant

## Project Overview

The Intelligent Invoice Data Extraction Assistant is an AI-powered automation tool developed using Python and Google Gemini AI. The application reads invoice PDF documents, extracts important business information using Artificial Intelligence, and automatically exports the extracted data into CSV and Excel files.

This project demonstrates the use of AI, Natural Language Processing (NLP), PDF processing, and business automation.

---

## Objective

The objective of this project is to automate invoice data extraction and reduce manual data entry performed by finance teams.

---

## Problem Statement

Finance departments receive hundreds of invoices every day. Manually entering invoice details into Excel is time-consuming and prone to human error.

This application automates the process by extracting important invoice information using AI.

---

## Features

- Read invoice PDFs
- Extract invoice text using PyMuPDF
- Use Google Gemini AI for intelligent data extraction
- Export extracted data to CSV
- Export extracted data to Excel
- Modular Python project structure
- Error handling

---

## Technologies Used

- Python 3.13
- Google Gemini API
- PyMuPDF
- Pandas
- OpenPyXL
- Python Dotenv
- VS Code

---
## Architecture Diagram


                +----------------------+
                |   Invoice PDF        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | PDF Reader (PyMuPDF) |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Extract Invoice Text |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Gemini AI API      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | JSON Invoice Fields  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | CSV / Excel Export   |
                +----------------------+

---                

## Folder Structure

```
Intelligent-Invoice-Extractor

│
├── invoices
├── output
├── src
│
├── main.py
├── pdf_reader.py
├── gemini_service.py
├── csv_exporter.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## Workflow

Invoice PDF

↓

Read PDF

↓

Extract Text

↓

Gemini AI

↓

JSON Response

↓

CSV / Excel

---

## Output

The application extracts:

- Invoice Number
- Vendor Name
- Invoice Date
- Amount
- Reference

and saves the information in:

- invoices.csv
- invoices.xlsx

---

## Future Enhancements

- Support multiple invoices
- OCR for scanned invoices
- Database integration
- Web application using Flask
- Cloud deployment

---

## Author

Mohammed Navith
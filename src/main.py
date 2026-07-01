import os
from dotenv import load_dotenv
from google import genai

from pdf_reader import extract_text_from_pdf
from gemini_service import extract_invoice_data
from csv_exporter import save_invoice


def main():
    """
    Intelligent Invoice Data Extraction Assistant
    """

    # Load environment variables
    load_dotenv()

    # Read Gemini API Key
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API Key not found. Please check your .env file.")

    # Initialize Gemini Client
    client = genai.Client(api_key=api_key)

    # Invoice PDF Path
    pdf_path = "invoices/sample_invoice.pdf"

    # Check if PDF exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Invoice not found: {pdf_path}")

    print("=" * 70)
    print("      Intelligent Invoice Data Extraction Assistant")
    print("=" * 70)

    # Step 1
    print("\n[1/4] Reading PDF...")
    invoice_text = extract_text_from_pdf(pdf_path)
    print("✓ PDF text extracted successfully.")

    # Step 2
    print("\n[2/4] Sending invoice to Gemini AI...")
    invoice_data = extract_invoice_data(client, invoice_text)
    print("✓ Invoice data extracted successfully.")

    # Step 3
    print("\n" + "=" * 70)
    print("Extracted Invoice Details")
    print("=" * 70)

    print(f"{'Invoice Number':20}: {invoice_data['invoice_number']}")
    print(f"{'Vendor Name':20}: {invoice_data['vendor_name']}")
    print(f"{'Invoice Date':20}: {invoice_data['invoice_date']}")
    print(f"{'Amount':20}: {invoice_data['amount']}")
    print(f"{'Reference':20}: {invoice_data['reference']}")

    # Step 4
    print("\n[3/4] Saving CSV and Excel...")
    save_invoice(invoice_data)
    print("✓ Files saved successfully.")

    print("\n" + "=" * 70)
    print("Project Completed Successfully")
    print("=" * 70)


if __name__ == "__main__":
    main()
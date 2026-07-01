import pandas as pd
import os
from datetime import datetime


def save_invoice(invoice_data):
    """
    Save extracted invoice data into CSV and Excel.
    """

    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Convert dictionary into DataFrame
    df = pd.DataFrame([invoice_data])

    # Rename columns
    df = df.rename(columns={
        "invoice_number": "Invoice Number",
        "vendor_name": "Vendor Name",
        "invoice_date": "Invoice Date",
        "amount": "Amount",
        "reference": "Reference"
    })

    # Create timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Output file names
    csv_file = f"output/invoices_{timestamp}.csv"
    excel_file = f"output/invoices_{timestamp}.xlsx"

    # Save files
    df.to_csv(csv_file, index=False)
    df.to_excel(excel_file, index=False)

    print(f"\nCSV saved successfully : {csv_file}")
    print(f"Excel saved successfully : {excel_file}")
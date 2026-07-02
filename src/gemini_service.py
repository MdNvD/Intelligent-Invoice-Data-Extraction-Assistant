import json
import time

MODEL_NAME = "gemini-2.5-flash"


def extract_invoice_data(client, invoice_text):

    prompt = f"""
You are an Intelligent Invoice Data Extraction Assistant.

Extract the following fields:

1. Invoice Number
2. Vendor Name
3. Invoice Date
4. Amount
5. Reference

Return ONLY valid JSON.

Do NOT return markdown.
Do NOT return explanations.

Return exactly like this:

{{
    "invoice_number":"",
    "vendor_name":"",
    "invoice_date":"",
    "amount":"",
    "reference":""
}}

Invoice Text:

{invoice_text}
"""

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            result = response.text.strip()

            if result.startswith("```json"):
                result = result.replace("```json", "").replace("```", "").strip()

            elif result.startswith("```"):
                result = result.replace("```", "").strip()

            return json.loads(result)

        except Exception as e:

            print(f"\nAttempt {attempt + 1} failed.")
            print(e)

            time.sleep(5)

    raise Exception("Gemini failed after 3 attempts.")
import pdfplumber
import re
import pandas as pd
import os
import pytesseract
from pdf2image import convert_from_path


# --- CONFIGURATIONS ---
STATEMENTS_FOLDER = "statements"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\Users\rugve\Downloads\Release-25.07.0-0\poppler-25.07.0\Library\bin"

# --- REGEX PATTERNS ---
PATTERNS = {
    "Name": r"Name\s*[:\-]?\s*([A-Z\s]+)",
    "Email": r"Email\s*[:\-]?\s*([\w\.\-]+@[\w\.\-]+)",
    "Address": r"Address\s*[:\-]?\s*(.+)",
    "Statement Date": r"Statement\s*Date\s*[:\-]?\s*([\d/]+)",
    "Card Last 4 Digits": r"(?:Card No|XXXX)\D*(\d{4})",
    "Payment Due Date": r"Payment\s*Due\s*Date\s*[:\-]?\s*([\d/]+)",
    "Total Dues": r"Total\s*Amount\s*Due\s*[:\-]?\s*(₹?\s?[\d,]+\.\d{2})",
    "Minimum Amount Due": r"Minimum\s*Amount\s*Due\s*[:\-]?\s*(₹?\s?[\d,]+\.\d{2})",
    "Credit Limit": r"Credit\s*Limit\s*[:\-]?\s*([\d,]+)",
    "Available Credit Limit": r"Available\s*Credit\s*Limit\s*[:\-]?\s*([\d,]+)"
}

# --- FUNCTION 1: Direct text extraction ---
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# --- FUNCTION 2: OCR extraction ---
def ocr_extract_text(pdf_path):
    print(f"🟡 Using OCR for {os.path.basename(pdf_path)} (scanned image detected)")
    text = ""
    pages = convert_from_path(pdf_path, dpi=200, poppler_path=POPPLER_PATH)
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text

# --- FUNCTION 3: Apply regex patterns ---
def extract_fields(text):
    data = {}
    for field, pattern in PATTERNS.items():
        match = re.search(pattern, text, re.IGNORECASE)
        data[field] = match.group(1).strip() if match else None
    return data


def ocr_extract_text(pdf_path):
    print(f"🟡 Using OCR for {os.path.basename(pdf_path)} (scanned image detected)")
    text = ""
    pages = convert_from_path(pdf_path, dpi=200, poppler_path=POPPLER_PATH)
    for page in pages:
        text += pytesseract.image_to_string(page)

    return text


# --- MAIN ---
def main():
    results = []

    for filename in os.listdir(STATEMENTS_FOLDER):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(STATEMENTS_FOLDER, filename)
            print(f"📄 Processing: {filename}")

            # Try direct text extraction first
            text = extract_text_from_pdf(pdf_path)

            # If no text found, use OCR
            if not text.strip():
                text = ocr_extract_text(pdf_path)

            fields = extract_fields(text)
            fields["File Name"] = filename
            results.append(fields)

    # Save results
    df = pd.DataFrame(results)
    df.to_csv("parsed_credit_statements.csv", index=False)
    print("\n✅ Extraction complete! Saved to 'parsed_credit_statements.csv'")


if __name__ == "__main__":
    main()

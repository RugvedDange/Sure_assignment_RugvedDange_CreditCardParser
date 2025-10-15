# Sure_assignment_RugvedDange_CreditCardParser
Automated Credit Card Statement Parser | Extracts key financial details (due dates, credit limits, dues) from text or scanned PDFs using OCR &amp; Regex | Saves results as structured CSV for analysis | Visualizes the result in an attractive cardformat

Credit Card Statement Extractor

An intelligent Python-based tool that extracts and visualizes credit card statement details from both text-based and scanned PDFs.
It uses OCR (Tesseract) and Regex-based parsing to retrieve important financial information like cardholder details, total dues, and credit limits — and displays them in a modern card-style visualization.

 Features

 Extracts data from multiple banks (HDFC, ICICI, SBI, Axis, etc.)
 Works for both text-based and scanned PDFs
 Automatically detects whether to use OCR
 Extracts key fields like:

Cardholder Name

Card Number (Last 4 digits)

Statement Date & Payment Due Date

Total Amount Due & Minimum Due

Credit Limit & Available Credit Limit

 Saves everything in a clean CSV file
 Visualizes results in a credit card–style dashboard

 Technologies Used

 Python 3.13

 pdfplumber – extract text from PDFs

 pytesseract (OCR) + pdf2image – extract from scanned statements

 re (regex) – identify text patterns dynamically

 pandas – organize and export extracted data

 React / Web UI or Dash – visualize extracted credit card data in card-style view

✅ Output:

A CSV file — parsed_credit_statements.csv

A terminal summary like:

 Extracted Credit Statement Summary
---------------------------------------------
 Bank: HDFC
 Name: Akash Kundu
 Card Ending: 3388
 Total Due: ₹83,794
 Due Date: 12/11/2024
 Credit Limit: ₹90,000
 Available Credit: ₹6,206
---------------------------------------------

 Visualization (Card-Style View)

Once extraction is complete, the data is visualized in a credit card–like layout showing all key financial details for each statement.



 Features of the Visualization:

Displays all extracted fields as a virtual credit card

Auto-detects CSV fields — no manual mapping required

Responsive layout with modern black & white design

Clean typography and highlight of total dues

Each record (row) from the CSV is represented as an interactive credit card with:

Cardholder name

Bank name / File name

Last 4 digits

Email & Address

Statement & Due Date

Credit limits and dues
-----------------------------------------------------------------------------------

Future Enhancements

Multi-month tracking of due payments

Export visual cards to PDF or HTML reports

Integration with Power BI / Tableau

Dashboard with trend analysis of credit utilization

----------------------------------------------------------------------------------
Author

Rugved Ravindra Dange
B.Tech – Computer Engineering
Shah & Anchor Kutchhi Engineering College (SAKEC)

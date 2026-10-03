AI Data Automation System

An AI-powered Python automation project that reads student data from a CSV file, processes the data, sends it to Gemini for analysis, and automatically generates an AI report.

Features
Read student data from CSV
Process student marks using Python
Automatically create an AI prompt
Analyze data using Gemini API
Generate an AI report
Save the report as a text file
Protect API keys using .env
Handle API errors using try/except
Project Flow

CSV File → Python → Process Data → Gemini API → AI Analysis → AI Report

Project Structure
Day 6/
├── main.py
├── students.csv
├── AI_Report.txt
├── requirements.txt
├── .env
└── .gitignore
Installation

Install the required packages:

pip install -r requirements.txt
Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here

Never upload .env to GitHub.

How to Run

Run:

python main.py

The program reads students.csv, sends the student data to Gemini, and creates:

AI_Report.txt
Example Input
name,marks
Ali,85
Ahmed,72
Sara,91
Asim,45
Example Output

The AI generates a report containing:

Average marks
Highest marks
Lowest marks
Number of students who passed
Number of students who failed
Overall summary
Technologies Used
Python
CSV
Gemini API
Google GenAI SDK
python-dotenv
Git
GitHub
Author

Syed Asim
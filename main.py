import csv
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()


# Read CSV
students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({
            "name": row["name"],
            "marks": int(row["marks"])
        })


# Create student text
student_text = ""

for student in students:
    student_text += f"{student['name']}: {student['marks']} marks\n"


# Create Gemini prompt
prompt = f"""
Analyze these student results:

{student_text}

Give me:
1. Average marks
2. Highest marks
3. Lowest marks
4. Number of students who passed
5. Number of students who failed
6. A short overall summary
"""


# Send prompt to Gemini
try:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    ai_report = interaction.output_text

except Exception as e:
    print("Something went wrong while contacting Gemini.")
    print("Error:", e)
    exit()


# Save AI report
with open("AI_Report.txt", "w") as file:
    file.write(ai_report)

print("AI report generated successfully!")
print("\n===== AI REPORT =====")
print(ai_report)
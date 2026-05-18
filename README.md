# 🤖 AI Interview Agent

## 📌 Overview

AI Interview Agent is an AI-powered technical interview simulator developed using Python, Streamlit, SQLite, and Gemini AI API. The application dynamically generates technical interview questions based on candidate skills and job roles, evaluates candidate responses using AI, provides feedback with scoring, and stores interview history in a SQL database.

This project demonstrates the practical implementation of Generative AI, API integration, database management, and web application development in a real-world interview automation system.

---

# 🚀 Features

- AI-generated technical interview questions
- Dynamic question generation based on skills and job role
- AI-powered answer evaluation system
- Automated scoring and feedback generation
- SQLite database integration
- Candidate interview history tracking
- Interactive Streamlit web interface
- Real-time interview simulation

---

# 🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- Gemini AI API
- Pandas

---

# 🧠 How the System Works

1. Candidate enters:
   - Name
   - Job Role
   - Technical Skills

2. AI generates a technical interview question based on the provided skills.

3. Candidate submits an answer.

4. AI evaluates the response and generates:
   - Score
   - Feedback
   - Suggestions for improvement

5. Interview data is stored in SQLite database for tracking and analysis.

---

# 📂 Project Structure

```bash
AI_Interview_Agent/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
|__ .gitignore

# Prescription Follow-up System

## Overview
This project is a **Prescription Follow-up System** that allows doctors to add patient prescriptions and automatically sends **AI-generated follow-up emails** to patients after a specified period. The system uses **Python, PostgreSQL, and Google Gemini AI** for email content generation, ensuring personalized, professional, and empathetic communication.

---

## Features

- Add patient prescriptions with:
  - Name
  - Email
  - Diagnosed disease
  - Prescribed medicine(s)
  - Duration (in days)
- AI-generated follow-up emails personalized for each patient.
- Automatic email delivery after a specified time (e.g., 7 days; 5 seconds for testing).
- Track follow-up status in the database.
- Modular architecture separating:
  - Prescription addition
  - AI email generation
  - Email sending
- Easily extensible for cloud deployment and scheduling.

---

## Tech Stack

- **Backend:** Python 3.x
- **Database:** PostgreSQL (via SQLAlchemy)
- **Email:** Gmail SMTP (or configurable for other mail providers)
- **AI:** Google Gemini (Generative AI) for dynamic email generation
- **Environment:** Python virtual environment (`venv`)
- **Other Libraries:** `dotenv`, `threading`, `smtplib`, `datetime`

---

## Project Structure

prescription_followup/
│
├─ main.py # Main script to add prescriptions
├─ add_prescription.py # Script to add patient prescriptions
├─ send_followups.py # Script to send AI follow-up emails
├─ database.py # SQLAlchemy database setup
├─ email_utils.py # Email sending utilities
├─ ai_agent.py # AI email generator using Google Gemini
├─ .env # Environment variables (API keys, email credentials)
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation


---

## Setup Instructions

### 1. Clone the repository
```bash
git clone [<repository_url>](https://github.com/AyushiSoni2003/prescription_followup.git)
cd prescription_followup


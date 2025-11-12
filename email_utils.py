import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_followup_email(to_email, body , patient_name):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    subject = f"Follow-up on your health, {patient_name}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls() # Secure the connection
            server.login(sender, password)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_followup_email("ayushisoni31103@gmail.com", "Himanshi")



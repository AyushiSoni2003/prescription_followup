import time
from database import SessionLocal, Prescription
from email_utils import send_followup_email
from datetime import datetime ,UTC
from ai_agent import generate_followup_email
import threading
from twilio_utils import make_followup_call

def schedule_followup(prescription_id, delay):
    """Wait for 'delay' seconds then send follow-up email."""
    time.sleep(delay)
    db = SessionLocal()
    prescription = db.query(Prescription).filter(Prescription.id == prescription_id).first()
    if prescription and not prescription.followup_sent:
        # Generate email content using AI agent
        emai_body = generate_followup_email(
            patient_name=prescription.patient_name,
            disease=prescription.disease,
            medicine=prescription.prescription,
            days=prescription.days
        )
        # Send the email
        send_followup_email(to_email = prescription.patient_email, body = emai_body , patient_name = prescription.patient_name)
        prescription.followup_sent = True
        db.commit()
        print(f"Follow-up sent for patient: {prescription.patient_name}")
    db.close()

def schedule_followup_call(patient_phone,patient_name, delay, disease, medicine, days):
    # Wait for 'delay' seconds then make follow-up call
    time.sleep(delay)
    make_followup_call(patient_phone,patient_name,disease,medicine,days)


def add_prescription(patient_name, patient_email, disease, prescription_text, days, patient_phone):
    db = SessionLocal()

    # patient_name = input("Enter patient name: ")
    # patient_email = input("Enter patient email: ")
    # disease = input("Enter diagnosed disease: ")
    # prescription_text = input("Enter prescribed medicine(s): ")
    # days = int(input("Enter duration (in days): "))
    # patient_phone = input("Enter patient phone number (with country code): ")

    new_prescription = Prescription(
        patient_name=patient_name,
        patient_email=patient_email,
        disease=disease,
        prescription=prescription_text,
        days=days,
        created_at=datetime.now(UTC),
        patient_phone=patient_phone
    )

    db.add(new_prescription)
    db.commit()
    db.refresh(new_prescription)
    print(f"Prescription added for {patient_name}")

    # Schedule follow-up (5 sec for testing)
    threading.Thread(target=schedule_followup, args=(new_prescription.id, 3)).start()
    threading.Thread(
    target=schedule_followup_call,
    args=(
        new_prescription.patient_phone,
        new_prescription.patient_name,
        3,  # delay in seconds
        new_prescription.disease,
        new_prescription.prescription,
        new_prescription.days
    )
).start()
    db.close()


if __name__ == "__main__":
    add_prescription()

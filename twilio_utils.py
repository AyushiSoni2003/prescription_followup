from twilio.rest import Client
from dotenv import load_dotenv
import os
from ai_agent import generate_followup_call_script

load_dotenv()

def make_followup_call(patient_phone, patient_name , disease, medicine, days):
    """Makes an automated voice call to remind the patient about their follow-up."""
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_number = os.getenv("TWILIO_PHONE_NUMBER")

        client = Client(account_sid, auth_token)

        message_text =generate_followup_call_script(patient_name,disease,medicine,days)
        call = client.calls.create(
            twiml=f'<Response><Say language="hi-IN" voice="Google.hi-IN-Wavenet-A">{message_text}</Say></Response>',
            to=patient_phone,
            from_=from_number
        )

        print(f"Follow-up call initiated! Call SID: {call.sid}")

    except Exception as e:
        print(f"Error making follow-up call: {e}")

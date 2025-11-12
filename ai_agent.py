import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_followup_email(patient_name, disease, medicine , days):
    try:
        prompt = f"""
        You are a friendly yet professional medical assistant.
        Write a follow-up email for a patient named {patient_name}.

        The patient was diagnosed with {disease} and was prescribed {medicine} for {days} days.

        The email should include the body part only and cover the following points:
        1. A warm greeting to {patient_name}.
        2. A Question to ask if they took prescribed medicine regularly.
        3. Ask if they are feeling better or have any side effects.
        4. Encourage them to book a follow-up appointment if symptoms persist.
        5. Sign off simply as the 'doctor's assistant', politely and professionally.

        The tone should be:
        - Empathetic and caring
        - Professional and concise
        - Easy to read
        - Avoid medical jargon
        - Suitable to send as an actual email message

        Do not include markdown or formatting. Just plain text.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Error generating follow-up email."
    
if __name__ == "__main__":
     print(generate_followup_email("Himanshi", "fever", "paracetamol", 7))
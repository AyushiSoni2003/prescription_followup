import os
from google import genai
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

client = genai.Client(api_key=GOOGLE_API_KEY)

def translate_to_hindi(text):
    """Translate English text to Hindi using deep-translator."""
    try:
        translated = GoogleTranslator(source='en', target='hi').translate(text)
        return translated
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # fallback to original English

    
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
    
def generate_followup_call_script(patient_name, disease, medicine, days):
    try:
        prompt = f"""
        You are a helpful AI medical assistant.
        Write a short voice call script (under 50 words) for a follow-up reminder.

        Patient name: {patient_name}
        Diagnosed with: {disease}
        Prescribed medicine: {medicine}
        Treatment duration: {days} days.

        The message should sound natural when spoken by a human or AI voice:
        - Use a conversational tone
        - Be polite and empathetic
        - Mention the patient's name
        - Encourage them to take medicines and consult doctor if not better
        - Do not include greetings like 'Hello, this is an AI'
        - No markdown or extra formatting
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        english_text = response.text.strip()
        hindi_text = translate_to_hindi(english_text)

        return hindi_text

    except Exception as e:
        print(f"Gemini API error (call script): {e}")
        return "कृपया अपनी दवा समय पर लें और अगर तबियत में सुधार न हो तो डॉक्टर से संपर्क करें।"

    
if __name__ == "__main__":
     print(generate_followup_email("Himanshi", "fever", "paracetamol", 7))
     hindi_call = generate_followup_call_script("Himanshi", "fever", "paracetamol", 7)
     print("📞 Hindi Call Script:\n", hindi_call)
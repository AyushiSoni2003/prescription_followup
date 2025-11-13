# voice_utils.py
import os
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

def generate_hindi_audio(text, output_file="hindi_followup.mp3"):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise ValueError("ELEVENLABS_API_KEY not found in environment variables.")

    client = ElevenLabs(api_key=api_key)

    # You can change the voice to one that supports Hindi naturally (like "Bella", "Antoni", etc.)
    audio = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",   # Choose any preferred voice ID
        model_id="eleven_multilingual_v2",
        text=text
    )

    # Save generated voice to file
    with open(output_file, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    print(f"Hindi voice saved as {output_file}")
    return output_file

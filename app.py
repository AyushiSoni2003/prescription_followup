from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
from followup_scheduler import add_prescription
from database import SessionLocal, Prescription  


# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "defaultsecret")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_patient',methods=['GET','POST'])
def add_patient():
    if request.method == 'POST':
        patient_name = request.form.get('patient_name')
        patient_email = request.form.get('patient_email')
        phone_number = request.form.get('patient_phone')
        disease = request.form.get('disease')
        prescription = request.form.get('prescription')
        days = request.form.get('days')

        add_prescription(
            patient_name=patient_name,
            patient_email=patient_email,
            disease=disease,
            prescription_text=prescription,
            days=days,
            patient_phone=phone_number
        )
        
        flash("Patient details saved successfully!", "success")
        return redirect(url_for('home'))
    return render_template('add_patient.html')

@app.route('/patient')
def patient_list():
    """Fetch all patients from the database and display them."""
    session = SessionLocal()
    try:
        patients = session.query(Prescription).all()
        print(f"Fetched {len(patients)} patients")  
        return render_template('patient_list.html', patients=patients)
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
from database import db
from models import Prescription
from mail_utils import send_followup_email
from twilio_utils import initiate_followup_call
from followup_scheduler import schedule_followup
import threading

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prescriptions.db"
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]
        email = request.form["email"]
        disease = request.form["disease"]
        medicine = request.form["medicine"]
        duration = int(request.form["duration"])
        phone = request.form["phone"]

        new_prescription = Prescription(
            patient_name=name,
            patient_email=email,
            diagnosed_disease=disease,
            prescribed_medicine=medicine,
            duration_days=duration,
            phone_number=phone
        )

        db.session.add(new_prescription)
        db.session.commit()

        # Send email
        send_followup_email(email, name, medicine, duration)

        # Initiate call
        initiate_followup_call(phone, name)

        # Schedule follow-up after duration
        threading.Thread(target=schedule_followup, args=(new_prescription.id, duration)).start()

        flash("Prescription added and follow-up scheduled successfully!", "success")
        return redirect(url_for("home"))

    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

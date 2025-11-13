from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to PostgreSQL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Prescription model
class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(100), nullable=False)
    patient_email = Column(String(120), nullable=False)
    disease = Column(String(120), nullable=False)
    prescription = Column(Text, nullable=False)
    days = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    followup_sent = Column(Boolean, default=False)
    patient_phone = Column(String(20), nullable=False)

# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database and tables created successfully")

if __name__ == "__main__":
    init_db()

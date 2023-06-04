from sqlalchemy import Boolean, Column, ForeignKey, Integer,String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Doctors(Base): 
    __tablename__ = "Doctors"
    Doc_id = Column(Integer, primary_key=True)
    doctor_name = Column(String)
    age = Column(String)
    specialty = Column(String)
    email = Column(String)
    phone = Column(Integer) 

class Users(Base):
    __tablename__ = "Users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    age = Column(Integer)
    email = Column(String)
    phone = Column(Integer)
    
class Appointments(Base):
    __tablename__ = "Appointments"
    Appo_id = Column(Integer, primary_key=True)
    when = Column(DateTime)

class MedicalHistories(Base):
    __tablename__ = "MedicalHistories"
    History_id = Column(Integer,primary_key=True)
    algergies = Column(String)
    pastDiseases = Column(String)


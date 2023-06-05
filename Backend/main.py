from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from fastapi import Request
import requests
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt

import models

from database import engine, SessionLocal

from sqlalchemy.orm import Session

from datetime import date, datetime


VIDEOSDK_API_KEY = "cf3eb927-dffd-4be6-a16a-cdb9305502d3"
VIDEOSDK_SECRET_KEY = "427afac3767f19f472c4e1b41adef461fe6a2055ed544533bd1628a04f6df76e"
VIDEOSDK_API_ENDPOINT = "https://api.zujonow.com"

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db= SessionLocal()
        yield db
    finally: 
        db.close()


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
docs = {

}

class Doctor(BaseModel):
    doctor_name : str
    age : int
    specialty : str
    email : str
    phone : int


class User(BaseModel):
    username:str
    age: int
    phone: int
    email: str
    fullname: str
    
    
class MedHistory(BaseModel):
    alergies: str
    pastDiseases: str

class Appointment(BaseModel):
    when : datetime


@app.get("/get-token")
def getToken():
    expiration_in_seconds = 600
    expiration = datetime.datetime.now() + datetime.timedelta(seconds=expiration_in_seconds)
    token = jwt.encode(payload={
        'exp': expiration,
        'apikey': VIDEOSDK_API_KEY,
        'permissions': ["allow_join", "allow_mod"],
    },  key=VIDEOSDK_SECRET_KEY, algorithm="HS256")
    token = token.decode('UTF-8')

    if __name__ == '__main__':
        print(getToken())

@app.post('/newToken')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token':form_data.username + 'token'}

    
@app.post("/create-meeting")
def createMeet(request: Request):
    obj = request.get_json()
    res = requests.post(VIDEOSDK_API_ENDPOINT + "/api/meetings",
                        headers={"Authorization": obj["token"]})
    return res.json()

@app.post("/validate-meeting/{meetingId}")
def validateMeeting(meetingId: str, request:Request):
    print(meetingId)
    obj = request.get_json()
    res = requests.post(VIDEOSDK_API_ENDPOINT + "/api/meetings/" +
                        meetingId, headers={"Authorization": obj["token"]})
    return res.json()

@app.get("/getDoc")
def getDoc(db: Session = Depends(get_db)):
    return db.query(models.Doctors).all()

app.post("/newDoc")
def newDoc(doc:Doctor, db: Session = Depends(get_db)):
    if models.Doctors.Doc_id in docs:
        return {"error":"Doctors' ID already exists"}
    doc_model = models.Doctors()
    doc_model.doctor_name = doc.doctor_name
    doc_model.age = doc.age
    doc_model.email = doc.email
    doc_model.phone = doc.phone
    doc_model.specialty = doc.specialty

    db.add(doc_model)
    db.commit()

    return doc

app.put("/{doc_id}")
def update_doc(doc_id: int, doc:Doctor,db: Session = Depends(get_db)):
    doc_model = db.query(models.Doctors).filter(models.Doctors.Doc_id == doc_id).first()

    if doc_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {doc_id} : ID was not found"
        )

    if doc_model.doctor_name != None:
        doc_model.doctor_name = doc.doctor_name
    if doc_model.age != None:
        doc_model.age = doc.age
    if doc_model.email != None:
        doc_model.email = doc.email
    if doc_model.phone != None:
        doc_model.phone = doc.phone
    if doc_model.specialty != None:
        doc_model.specialty = doc.specialty
    
    db.add(doc_model)
    db.commit()
    return doc

@app.delete("/{doc_id}")
def delete_doc(doc_id: int, db:Session = Depends(get_db)):
    doc_model = db.query(models.Doctors).filter(models.Doctors.Doc_id == doc_id).first()

    if doc_model is None:
        raise HTTPException(
            status_code = 404,
            details=f"ID {doc_id}: Does not exist"
        )
    db.query(models.Doctors).filter(models.Doctors.Doc_id == doc_id).delete()
    db.commit()

@app.get("/getAppointment")
def getAppointment(db:Session = Depends(get_db)):
    return db.query(models.Appointments).all()

@app.post("/newAppoint")
def newAppoint(Appo: Appointment, db:Session = Depends(get_db)):
    if models.Appointments.Appo_id in Appo:
        return {"error":"Doctors' ID already exists"}
    Appo_model = models.Appointments()
    Appo_model.when = Appo.when

    db.add(Appo)
    db.commit()

    return Appo

@app.put("/{Appo_id}")
def editAppo(Appo_id: int, Appo: Appointment, db:Session = Depends(get_db)):
    Appo_model = db.query(models.Appointments).filter(models.Appointments == Appo_id).first()

    if Appo_model is None:
        raise HTTPException(
            status_code=404,
            details=f"ID {Appo_id}: Does not exist"
        )

    if Appo_model.when != None:
        Appo_model.when = Appo.when
    
    db.add(Appo)
    db.commit()

    return Appo

@app.delete("/{Appo_id}")
def deleteAppo(Appo_id:int, Appo:Appointment, db:Session = Depends(get_db)):
    Appo_model = db.query(models.Appointments).filter(models.Appointments.Appo_id == Appo_id).first()
    
    if Appo_model is None:
        raise HTTPException(
            status_code=404,
            details=f"ID {Appo_id}: Does not exist"
        )
    
    db.query(models.Appointments).filter(models.Appointments.Appo_id == Appo_id).delete()
    db.commit()

@app.get("/getUser")
def getUser(db : Session = Depends(get_db())):
    db.query(models.Users).all()

@app.post("/newUser")
def newUser(Use:User, db:Session = Depends(get_db)):
    if models.Users.user_id in Use:
        return {"error": "Doctors' ID already exists"}
    User_model = models.Users()
    User_model.username = Use.username
    User_model.email = Use.email
    User_model.fullname = Use.fullname
    User_model.phone = Use.phone
    User_model.age = Use.age

    db.add(Use)
    db.commit()

    return Use


app.put("/{user_id}")
def update_doc(user_id: int, Use: User, db: Session = Depends(get_db)):
    User_model = db.query(models.Users).filter(
        models.Users.user_id == user_id).first()

    if  User_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {user_id} : ID was not found"
        )

    if User_model.fullname != None:
        User_model.fullname = Use.fullname
    if User_model.age != None:
        User_model.age = Use.age
    if User_model.email != None:
        User_model.email = Use.email
    if User_model.phone != None:
        User_model.phone = Use.phone

    db.add(User_model)
    db.commit()
    return Use


@app.delete("/{user_id}")
def delete_doc(user_id: int, db: Session = Depends(get_db)):
    User_model = db.query(models.Users).filter(
        models.Users.user_id == user_id).first()
    if User_model is None:
        raise HTTPException(
            status_code=404,
            details=f"ID {user_id}: Does not exist"
        )
    db.query(models.Users).filter(models.Users.user_id == user_id).delete()
    db.commit()


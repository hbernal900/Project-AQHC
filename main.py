from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from database import engine, localSession
from schemas import UserData, UserId
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def root():
    return 'Hi estoy probando mi api en mi pc personal'
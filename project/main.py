from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from models import Schedule
from servises import engine, create_db_and_tables
from sqlmodel import Session
from scraper_metro import x


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True
    #allow_methods = ["*"]
    #allow_headers = ["*"]
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/add-schedule/")
def add_schedule(schedule: Schedule):
    with Session(engine) as session:
        session.add()
        session.commit()
        session.refresh(schedule)
        return schedule

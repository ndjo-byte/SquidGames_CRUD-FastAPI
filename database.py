import os
from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
from models import Supplier, Equipment, FailureIncident

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file.")

print(f"Connecting to: {DATABASE_URL}")

def create_tables() -> None:
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__": 
    create_tables()
    print("Database and Tables Created")
    print(SQLModel.metadata.tables.keys())
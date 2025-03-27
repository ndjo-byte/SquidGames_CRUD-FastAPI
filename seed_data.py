import pandas as pd
from sqlmodel import Session
from database import engine
from models import Supplier, Equipment, FailureIncident

def seed_table_from_csv(csv_path, model_class):
    df = pd.read_csv(csv_path)
    print(df.head(5))  
    records = df.to_dict(orient="records")  
    objects = [model_class(**record) for record in records]

    with Session(engine) as session:
        session.add_all(objects)  
        session.commit()

if __name__ == "__main__":
    seed_table_from_csv("seed_data/supplier.csv", Supplier)
    seed_table_from_csv("seed_data/equipment.csv", Equipment)
    seed_table_from_csv("seed_data/failure_incident.csv", FailureIncident)
    print("✅ Data successfully inserted!")

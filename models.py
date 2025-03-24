from sqlmodel import SQLModel, Field, Relationship, create_engine
from typing import Optional, List
from sqlalchemy import Date



class Suppliers(SQLModel, Table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str

class Equipment(SQLModel, Table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    supplier_id : Optional[int]  = Field(default=None, foreign_key="Suppliers.id")
    game_type: str
    installation_date: Date

class FailureIncidents(SQLModel, Table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    failed_equipmente_id: Optional[int] = Field(default=None, foreign_key="Equipment.id")
    failure_type: str
    failure_date: Date
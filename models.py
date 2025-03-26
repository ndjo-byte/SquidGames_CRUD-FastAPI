from sqlmodel import SQLModel, Field, Relationship, create_engine
from typing import Optional, List
from datetime import date


class Supplier(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    country: str

    equipment: List["Equipment"] = Relationship(back_populates="supplier")

class Equipment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    supplier_id : Optional[int]  = Field(default=None, foreign_key="supplier.id")
    game_type: str
    installation_date: date

    supplier: Supplier = Relationship(back_populates="equipment")
    failure: List["FailureIncident"] = Relationship(back_populates="equipment")

class FailureIncident(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    failed_equipmente_id: Optional[int] = Field(default=None, foreign_key="equipment.id")
    failure_type: str
    failure_date: date

    equipment: Equipment = Relationship(back_populates="failure")
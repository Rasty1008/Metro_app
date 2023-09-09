from sqlmodel import Field, SQLModel
from typing import Optional

class Schedule(SQLModel, table=True):
    id: Optional[int] = Field(default = None, primary_key = True)
    station: str
    rayymbek_momyshuly: str
    momyshuly_rayymbek: str
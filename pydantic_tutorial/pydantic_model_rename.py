# See problem.txt for the problem this is trying to solve

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

app = FastAPI()

class FieldNames(BaseModel):
    building: str = Field(alias="spi:triParentBuildingTX")
    space: str = Field(alias="spi:triNameTX")
    reservation_start: datetime = Field(alias="spi:triStartDT")
    reservation_end: datetime = Field(alias="spi:triEndDT")
    property: str = Field(alias="spi:triParentPropertyTX")
    requested_by: str = Field(alias="spi:triRequestedByFullNameTX")
    about: str = Field(alias="rdf:about")

    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

@app.post("/transform")
async def transform(field_names: List[FieldNames]):
    try:
        field_names = [field_name.model_dump(by_alias=False) for field_name in field_names]
        return field_names
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

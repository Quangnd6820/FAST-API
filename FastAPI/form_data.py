from pydantic import BaseModel, EmailStr
from typing import Optional, List
from fastapi import HTTPException

class boxes(BaseModel):
    box: List[float]

class dataSample(BaseModel):
    id: str
    type: str
    name: str
    url: str

class categorie(BaseModel):
    id: str
    type: str
    name: str

class annotation(BaseModel):
    id: str
    type: str
    categoryId: str
    categoryName: str
    dataId: str
    annotation: boxes

class data_api(BaseModel):
    id: str
    dataSamples: List[dataSample]
    annotations: List[annotation]

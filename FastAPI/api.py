from fastapi import FastAPI, Query, Path, Body, HTTPException
from datetime import datetime, time, timedelta
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from uuid import UUID
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

app = FastAPI()

#---------------------------------------------------GET API----------------------------------------------------------#
@app.get("/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


@app.get("/items/fix")
async def rd_items_1(
                        q: List[str] = Query(
                                                None,
                                                title="Query string",
                                                description="Query string for the items to search in the database that have a good match",
                                                min_length=3,
                                            )
                    ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/fixed")
async def read_items_2(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items_3(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/infomations/")
async def info(name: str = "Quang", date: str = "21/06"):
    return {"name": name, "date": date}


#---------------------------------------------------POST API----------------------------------------------------------#
@app.post("/post/items/")
async def create_item(item: Item):
    return item


@app.post("/post/item/")
async def create_item_update(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/post/update/{item_id}/")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results



#--------------------------------------------------Update Response Model--------------------------------------------------------
@app.post("/user/", response_model=UserOut, response_model_exclude=["email"])
async def create_user(user: UserIn):
    return user

import pymongo

client = pymongo.MongoClient("mongodb+srv://seta-quangnguyen:1@cluster0.kkp0b.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test

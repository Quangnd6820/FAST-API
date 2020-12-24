from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from form_data import data_api

data = {
            "id": "jkfajdfa",
            "dataSamples":  [
                                {
                                    "id": "aaa",
                                    "type": "Image",
                                    "name": "Image1.jpg",
                                    "url": "https://assets.ey.com/content/dam/ey-sites/ey-com/en_gl/topics/global-review/2019/ey-staff-at-event.jpg"
                                }
                            ],
            "categories":   [
                                {
                                    "id": "jjjjj",
                                    "type": "BoundingBox2D",
                                    "name": "Person",
                                }
                            ],
            "annotations":  [
                                {
                                    "id": "kkkk6",
                                    "type": "BoundingBox2D",
                                    "categoryId": "jjjjj",
                                    "categoryName": "Person",
                                    "dataId": "aaa",
                                    "annotation":   {
                                                        "box": [0.0, 0.0, 0.3, 0.4]
                                                    }
                                },
                                {
                                    "id": "kkk5k",
                                    "type": "BoundingBox2D",
                                    "categoryId": "jjjjj",
                                    "categoryName": "Person",
                                    "dataId": "aaa",
                                    "annotation":   {
                                                        "box": [0.1, 0.2, 0.3, 0.4]
                                                    }
                                },
                                {
                                    "id": "kk1kk",
                                    "type": "BoundingBox2D",
                                    "categoryId": "jjjjj",
                                    "categoryName": "Person",
                                    "dataId": "aaa",
                                    "annotation":   {
                                                        "box": [0.5, 0.2, 0.7, 0.4]
                                                    }
                                },
                                {
                                    "id": "kkkk2",
                                    "type": "BoundingBox2D",
                                    "categoryId": "jjjjj",
                                    "categoryName": "Person",
                                    "dataId": "aaa",
                                    "annotation":   { 
                                                        "box": [0.1, 0.4, 0.5, 0.8]
                                                    }
                                },
                                {
                                    "id": "kkk3k",
                                    "type": "BoundingBox2D",
                                    "categoryId": "jjjjj",
                                    "categoryName": "Person",
                                    "dataId": "aaa",
                                    "annotation":   {
                                                        "box": [0.5, 0.6, 1.0, 1.0]
                                                    }
                                }
                            ]
        }

app = FastAPI()

@app.post("/")
async def read_items(q: data_api):
    return q


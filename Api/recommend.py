from fastapi import APIRouter, FastAPI
from Model.predict import predict_model
from pydantic import BaseModel
class BookRequest(BaseModel):
    nameBook: str

app = FastAPI()

@app.get('/')
def root_api():
    return {"message": "Welcome to The Nghia"}

@app.post('/recommend')
async def recommend(book_request: BookRequest):
    name_book = book_request.nameBook
    try:
        data = predict_model(name_book)
        return data
    except Exception as e:
        return {"error": str(e)}
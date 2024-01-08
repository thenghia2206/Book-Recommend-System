from fastapi import APIRouter, FastAPI
from Model.predict import predict_model
from pydantic import BaseModel
class BookRequest(BaseModel):
    bookId: str

app = FastAPI()

@app.get('/')
def root_api():
    return {"message": "Welcome to The Nghia"}

@app.post('/recommend')
async def recommend(book_request: BookRequest):
    bookId = book_request.bookId
    try:
        data = predict_model(bookId)
        return data
    except Exception as e:
        return {"error": str(e)}
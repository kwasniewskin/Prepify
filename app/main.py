from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI(title="Prepify")

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Prepify działa!"}

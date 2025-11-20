from fastapi import FastAPI

from app.api.routes import router as api_router

app = FastAPI(title="Meine Freund Backend")


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Backend is running"}


app.include_router(api_router)


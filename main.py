from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth as auth_router, tasks as tasks_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(auth_router.router)
app.include_router(tasks_router.router)

@app.get("/")
def root():
    return {"message": "Task Manager API is running"}
from uvicorn import run
from fastapi import FastAPI
from dotenv import load_dotenv

from api.routes import init_routes

load_dotenv()
app = init_routes(FastAPI())

if __name__ == "__main__":
    run("api.main:app")

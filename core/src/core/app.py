# app
from fastapi import FastAPI

def endpoints(app: FastAPI):

    @app.post("/simulate")
    def _():
        
""" endpoints """
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.webapi.endpoints import register_routers, register_exception_handlers

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://creditsim-frontend.s3-website.us-east-2.amazonaws.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_routers(app)
register_exception_handlers(app)

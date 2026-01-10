""" endpoints """
import logging
from fastapi import FastAPI
from backend.webapi.endpoints import register_routers, register_exception_handlers

logging.basicConfig(level=logging.WARN,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

app = FastAPI()


register_routers(app)
register_exception_handlers(app)

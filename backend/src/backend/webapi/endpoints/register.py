""" register """
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from .migrate import router as migrate_router
from .simulation import router as simula_router
from .read_simulation import router as read_simula_router


def register_routers(app: FastAPI):
    """ endpoint register """

    app.include_router(router=simula_router, tags=["Credit Simulation"])
    app.include_router(router=read_simula_router, tags=["Credit Simulation"])
    app.include_router(router=migrate_router, tags=["Migration"])


def register_exception_handlers(app):
    """ exception handler """
    @app.exception_handler(HTTPException)
    async def _(_: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"messages": exc.detail},
        )

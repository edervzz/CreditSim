""" register """
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from .migrate import router as migrate_router
from .simulation import router as simula_router


def register_routers(app: FastAPI):
    """ endpoint register """

    app.include_router(migrate_router)
    app.include_router(simula_router)


def register_exception_handlers(app):
    """ exception handler """
    @app.exception_handler(HTTPException)
    async def _(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"messages": exc.detail},
        )

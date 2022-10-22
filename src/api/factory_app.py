from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import ProgrammingError
from loguru import logger

from src.api.routers import (
    user,
    users_auth,
    ore_concentrate,
    content,
    report
)

from src.utils.exceptions.base import JSONException
from src.config import get_settings

settings = get_settings()
api_url = settings.API_URL
api_name = settings.API_NAME


def create_app(with_logger: bool = True):
    application = FastAPI(title=f'{api_name}',
                          version='0.1.0',
                          docs_url=f'{api_url}/docs',
                          redoc_url=f'{api_url}/redoc',
                          openapi_url=f'{api_url}/openapi.json')

    # Routers
    application.include_router(users_auth.router, prefix=api_url)
    application.include_router(user.router, prefix=api_url)
    application.include_router(ore_concentrate.router, prefix=api_url)
    application.include_router(content.router, prefix=api_url)
    application.include_router(report.router, prefix=api_url)

    # Exception handlers
    @application.exception_handler(JSONException)
    async def error_handler_400(request: Request, exception: JSONException):
        logger.exception(exception) if with_logger else None
        return JSONResponse(status_code=exception.status_code,
                            content={"message": exception.message})

    @application.exception_handler(ProgrammingError)
    async def handler_alchemy_integrity_error(request: Request, programming_err):
        logger.exception(programming_err) if with_logger else None
        err_name = "sqlalchemy.exc.ProgrammingError"
        traceback = programming_err.args[0] or str(programming_err)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"message": {'err_name': err_name,
                                                 'traceback': traceback}})

    @application.exception_handler(AttributeError)
    async def handler_alchemy_integrity_error(request: Request, attribute_err):
        logger.exception(attribute_err) if with_logger else None
        err_name = "AttributeError"
        traceback = attribute_err.args or str(attribute_err)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"message": {'err_name': err_name,
                                                 'traceback': traceback}})

    return application

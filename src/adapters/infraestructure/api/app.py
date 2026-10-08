from fastapi import FastAPI;
from .router.router import test_postman;
from ....settings import GLPI_DATABASE, GLPI_HOST, GLPI_PASSWORD, GLPI_USER;

if __name__ == "__main__":
    app = FastAPI(title="Zulip Bot API");
    app.include_router(test_postman)
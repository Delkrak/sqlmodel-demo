from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import create_db_and_tables
from .hero.hero_routes import router as hero_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup:
    create_db_and_tables()

    yield

    # Shutdown:


app = FastAPI(lifespan=lifespan)

# TODO: override the app.include_router to collect lifespan and run them with


HEROES_ROUTE = "/heroes"
app.include_router(hero_router, prefix=HEROES_ROUTE, tags=["heroes"])

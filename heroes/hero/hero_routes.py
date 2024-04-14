from typing import List
from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter, HTTPException, Query
from sqlmodel import Session
from loguru import logger

from ..database import default_session
from .hero_schemas import HeroPublic, HeroCreate, HeroUpdate
from .hero_operations import (
    create_hero,
    read_heroes,
    read_hero,
    update_hero,
    delete_hero,
)


router = APIRouter()


@router.post("/", response_model=HeroPublic)
def create_hero_route(
    hero: HeroCreate,
    session: Session = default_session,
):
    return create_hero(session, hero)


@router.get("/", response_model=List[HeroPublic])
def read_heroes_route(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    session: Session = default_session,
):
    return read_heroes(session, offset, limit)


@router.get("/{hero_id}", response_model=HeroPublic)
def read_hero_route(
    hero_id: int,
    session: Session = default_session,
):
    hero = read_hero(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@router.patch("/{hero_id}", response_model=HeroPublic)
def update_hero_route(
    hero_id: int,
    hero: HeroUpdate,
    session: Session = default_session,
):
    db_hero = update_hero(session, hero_id, hero)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return db_hero


@router.delete("/{hero_id}")
def delete_hero_route(
    hero_id: int,
    session: Session = default_session,
):
    hero = delete_hero(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return {"ok": True}

from sqlmodel import Session, select

from .hero_models import Hero
from .hero_schemas import HeroCreate, HeroUpdate


def create_hero(session: Session, hero: HeroCreate):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


def read_heroes(session: Session, offset: int = 0, limit: int = 100):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes


def read_hero(session: Session, hero_id: int):
    hero = session.get(Hero, hero_id)
    return hero


def update_hero(session: Session, hero_id: int, hero: HeroUpdate):
    db_hero = session.get(Hero, hero_id)
    hero_data = hero.model_dump(exclude_unset=True)
    for key, value in hero_data.items():
        setattr(db_hero, key, value)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


def delete_hero(session: Session, hero_id: int):
    hero = session.get(Hero, hero_id)
    session.delete(hero)
    session.commit()
    return {"ok": True}

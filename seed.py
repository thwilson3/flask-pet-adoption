"""Seed file to make sample data for pets db"""

from models import Pet, db
from app import app

db.drop_all()
db.create_all()

pistachio = Pet(
    name="Pistachio",
    species="dog",
    photo_url='',
    age='senior',
    notes='partially deaf'
    )

orbit = Pet(
    name="Orbit",
    species="dog",
    photo_url='',
    age='adult'
    )

lexi = Pet(
    name="Lexi",
    species="dog",
    photo_url='',
    age='adult'
    )

db.session.add(pistachio)
db.session.add(orbit)
db.session.add(lexi)

db.session.commit()
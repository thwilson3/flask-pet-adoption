import os

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
"DATABASE_URL", 'postgresql:///pets')
app.config["SECRET_KEY"] = 'fdhsabk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get('/')
def homepage():
    """Redirects to pets page"""

    pets = Pet.get_all_pets()
    print(pets)
    return render_template('/homepage.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def handle_add_pet_form():
    """Shows add pet form and handles submit"""

    # pet = Pet.query.get_or_404(id)
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes,
            available=available)

        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add-pet.html', form=form)


@app.route('/<int:id>', methods=["GET", "POST"])
def view_or_update_pet(id):
    """Show more info on pet and form to edit details"""

    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)
    # breakpoint()

    return render_template('pet-info.html', form=form, pet=pet)
    # if form.validate_on_submit():

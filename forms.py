from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Pet Name",
        validators=[InputRequired()])

    species = StringField("Animal Type",
        validators=[InputRequired(),
            AnyOf(["dog", "cat", "porcupine"])])

    photo_url = StringField("Image URL",
        validators=[Optional(), URL()])

    age = SelectField('Age',
        choices=[("baby", "Baby"), ("young", "Young"),
        ("adult", "Adult"), ("senior", "Senior")],
        validators=[InputRequired()])

    notes = StringField("Additional Notes",
        validators=[Optional()])

    available = BooleanField()
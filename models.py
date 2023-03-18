

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    app.app_context().push()
    db.app = app
    db.init_app(app)



class Pet(db.Model):
    """Class to contain pet info"""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    name = db.Column(
        db.Text,
        nullable = False
    )

    species = db.Column(
        db.Text,
        nullable = False
    )

    photo_url = db.Column(
        db.Text,
        nullable = False,
        default = ''
    )

    age = db.Column(
        db.Text,
        nullable = False,
           # in ['baby', 'young', 'adult', 'senior']
    )

    notes = db.Column(
        db.Text,
        nullable = True
    )

    available = db.Column(
        db.Boolean,
        nullable = False,
        default = True
    )

    @classmethod
    def get_all_pets(cls):
        """Returns a list of all Pet instances"""

        return Pet.query.all()
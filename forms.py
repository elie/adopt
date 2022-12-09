"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    age = SelectField(
        "Age",
        choices=[("baby", "Baby"), ("young", "Young"), ("adult", "Adult"), ("senior", "Senior")]
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")

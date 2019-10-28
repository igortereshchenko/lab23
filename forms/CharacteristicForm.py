from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField, IntegerField
from wtforms import validators


class CharacteristicForm(Form):

    charac_name = StringField("Name: ", [
        validators.DataRequired("Please enter your name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])
    charac_description = StringField("Description: ", [
        validators.DataRequired("Please enter your description."),
        validators.Length(3, 20, "Description should be from 3 to 20 symbols")
    ])

    submit = SubmitField("Save")
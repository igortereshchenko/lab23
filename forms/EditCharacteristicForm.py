from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField
from wtforms import validators


class EditCharacteristicForm(Form):

    charac_name = StringField("Name: ", [
        validators.DataRequired("Please enter your description."),
        validators.Length(1, 20, "Description should be from 3 to 20 symbols")
    ])
    charac_description = StringField("Description: ", [
        validators.DataRequired("Please enter your description."),
        validators.Length(3, 20, "Description should be from 3 to 20 symbols")
    ])

    submit = SubmitField("Save")
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField, IntegerField
from wtforms import validators


class UserForm(Form):

    user_name = StringField("Name: ", [
        validators.DataRequired("Please enter your name."),
        validators.Length(1, 20, "Name should be from 3 to 20 symbols")
    ])
    user_birthday = DateField("birthday: ", format='%Y-%m-%d')

    user_salary = IntegerField("Description: ", [validators.NumberRange(min=0, max=1000, message="must be between 0 to 1000")])

    user_position = StringField("position: ", [
        validators.DataRequired("Please enter your position."),
        validators.Length(1, 20, "position should be from 3 to 20 symbols")
    ])

    submit = SubmitField("Save")
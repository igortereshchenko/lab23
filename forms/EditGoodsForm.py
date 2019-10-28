from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField
from wtforms import validators


class EditGoodsForm(Form):
    good_id = HiddenField("id:")

    good_name = StringField("Name: ", [
        validators.DataRequired("Please enter your name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    good_model = StringField("Model: ", [
        validators.DataRequired("Please enter your model."),
        validators.Length(0, 20, "Model should be from 3 to 20 symbols")
    ])




    submit = SubmitField("Save")
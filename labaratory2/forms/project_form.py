from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField, IntegerField
from wtforms import validators


class ProjectForm(Form):

   project_name = HiddenField()

   project_cost = IntegerField("Cost: ",[
                                    validators.DataRequired("Please enter your cost."),
                                    validators.number_range(0, 10000, "Name should be from 3 to 20 symbols")
                                 ])

   project_lider = StringField("Lider: ", [
                                   validators.DataRequired("Please enter your lider."),
                                   validators.Length(0, 10, "Name should be from 3 to 20 symbols")
                               ])

   project_department = HiddenField()


   submit = SubmitField("Save")



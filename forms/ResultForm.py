from flask_wtf import Form
from wtforms import StringField, SubmitField




class SearchForm(Form):
    group_name = StringField('User name: ')
    submit = SubmitField('Search')

    def get_result_by_Schedule(self):
        helper = UserHelper()
        return helper.getVariable(self.group_name.data)
    def get_result_by_Group(self):
        helper = UserHelper()
        return helper.getVariable(self.schedule_data.data)
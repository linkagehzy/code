from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField,StringField,PasswordField
from wtforms.validators import Required,DataRequired

class SubmitForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    tel = StringField('Tel',validators=[DataRequired()])
    oidname = StringField('oidname',validators=[DataRequired()])
    add = StringField('add',validators=[DataRequired()])
    
class User():
	info = {'name':'None','tel':'none','oidname':'none','add':'none'}
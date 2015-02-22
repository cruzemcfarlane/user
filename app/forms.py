from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextField;
from wtforms.validators import DataRequired, Required, Email

class LoginForm(Form):
	firstname = TextField('First Name', validators=[Required()]
	lastname = TextField('Last Name', validators=[Required(), Email()])
	username = TextField('Username', validators=[Required()])
	userid = TextField('ID', validators=[Required()])
	sex = TextField('Sex', validators=[Required()])
	age = TextField('Age', validators=[Required()])
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)

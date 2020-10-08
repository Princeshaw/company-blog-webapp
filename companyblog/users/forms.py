from flask_wtf import FlaskFrom
from wtforms import StringField, PasswordField, SubmitedField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidatationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from companyblog.models import User

class LoginForm(FlaskFrom):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit  = SubmitedField('Log In')

class RegistrationForm(FlaskFrom):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords Must Match')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit  = SubmitedField('Register')


    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidatationError('Your email has been registered already!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidatationError('Your Username has been registred already!')   


class UpdateUserForm(FlaskFrom):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitedField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidatationError('Your email has been registered already!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidatationError('Your Username has been registred already!')

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class RegisterForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired(), Length(min = 4, max = 20)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8, max=20)])
    confirm = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email',validators=[DataRequired(),Email()])
    phone = StringField('Phone',validators=[DataRequired(),Length(min=10, max=10)])
    #address = StringField('Address', validators=[DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Register',)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    age = StringField('Age')
    underlying = StringField('Underlying')
    fever = StringField('Fever')
    shortnessOfBreath = StringField('ShortnessOfBreath')
    lossOfTaste = StringField('LossOfTaste')
    soreThroat = StringField('SoreThroat')
    riskFactor = StringField('RiskFactor')
    submit = SubmitField('Submit')
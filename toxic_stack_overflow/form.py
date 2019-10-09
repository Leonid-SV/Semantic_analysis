from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InstantForm(FlaskForm):
    text_field = StringField('введите значение', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])



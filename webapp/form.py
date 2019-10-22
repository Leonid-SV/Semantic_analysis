# описание элементов форм для Html

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired

class SmallTextField(FlaskForm):
    text = TextAreaField('Запрос', validators=[DataRequired()])
    submit = SubmitField('Подтвердить', validators=[DataRequired()])

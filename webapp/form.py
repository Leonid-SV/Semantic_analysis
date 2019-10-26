# описание элементов форм для Html
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired

db = SQLAlchemy()

class ModelComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_post= db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

class SmallTextField(FlaskForm):
    text = TextAreaField('Запрос', validators=[DataRequired()])
    submit = SubmitField('Подтвердить', validators=[DataRequired()])

class ModelPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_type_id = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Text, nullable=False)
    accepted_answer_id = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    view_count = db.Column(db.Integer, nullable=False)
    dody = db.Column(db.Text, nullable=False)
    owner_user_id = db.Column(db.Integer, nullable=False)
    owner_display_name = db.Column(db.Text, nullable=False)
    last_editor_user_id = db.Column(db.Integer, nullable=False)
    last_editor_display_name = db.Column(db.Text, nullable=False)
    last_edit_date = db.Column(db.DateTime, nullable=False)
    last_activity_date = db.Column(db.DateTime, nullable=False)
    community_owned_date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.Text, nullable=False)
    tags = db.Column(db.Text, nullable=False)
    answer_count = db.Column(db.Integer, nullable=False)
    comment_count = db.Column(db.Integer, nullable=False)
    favorite_count = db.Column(db.Integer, nullable=False)
    closed_date = db.Column(db.DateTime, nullable=False)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModelComments(db.Model):
    id = db.Column(db.Text, primary_key=True)
    id_post= db.Column(db.Text, nullable=False)
    score = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Text, nullable=False)


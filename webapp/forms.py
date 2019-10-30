from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModelTest(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)


class ModelComments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    postid = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    creationdate = db.Column(db.DateTime, nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    userdisplayname = db.Column(db.Text, nullable=False)


class ModelPosts(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    post_type_id = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Text, nullable=False)
    accepted_answer_id = db.Column(db.Integer, nullable=False)
    creation_date = creation_date = db.Column(db.DateTime, nullable=False)
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

    # def __repr__(self):
    #     return '<ModelPosts {} {} >'.format(self.title, self.url)

class ModelTags(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.Text, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    excerptpostid = db.Column(db.Integer, nullable=True)
    wikipostid = db.Column(db.Integer, nullable=False)
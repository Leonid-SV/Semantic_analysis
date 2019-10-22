from webapp import db_comments, create_app

# создание таблицы в выбранной базе данных
db_comments.create_all(app = create_app())
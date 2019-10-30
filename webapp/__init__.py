# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from webapp.forms import db, ModelPosts, ModelComments, ModelTags
from read_db import *


def create_app():  # фабрика Flask
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/', methods=['POST', 'GET'])
    def index():
        # текстовые константы для страницы:

        title = 'Введите запрос'

        result = ''
        if request.method == 'POST':
            answer = request.form['text']

            try:
                result = get_data(answer, db)  # main function for getting data by input value
            except:
                result = '----- no answer -----'
            finally:
                for r in result:
                    print(type(r))
                    print(r)

        if request.method == 'GET':
            return render_template('index.html', title=title, answer='')

        return render_template('index.html', title=title, answer=result)

    return app


############################
if __name__ == '__main__':
    create_app().run(debug=True)

#export FLASK_APP=webapp_f && export FLASK_ENV=development && flask run
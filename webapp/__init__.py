# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from webapp.forms import db, ModelPosts, ModelComments, ModelTags
from read_db import *


def f_toxic_vals(v0, v1, v2):
    ''' processing results function for provide into web-page'''

    toxic_rslts = [[], [], []]

    v0 = round(v0)
    v1 = round(v1)
    v2 = round(v2)

    over50 = 'progress-circle over50 p'
    under50 = 'progress-circle p'
    toxic_rslts[0] = [v0, over50 + str(v0) if v0 >= 50 else under50 + str(v0)]
    toxic_rslts[1] = [v1, over50 + str(v1) if v1 >= 50 else under50 + str(v1)]
    toxic_rslts[2] = [v2, over50 + str(v2) if v2 >= 50 else under50 + str(v2)]

    return toxic_rslts


def create_app():  # фабрика Flask
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/', methods=['POST', 'GET'])
    def index():
        # текстовые константы для страницы:

        v0, v1, v2 = 5, 10, 50

        title = 'Введите запрос'
        flag = False
        result = ''
        if request.method == 'POST':
            answer = request.form['text']
            flag = True
            try:
                result = get_data(answer)  # main function for getting data by input value

            except:
                result = '----- no answer -----'
            finally:
                flag = True
                for r in result:
                    print(type(r))
                    print(r)
######################################################
                # values for visualising results
                v0 = 65
                v1 = 15
                v2 = 20
######################################################
        if request.method == 'GET':
            return render_template('index.html', title=title, answer='', flag=flag, toxic_vals=f_toxic_vals(v0, v1, v2))

        return render_template('index.html', title=title, answer=result, flag=flag, toxic_vals=f_toxic_vals(v0, v1, v2))

    return app

############################
if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port='5000', debug=False)
pi
#export FLASK_APP=webapp_f && export FLASK_ENV=development && flask run
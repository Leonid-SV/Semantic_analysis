# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from webapp.forms import db, ModelPosts, ModelComments, ModelTags
from read_db import *


# импорт семантического анализа
from semantic import semantic_res

def f_toxic_vals(v0, v1, v2):
    # processing results function for provide into web-page
    # функция предназначена для передачи данных в index.html в виде частей кода с целью отризовки круговых диаграмм
    # эмециональности

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

        # временные текстовые константы для страницы:
        v0, v1, v2 = 5, 10, 50

        title = 'Введите запрос'
        flag = False
        result = ''
        if request.method == 'POST':
            answer = request.form['text']
            answer = answer.lower()
            # information about answer
            #
            print('#'*100)
            print(type(answer))
            print(answer)
            print('#' * 100)

            result = '----- no answer -----'
            # флаг для вызова отображения результатов на странице html
            flag = True
            try:
                # function for getting data by input value
                # вызов функции для извлечениия и предобработки данных для предоставления ее в семантический анализатор
                result = get_data(answer)

            except:         # использовать без параметров не реккомендуется, но тут для красоты сделано исключение
                result = '----- no answer -----'
            finally:
                flag = True
                # печать результатов в стадии отладки приложения
                # for r in result:
                #     print(type(r))
                #     print(r)

                result_in_digits = semantic_res(result)

                v0 = result_in_digits['neg']
                v1 = result_in_digits['neu']
                v2 = result_in_digits['pos']

                # v0 = 10
                # v1 = 20
                # v2 = 30

        if request.method == 'GET':
            return render_template('index.html', title=title, answer='', flag=flag, toxic_vals=f_toxic_vals(v0, v1, v2))

        return render_template('index.html', title=title, answer=result, flag=flag, toxic_vals=f_toxic_vals(v0, v1, v2))

    return app

############################
if __name__ == '__main__':
    create_app().run(port='5000', debug=True)

#export FLASK_APP=webapp_f && export FLASK_ENV=development && flask run
#-h 172.19.65.99
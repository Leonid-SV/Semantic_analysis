from flask import Flask, render_template, request
from webapp.form import SmallTextField
from webapp.model import db, ModelComments
from request_from_db import db_execute


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    #инициализация базы данных. Строка идет после строчки с config потому что для инициализации требуется ключ
    print('******************')
    db.init_app(app)

    @app.route('/', methods=['POST', 'GET'])
    def inputs():
        title = 'Введите запрос'
        stf = SmallTextField()
        answer = ''
        if request.method == 'POST':
            answer = request.form['text']

        try:
            res = db_execute(int(answer))[0]
        except:
            res = '----- no answer -----'

        print(type(res))
        print(res)

        return render_template('index_test.html', title=title, stf=stf, answer=res)

    return app



# запуск сервера Linux из терминала
# export FLASK_APP=webapp && export FLASK_ENV=development && flask run

# запуск сервера Windows из терминала
# set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

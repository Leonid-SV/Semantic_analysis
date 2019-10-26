from flask import Flask, render_template, request
# from webapp.form import SmallTextField
# from webapp.model import db, ModelComments
from request_from_db import db_request

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/', methods=['POST', 'GET'])
    def inputs():
        title = 'Введите запрос'
        global result
        result = ''
        if request.method == 'POST':
            answer = request.form['text']

            try:
                result = db_request(answer)
            except:
                result = '----- no answer -----'
            finally:
                for r in result:
                    print(type(r))
                    print(r)

        # if request.method == 'POST':
        #     reset = request.form['reset']
        #     result = ''

        return render_template('index_test.html', title=title, answer=result)

    result = ''
    return app


# запуск сервера Linux из терминала
# export FLASK_APP=webapp && export FLASK_ENV=development && flask run

# запуск сервера Windows из терминала
# set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

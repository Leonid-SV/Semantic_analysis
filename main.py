from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index(): # где  index() декорированный app.route() вызывается и исполняется?
    answer = ''
    if request.method == 'POST':
        answer = request.form['input']
        print(answer)
    title = 'Семантическая оценка ИТ-направления.'
    return render_template('index.html', title=title, answer=answer)

if __name__ == '__main__':
    app.run(debug = True)

# запуск сервера
# export FLASK_APP
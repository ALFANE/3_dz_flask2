from flask import Flask, request, render_template, session

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def schetchik():
    """    функция предназначена для отображения количества открытий пользователем страницы.
    В случе если пользователь авторизован будет выведено имя пользователя.
    Если пользователь не автоизован также будет выведено соответсвуещее сообщение.
    Реализация выполенена с помощью flask session
    """

    counter = 0
    if session.get('visited'):
        counter = session['visited']
    else:
        session['visited'] = 0
    session['visited'] += 1
    if session.get('username'):
        username = session['username']
        return f'<h2>Страница открыта {counter} раз </p> Авторизован пользователь {username}<h2>'
    return f'<h2>Страница открыта {counter} раз </p>  Пользователь не авторизован<h2>'

@app.route('/login', methods=['GET', 'POST'])
def login():

    '''
    функция предназначена для авторизации двумя способами: GEt и POST запросы
    сначала идет проверка на наличие пользователя в системе, если пользователь уже авторизован,
    будет выведено соответствующее сообщение,
    далее идет проверка на тип запроса и реализация авторизации
    '''

    if session.get('username'):
        username = session['username']
        return f'<h2>Пользователь {username} авторизован</h2>'
    elif request.method == 'GET':
        session['username'] = request.args.get('name')
        if session.get('username'):
            username = session['username']
            return f'<h2>You have written your username: <b>{username}</b> and sent it by GET request</h2>'
        else:
            return render_template('index.html')
    elif request.method == 'POST':
            session['username'] = request.form['name']
            username = session['username']
            return f'<h2>You have written your username: <b>{username}</b> and sent it by POST request</h2>'


@app.route('/logout')
def logaut():

    # В данной функции происходит очистка сессии
    session.clear()
    return '<h1>Session was be clear</h1> '


if __name__=='__main__':
    app.run(debug=True)


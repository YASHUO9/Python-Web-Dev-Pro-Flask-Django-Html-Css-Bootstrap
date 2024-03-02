from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new_user.html', greeting='')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    greeting = f'Hello, {name}!'
    return render_template('new_user.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)

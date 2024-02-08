from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/red')
def red():
    return render_template('red.html')

@app.route('/hello/<name>')
def green(name):
    return render_template('green.html', name=name)

@app.route('/fruits')
def some_fruits():
    fruits = ['apple', 'kiwi', 'orange', 'papaya']
    return render_template('fruits.html', fruits=fruits)

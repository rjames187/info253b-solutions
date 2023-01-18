from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello!</h1><p>Congrats on building your own server!</p><br /></br /><a href="/page2">Go to the next page</a>'

@app.route('/page2')
def page2():
    return '<h1>This is page 2!</h1><p>let us move to page three</p><br /></br /><a href="/page3">Go to the next page</a>'

@app.route('/page3')
def page3():
    return '<h1>This is page 3!</h1><p>And of end of our journey!</p>'

@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello {name}</h1>'
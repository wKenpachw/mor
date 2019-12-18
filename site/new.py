from flask import Flask, render_template

app = Flask(__name__)

class MyClass:
    """A simple example class"""
    i = 12345
    y = 1321313

x = MyClass()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=x)

@app.route('/char')
def char(name=None):
    return render_template('char.html')

@app.route('/chars/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

app.run(host='0.0.0.0')
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)





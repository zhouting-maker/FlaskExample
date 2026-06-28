from flask import Flask, render_template

app = Flask(__name__)


@app.route('/html')
def hello_html():
    return render_template('index.html', name='John', age=30)


@app.route('/user/<name>')
def hello_user(name):
    return f"Hello, {name}!"

@app.route('/age/<int:age>')
def show_age(age):
    return f"you age is {age}!"

@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/user/<name>')
# def hello_user(name):
#     return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
    
    
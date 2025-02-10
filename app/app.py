from flask import Flask, render_template

app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return "Hello CPS3500!"

# New page route
@app.route('/new_page')
def new_page():
    return "This is a New Page!"

# Route using a template
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)

if __name__ == '__main__':
    app.run(debug=True)

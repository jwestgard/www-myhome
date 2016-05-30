from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index.html')
@app.route('/index')
def index():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug = True)

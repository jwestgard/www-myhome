from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask import g
import sqlite3
app = Flask(__name__)
bootstrap = Bootstrap(app)

DATABASE = 'db/bedemss.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
    
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
@app.route('/index.html')
@app.route('/index')
def index():
    return render_template('homepage.html')

@app.route('/bedemss')
def bedemss_home():
    cur = get_db().cursor()
    works = [w for w in query_db('select * from works')]
    return render_template('bedemss.html', works=works)
    
@app.route('/bedemss/<work_id>')
def work_mss(work_id):
    cur = get_db().cursor()
    work = query_db(
        'select * from works where abbreviation = ?', 
        [work_id], one=True)
    return render_template('work_mss.html', work=work)

if __name__ == '__main__':
    app.run(debug = True)

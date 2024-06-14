from flask import Flask;
import psycopg2

conn = psycopg2.connect()


app = Flask('__main__')

@app.route('/')
def home():
    return 'Hello, World !!'

@app.route('/getAllStudent')
def getAllStudent():
    return 'all students data'


if (__name__ == '__main__'):
    app.run(debug=True)
from flask import Flask
import psycopg2
from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig'] = ('evo', 'postgres', 'mettler24')


def log_request(req: 'flask_request', result: str) -> 'None':
    try:
        with UseDatabase(app.config['dbconfig'][0], app.config['dbconfig'][1],
                         app.config['dbconfig'][2]) as cursor:
            sql = """INSERT INTO comment(name, comment, result_comment) VALUES(%s, %s, %s)"""
            cursor.execute(sql, (req.form['Name'],
                                 req.form['Comment'],
                                 str(result)))
    except Exception as err:
        print('Something went wrong:', str(err))


def data_from_Log() -> 'str':
    try:
        with UseDatabase(app.config['dbconfig'][0], app.config['dbconfig'][1],
                         app.config['dbconfig'][2]) as cursor:
            sql = """SELECT name, result_comment FROM comment"""
            cursor.execute(sql)
            data = cursor.fetchall()
        return data
    except Exception as err:
        print('Something went wrong:', str(err))







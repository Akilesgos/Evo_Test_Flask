from flask import Flask, request, render_template, redirect
import psycopg2
from count import counts_worlds
from utils import log_request, data_from_Log


app = Flask(__name__)

app.config['dbconfig'] = ('evo', 'postgres', 'mettler24')


@app.route('/')
def hello() -> '302':
    return redirect('/index')


@app.route('/index')
def leave_comment_page() -> 'html':
    return render_template('index.html',
                           the_title='Welcome to post comments on the web!')


@app.route('/viewlog', methods=["POST"])
def view_the_log() -> 'html':
    name = request.form['Name']
    comment = request.form['Comment']
    result = counts_worlds(comment)
    title = 'Content information'
    row_titles = ("Name", "All Result")
    data = data_from_Log()
    try:
        log_request(request, result)
    except Exception as err:
        print('Logging failed with this error:', str(err))
    return render_template('viewlog.html',
                           the_title=title,
                           row_titles=row_titles,
                           the_name=name,
                           the_data=data,
                           the_results=result,
                           the_comment=comment)


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()

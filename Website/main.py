import flask  
from flask import Flask, render_template, request, redirect, request
from flask.helpers import url_for
import tabulate
import openfile


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/search', methods = ["GET", "POST"])
def years():
    if request.method == 'POST':
        day = request.form.get('day')
        month = request.form.get('month')
        year = request.form.get('year')

        return redirect(url_for('graph', day=day, month=month, year=year))

    else:
        return render_template('search.html')

@app.route('/graph')
def graph():
    
    day=request.args.get('day')
    month=request.args.get('month')
    year=request.args.get('year')

    try:
        if len(year)>2:
            year=str(year)[-2:]
        if len(month)<2:
            month = str(f'0{month}')
        if len(day)<2:
            day = str(f'0{day}')

        file=str(f'{day}.{month}.{year}.csv')
        file = openfile.openfile(file)
    
        return render_template('graph.html', day=day, month=month, year=year, file=file)

    except:
        return redirect(url_for('years'))


if __name__== ("__main__"):
    app.run(debug=True)
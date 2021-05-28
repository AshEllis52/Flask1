#Flask imports
from flask import Flask, render_template, send_file, make_response, url_for, Response
from flask import request
from flask_cors import CORS
import json
import pypyodbc
app = Flask(__name__)
CORS(app)


#Pandas and Matplotlib
import pandas as pd
from pandas import DataFrame
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader.data as web

#other requirements
import io

with open(".pw") as f:
  password = f.read()

conn2 = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=ashdb.dbsprojects.ie;'
'Database=Stocks;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD='+password,autocommit = True)

cur = conn2.cursor()

#Data imports

cur.execute('''Select * FROM AAPL''')
rv = cur.fetchall()

cur.execute('''Select * FROM TSLA''')
rv1 = cur.fetchall()

cur.execute('''Select * FROM BA''')
rv2 = cur.fetchall()


rv = DataFrame (rv,columns= ['Date','Open','Close','Low','Close','Adj Close', 'Volume'])
rv1 = DataFrame (rv1,columns= ['Date','Open','Close','Low','Close','Adj Close', 'Volume'])
rv2 = DataFrame (rv2,columns= ['Date','Open','Close','Low','Close','Adj Close', 'Volume'])

start = dt.datetime(2020, 5, 20)
end = dt.datetime(2021,5,20)

df = web.DataReader('TSLA', 'yahoo', start, end)
df1 = web.DataReader('AAPL', 'yahoo', start, end)
df2 = web.DataReader('BA', 'yahoo', start, end)

df.to_csv('tsla.csv')
df1.to_csv('aapl.csv')
df2.to_csv('ba.csv')

#from GetFixtres import ECS_data
#ECS_data = df
#from GetFixtures2 import GK_roi
#GK_roi = df1


#Pandas Page
@app.route('/')
@app.route('/tsla', methods=("POST", "GET"))
def tsla():
    return render_template('pandas.html',
                           PageTitle = "Pandas",
                           table=[rv.to_html(classes='data', index = False)], titles= rv.columns.values)
 
@app.route('/aapl', methods=("POST", "GET"))
def aapl():
    return render_template('pandas.html',
                           PageTitle = "Pandas",
                           table=[rv1.to_html(classes='data', index = False)], titles= rv1.columns.values)
 
@app.route('/ba', methods=("POST", "GET"))
def ba():
    return render_template('pandas.html',
                           PageTitle = "Pandas",
                           table=[rv2.to_html(classes='data', index = False)], titles= rv2.columns.values)

#Matplotlib page
@app.route('/plot/tsla', methods=("POST", "GET"))
def plot_tsla():
    return render_template('matplot.html',
                           PageTitle = "Matplotlib")


@app.route('/plot.png/tsla')
def plot_png():
    fig = create_figure_tsla()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
  
@app.route('/plot.png/aapl')
def plot_png_tsla():
    fig = create_figure_aapl()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
  
@app.route('/plot.png/ba')
def plot_png_aapl():
    fig = create_figure_ba()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure_tsla():
    fig, ax = plt.subplots(figsize = (6,4))
    fig.patch.set_facecolor('#E8E5DA')

    x = df.Close
    y = df.Open

    ax.bar(x, y, color = "#304C89")

    plt.xticks(rotation = 30, size = 5)
    plt.ylabel("Open", size = 5)

    return fig

def create_figure_aapl():
    fig, ax = plt.subplots(figsize = (6,4))
    fig.patch.set_facecolor('#E8E5DA')

    x = df1.Close
    y = df1.Open

    ax.bar(x, y, color = "#304C89")

    plt.xticks(rotation = 30, size = 5)
    plt.ylabel("Open", size = 5)

    return fig
  
def create_figure_ba():
    fig, ax = plt.subplots(figsize = (6,4))
    fig.patch.set_facecolor('#E8E5DA')

    x = df2.Close
    y = df2.Open

    ax.bar(x, y, color = "#304C89")

    plt.xticks(rotation = 30, size = 5)
    plt.ylabel("Open", size = 5)

    return fig



if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem'))

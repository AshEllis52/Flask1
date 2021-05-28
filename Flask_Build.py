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

cur = conn2.cursor()
cur.execute('''Select * FROM AAPL''')
rv = cur.fetchall()

cur.execute('''Select * FROM TSLA''')
rv1 = cur.fetchall()

#start = dt.datetime(2020, 1, 1)
#end = dt.datetime(2021,12,31)

#df = web.DataReader('TSLA', 'yahoo', start, end)
#df1 = web.DataReader('AAPL', 'yahoo', start, end)


rv = DataFrame (rv,columns= ['Date','Open','Close','Low','Close','Adj Close', 'Volume'])
#rv = df
rv1 = DataFrame (rv1,columns= ['Date','Open','Close','Low','Close','Adj Close', 'Volume'])
#rv = df1

rv.to_csv('tsla.csv')
rv1.to_csv('aapl.csv')

#from GetFixtres import ECS_data
#ECS_data = rv
#from GetFixtures2 import GK_roi
#GK_roi = rv1


#Pandas Page
@app.route('/')
@app.route('/pandas', methods=("POST", "GET"))
def GK():
    return render_template('pandas.html',
                           PageTitle = "Pandas",
                           table=[rv1.to_html(classes='data', index = False)], titles= rv1.columns.values)


#Matplotlib page
@app.route('/matplot', methods=("POST", "GET"))
def mpl():
    return render_template('matplot.html',
                           PageTitle = "Matplotlib")


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig, ax = plt.subplots(figsize = (6,4))
    fig.patch.set_facecolor('#E8E5DA')

    x = rv.Open
    y = rv.Close

    ax.bar(x, y, color = "#304C89")

    plt.xticks(rotation = 30, size = 5)
    plt.ylabel("Expected Clean Sheets", size = 5)

    return fig




if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) 

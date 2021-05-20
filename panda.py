from flask import Flask
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web



app = Flask(__name__)
@app.route("/")
def graphs():
 style.use('ggplot') 
 start = dt.datetime(200,1,1)
 end = dt.datetime(2016,12,31)
 
 df = web.DataReader('TSLA', 'yahoo', start, end)

 return print(df.head())

if __name__ == "__main__":
 app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080


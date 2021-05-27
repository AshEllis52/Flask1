from flask import Flask
from flask import request
from flask_cors import CORS
import json
import numpy as np
import matplotlib.pyplot as plt, mpld3
import pypyodbc
app = Flask(__name__)
CORS(app)

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

@app.route("/")#URL leading to method
def Graph():
 np.random.seed(4500)

 mean = 150
 sd = 10
 n = 1000

 heights = np.random.normal(mean, sd, n)

 density = False

 hist, bin_edges = np.histogram(heights, bins=50, density = density)

 bin_width = bin_edges[2] - bin_edges[1]
 print("Bin Width =", bin_width)

 plt.figure()
 plt.plot(bin_edges[:-1], hist, color="green", label="heights histogram")
 plt.xlabel("Height")
 plt.ylabel("Frequency")
 plt.grid()
 plt.legend()
 plt.title("Histogram/Density Functions of heights of college students")
 x = plt.show()
 return(x)

@app.route("/aapl") #add
 plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
  mpld3.show()
  
@app.route("/tsla") #add
def tsla():
 cur = conn2.cursor()
 cur.execute('''Select * FROM TSLA''')
 rv = cur.fetchall()
 Results = []
 for row in rv:
  Results = {}
  Results['Date'] = row[0].replace('\n',' ')
  Results['Open'] = row[1]
  Results['High'] = row[2]
  Results['Low'] = row[3]
  Results['Close'] = row[4]
  Results['Adj Close'] = row[5]
  Results['Volume'] = row[6]
  #Results.append(Result)
 response={'Results':Results, 'count':len(Results)}
 ret=app.response_class(
  response=json.dumps(response),
  status=200,
  mimetype='application/json'
 )
 return ret
if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem'))

from flask import Flask
from flask import request
from flask_cors import CORS
import json
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
def hello(): # Name of the method
 return("Hello World!")

@app.route("/aapl") #add
def aapl():
 cur = conn2.cursor()
 cur.execute('''Select * FROM AAPL''')
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
  #Results['Volume'] = row[6]
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

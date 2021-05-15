from flask import Flask
from flask import request


import plotly.express as px

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

my_plot_div  = fig.to_html(full_html=False) 

app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!")
@app.route("/greetme")#different URL
def helloall(): # different method name
 name = request.args.get('name')#retrieve GET parameters
 return("Hello {}!".format(name))#Python’s string.format
if __name__ == "__main__":
 app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080

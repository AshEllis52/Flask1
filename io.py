from flask import Flask
from flask import request
from flask_cors import CORS
import json
import pypyodbc
app = Flask(__name__)
CORS(app)
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
import cgi
from io import BytesIO

@app.route("/") 
def png():
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
    plt.show()
    fig = plt.figure()
    #plt.plot(range(10))
    figdata = BytesIO()
    fig.savefig(figdata, format='png')


    imgStr = "data:image/png;base64,"

    imgStr += base64.b64encode(figdata)
    
    return 

    print ("Content-type: text/html\n")
    print ("""<html><body>)
     Ash
           <img src="%s"></img>
     Ash
                </body></html>
     """ % imgStr

if __name__ == "__main__"
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) 

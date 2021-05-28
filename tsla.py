from flask import Flask
from flask import request
from flask_cors import CORS
import json
import pypyodbc
app = Flask(__name__)
CORS(app)
import matplotlib.pyplot as pyplot
from io import BytesIO
import numpy as np1


@app.route("/")#URL leading to method
np.random.seed(4500)

mean = 150
sd = 10
n = 1000

heights = np1.random.normal(mean, sd, n)

density = False

hist, bin_edges = np1.histogram(heights, bins=50, density = density)

bin_width = bin_edges[2] - bin_edges[1]
print("Bin Width =", bin_width)

pyplot.figure()
pyplot.plot(bin_edges[:-1], hist, color="green", label="heights histogram")
pyplot.xlabel("Height")
pyplot.ylabel("Frequency")
pyplot.grid()
pyplot.legend()
pyplot.title("Histogram/Density Functions of heights of college students")
pyplot.show()

format = "png"
sio = BytesIO()
pyplot.savefig(sio, format=format)
print ("Content-Type: image/%s\n" % format)
#msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY) # Needed this on windows, IIS
sys.stdout.write(sio.getvalue())


if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) 

import io
from matplotlib.figure import Figure     
from matplotlib import pyplot as plt                 

fig = Figure(figsize=[4,4])                               
ax = fig.add_axes([.1,.1,.8,.8])                          
ax.scatter([1,2], [3,4])                                  

buf = io.BytesIO()
fig.savefig(buf, format='png')
plt.close(fig)
data=buf.getvalue()

# In my case I would have used Django for the webpage
response = HttpResponse(data, content_type='image/png')
 return response

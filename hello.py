from flask import Flask
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
	return("Hello World!") #indent this line
if __name__ == "__main__":
	app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080

	import json 
string_with_json_obj = '' 
# Find data for teams 
for el in scripts: 
    if 'teamsData' in el.text: 
        string_with_json_obj = el.text.strip()
# print(string_with_json_obj)
# strip unnecessary symbols and get only JSON data 
ind_start = string_with_json_obj.index("('")+2 
ind_end = string_with_json_obj.index("')") 
json_data = string_with_json_obj[ind_start:ind_end] 
json_data = json_data.encode('utf8').decode('unicode_escape')

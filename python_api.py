from flask import *
import json, time
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = '10.128.8.5'
app.config['MYSQL_USER'] = 'original'
app.config['MYSQL_PASSWORD'] = 'Original@123'
app.config['MYSQL_DB'] = 'python_api_db'

mysql = MySQL(app)

@app.route('/',methods=['GET'])
def home_page():
	data = {'page':'Home', 'output':'Hi, You are in home page!. Give the enter your name through URL'}
	json_data = json.dumps(data)
	return json_data

@app.route('/user/', methods=['GET'])
def request_pop():
	user_name = str(request.args.get('user'))
	data = {'page':'Output Page', 'output': 'Hi,{} say Leni'.format(user_name)} 
	json_data = json.dumps(data)
	
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO api_data (name, data) VALUES (%s,%s)",(user_name, data['output']))
	mysql.connection.commit()
	cur.close()

	return json_data

if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)


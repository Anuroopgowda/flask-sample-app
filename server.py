from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
from yaml import load

app = Flask(__name__)

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def myform():
    return render_template('new2.html')

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        college = userDetails['college']
        begin = userDetails['begin']
        end = userDetails['end']
        project = userDetails['project']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO internship(name, college, begin, end, project) VALUES(%s, %s, %s, %s, %s)', (name, college, begin, end, project))
        mysql.connection.commit()
        cur.close()

    return render_template('new2.html')



if __name__ == '__main__':
    app.run(debug=True)

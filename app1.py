from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flsk'


mysql = MySQL(app)


@app.route('/',methods=['GET', 'POST'] )
def Home():

    if request.method == 'POST':
        name = request.form['name']
        pid = request.form['patientid']
        risk=request.form['risk']
        disease=request.form['disease']
        cur = mysql.connection.cursor()
        cur.execute("update patients Set pname=%s where pid=%s",(name,pid))
        mysql.connection.commit()
        cur.close()
        return ("success")           
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)








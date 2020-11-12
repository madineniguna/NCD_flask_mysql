from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flsk'
db = SQLAlchemy(app)


class Patients(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    pid = db.Column(db.String(20), primary_key=True)
    pname = db.Column(db.String(100), nullable=False)
    risk = db.Column(db.Integer, nullable=False)
    Disease = db.Column(db.String(120), nullable=False)
   




@app.route("/index/<int:pid>", methods = ['GET', 'POST'])
def index():
    if(request.method=='POST'):
        '''Add entry to the database'''
        pid = request.form.get('patientid')

        
        name = request.form.get('name')
        risk = request.form.get('risk')
        disease = request.form.get('disease')
        entry = Patients(pname = name, risk = risk, Disease = disease  )
        try:
        	db.session.query.filter_by(pid==pid)
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html')


app.run(debug=True)
from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route('/profile/')
def profile():
    return jsonify({'name':'Jimit',
                    'address':'India'})

@app.route('/appointments/')
def appointmentList():
    return jsonify([{'name':'Jimit',
                    'address':'India'},
                    {'name':'Jhon',
                    'address':'Chile'}])

#pip install flask
#export FLASK_APP=backend.py
#flask run
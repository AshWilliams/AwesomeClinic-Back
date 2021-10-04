from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route('/profile/')
def profile():
    return jsonify({'name':'Robert Rozas Navarro',
                    'phone':'+56 9 5811 9900',
                    'address':'Middle of Nowhere, Chile',
                    'member_since':'July 2012'})

@app.route('/appointments/')
def appointmentList():
    return jsonify([{'date':'10/10/2021',
                     'doctor':'Sergio Palma',
                     'specialty':'Gastroenterólogo',
                     'branch_address':'Las Condes'},
                    {'date':'23/10/2021',
                     'doctor':'Juan Soto',
                     'specialty':'Medicina General',
                     'branch_address':'Nuñoa'},
                    {'date':'10/11/2021',
                     'doctor':'Emilia Albuquerque',
                     'specialty':'Oftalmologo',
                     'branch_address':'Tobalaba'},
                    {'date':'28/11/2021',
                     'doctor':'Pedro Chandía',
                     'specialty':'Dentista',
                     'branch_address':'Las Condes'}])

#pip install flask
#export FLASK_APP=backend.py
#flask run
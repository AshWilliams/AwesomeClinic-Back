from flask import jsonify,Flask
from flask_cors import CORS, cross_origin
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/profile/')
@cross_origin()
def profile():
    """Example endpoint returning a luser profile
    This is using docstrings for specifications.
    ---
    parameters:
      - name: none
        in: path
        required: false
    definitions:
      profile:
        type: json object
        properties:
          name:
            type: string  
    responses:
      200:
        description: A user profile        
        examples:
                    {'name':'Robert Rozas Navarro',
                    'phone':'+56 9 5811 9900',
                    'email':'robert.rozas.n@gmail.com',
                    'address':'Middle of Nowhere, Chile',
                    'org':'Pycon Chile 2021',
                    'member_since':'July 2012'}
    """
    return jsonify({'name':'Robert Rozas Navarro',
                    'phone':'+56 9 5811 9900',
                    'email':'robert.rozas.n@gmail.com',
                    'address':'Middle of Nowhere, Chile',
                    'org':'Pycon Chile 2021',
                    'member_since':'July 2012'})

@app.route('/appointments/')
@cross_origin()
def appointmentList():
    return jsonify([{'date':'10/10/2021',
                     'doctor':'Sergio Palma',
                     'specialty':'Gastroenterologo',
                     'branch_address':'Las Condes'},
                    {'date':'23/10/2021',
                     'doctor':'Juan Soto',
                     'specialty':'Medicina General',
                     'branch_address':'Escuela Militar'},
                    {'date':'10/11/2021',
                     'doctor':'Emilia Albuquerque',
                     'specialty':'Oftalmologo',
                     'branch_address':'Tobalaba'},
                    {'date':'28/11/2021',
                     'doctor':'Pedro Chandia',
                     'specialty':'Dentista',
                     'branch_address':'Las Condes'}])

#pip install flask
#export FLASK_APP=backend.py
#flask run
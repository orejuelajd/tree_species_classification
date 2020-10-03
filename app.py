import flask
from flask import Flask, jsonify, request
import json
import pickle
from flask_cors import CORS, cross_origin
from pickle import load
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/hello', methods=['GET'])
@cross_origin()
def hello():
    print("hola")
    response = json.dumps({'response': 'yahhhh!'})
    return response, 200

# Time to add our machine learning model. Grab your model_file.p pickle and drop it into the /models/ directory in the
# app we made so your file tree now looks like the left.
def load_models():
    file_name = "resources/models/model_rfc_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

def load_scaler():
    scaler = load(open('resources/models/stardardscaler.pkl', 'rb'))
    return scaler

def load_transformer():
    transformer = load(open('resources/models/pcamodel.pkl', 'rb'))
    return transformer

def get_specie(number_specie):
    species = {0:'Palma real de Cuba',
               1:'Limon swinglea, Swinglea',
               2: 'Palma areca'
               }
    return species.get(number_specie, "Especie Inválida")

@app.route('/predict_get', methods=['GET'])
@cross_origin()
def predict_get():
    request_json = request.get_json()

    pb = float(request_json['pb'])
    pap = float(request_json['pap'])
    dap = float(request_json['dap'])
    dap2 = float(request_json['dap2'])
    papdel = float(request_json['papdel'])
    papgrueso = float(request_json['papgrueso'])
    altura_fuste = float(request_json['altura_fuste'])
    altura_arbol = float(request_json['altura_arbol'])
    diferencia = float(request_json['diferencia'])
    diametro_copa = float(request_json['diametro_copa'])
    tallos = float(request_json['tallos'])
    veg_Palma = float(request_json['veg_Palma'])
    veg_Arbol = float(request_json['veg_Arbol'])

    # load model
    model = load_models()

    prediction = model.predict([[pb, pap, dap, dap2, papdel, papgrueso, altura_fuste,
                                 altura_arbol, diferencia, diametro_copa, tallos, veg_Palma, veg_Arbol]])[0]

    response = json.dumps({'response': get_specie(int(prediction))})
    return response, 200

@app.route('/predict_post', methods=['POST'])
@cross_origin()
def predict_post():
    request_data = request.get_json()
    pb = float(request_data['pb'])
    pap = float(request_data['pap'])
    dap = float(request_data['dap'])
    papdel = float(request_data['papdel'])
    papgrueso = float(request_data['papgrueso'])
    altura_fuste = float(request_data['altura_fuste'])
    altura_arbol = float(request_data['altura_arbol'])
    diferencia = float(request_data['diferencia'])
    diametro_copa = float(request_data['diametro_copa'])
    tallos = float(request_data['tallos'])
    veg_Palma = float(request_data['veg_Palma'])
    veg_Arbol = float(request_data['veg_Arbol'])

    # load model
    model = load_models()
    scaler = load_scaler()
    transformer = load_transformer()

    data = [[pb, pap, dap, papdel, papgrueso, altura_fuste,
            altura_arbol, diferencia, diametro_copa, tallos, veg_Palma, veg_Arbol]]
    data = scaler.transform(data)
    data = transformer.transform(data)

    prediction = model.predict(data)[0]
    response = json.dumps({'response': get_specie(int(prediction))})
    return response, 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
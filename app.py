import flask
from flask import Flask, jsonify, request
import json
import pickle

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    response = json.dumps({'response': 'yahhhh!'})
    return response, 200

def load_models():
    file_name = "resources/models/model_rfc_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

@app.route('/predict', methods=['GET'])
def predict():
    # stub input features
    # x = 5.963
    # parse input features from request
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

    # prediction = model.predict([[2.56, 0, 0.08, 0.08, 0.21, 0.28, 5.5, 7.3, 1.8, 4.8, 6, 1, 0]])[0]

    print(prediction)
    response = json.dumps({'response': int(prediction)})
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
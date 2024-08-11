import pickle
from flask import Flask, request, jsonify

app = Flask("Phone-Price-Prediction")

# Linear Regression Model...
with open('model.pkl', 'rb') as x:
    model1 = pickle.load(x)

# Random Forest Model...
with open('RMmodel.pkl', 'rb') as y:
    model2 = pickle.load(y)


@app.route('/')
def home():
    return "Hello, Bachhoooooooooooonnnnn to kaise ho aap log"


@app.route('/linear', methods=['POST'])
def predict_linear():
    data = request.get_json()
    features = data['features']
    prediction = model1.predict([features])
    return jsonify({'prediction': prediction[0]})

@app.route('/random', methods=['POST'])
def predict_random():
    data = request.get_json()
    features = data['features']
    prediction = model2.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask , request, jsonify
from predict import predict_image
from flask_cors import CORS
import filetype


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello world'



@app.route('/predict' , methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'Error': 'No file'}), 400
    
    file = request.files['file']


    kind = filetype.guess(file)
    print(kind.extension)

    if kind.extension not in ['jpg', 'png' , 'jpeg']:
        return jsonify({'Error': 'Formato Invalido: jpg, jpeg, png'}), 400

    file.save('test.jpg')
    result = predict_image('test.jpg')
    return jsonify({'Prediction': result})







#Por alguna razon que no entiendo esto tiene que ir al final lol
if __name__ == '__main__':
    app.run(debug=True)






from flask import Flask, request, render_template
import pickle
import numpy as np
model = pickle.load(open('predict.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/predict', methods=['POST'])
def predict_crops():
    temp = float(request.form['temp'])
    humidity = float(request.form['hum'])
    ph = float(request.form['ph'])
    wa = float(request.form['wa'])
    season = int(request.form['season'])
        # data = [[temp, humidity, ph, wa, season]]
        # print(data)
        # prediction
    result = model.predict(np.array([temp, humidity, ph, wa, season]).reshape(1,5))
    if result[0] == 0:
        result = 'Rice'
    elif result[0] == 1:
        result = 'Maize'
    elif result[0] == 2:
        result = 'Chickpea'
    elif result[0] == 3:
        result = 'Kidney Beans'
    elif result[0] == 4:
        result = 'Pigeon pea'
    elif result[0] == 5:
        result = 'Moth Beans'
    elif result[0] == 6:
        result = 'Mung Beans'
    elif result[0] == 7:
        result = 'Black Gram'
    elif result[0] == 8:
        result = 'Lentil'
    elif result[0] == 9:
        result = 'watermelon'
    elif result[0] == 10:
        result = 'Muskmelon'
    elif result[0] == 11:
        result = 'Cotton'
    elif result[0] == 12:
        result = 'Jute'     
    return render_template('test.html', result='The Best Crop For Your Land Is {}'.format(result))

if __name__ == '__main__':
    app.run(debug=True)
    
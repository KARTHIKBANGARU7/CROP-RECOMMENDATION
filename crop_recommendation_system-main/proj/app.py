from flask import Flask, render_template, request
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
scaler=StandardScaler()

model = joblib.load("A:\OneDrive\Desktop\crop recomendation\crop_recommendation_system-main\Crop Recommendation.pkl")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = request.form.to_dict()
        input_data_array = [float(input_data['N']), float(input_data['P']), float(input_data['K']),
                            float(input_data['temperature']), float(input_data['humidity']),
                            float(input_data['ph']), float(input_data['rainfall'])]

        # Reshape the array
        reshaped_data = np.asarray(input_data_array).reshape(1, -1)

        # Standardize the data
        reshaped_data_transformed = scaler.fit_transform(reshaped_data)

        # Make prediction
        prediction = model.predict(reshaped_data_transformed)

        return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)

 # Crop Recommendation System
The Crop Recommendation System is a machine learning application designed to assist farmers in selecting suitable crops based on agricultural parameters. By leveraging historical data and predictive models, the system aims to optimize crop yield and enhance agricultural decision-making.

# Features
- Predictive Modeling: Utilizes machine learning algorithms, including Random Forest Classifier, Logistic Regression, Support Vector Machine (SVM), and K-Nearest Neighbors (KNN), to predict the most suitable crops based on input parameters.

- High Accuracy: Achieves 99.39% accuracy with the Random Forest Classifier, ensuring reliable recommendations.

- User-Friendly Interface: Implements a web interface using Flask, allowing farmers to easily input their agricultural data and receive instant crop recommendations.

# Tech Stack
- Python: Primary programming language for data analysis, model development, and web application scripting.
- Scikit-learn: Machine learning library for building and evaluating predictive models using algorithms such as Random Forest Classifier, Logistic Regression, SVM, and KNN.
- Flask: Micro-framework for web application development, enabling rapid deployment and scalability.
- Pandas and NumPy: Data manipulation and numerical computation libraries in Python.
- Matplotlib and Seaborn: Visualization tools for displaying data distributions and model performance metrics.

# Installation
Clone the repository:


```
git clone https://github.com/your_username/crop-recommendation.git
cd crop-recommendation
```
Install dependencies:
```
pip install -r requirements.txt
```
# Usage
Start the Flask application:
```
python app.py
```
# Access the application:

- Open a web browser and go to http://localhost:5000.
- Enter agricultural parameters (Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, rainfall) into the web form.
- Submit the form to receive crop recommendations based on the input data.
# Project Structure
php
```
crop-recommendation/
│
├── app.py                 # Main Flask application script
├── static/
│   └── css/
│       └── style.css      # CSS styles for web interface
├── templates/
│   ├── index.html         # HTML template for web interface
│   └── base.html          # Base HTML template
├── data/
│   └── Crop_recommendation.csv  # Dataset used for training and testing
├── README.md              # Detailed project overview and instructions
└── requirements.txt       # Python dependencies
```
# Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue to discuss them before submitting a pull request.

from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("House_Price_Prediction.pkl", "rb"))



@app.route("/")
@cross_origin()
def index():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        house_area = int(request.form["House_Area"])
         
        house_bedrooms = int(request.form["House_Bedrooms"])
        house_age = int(request.form["House_Age"])
        
        prediction=model.predict([[ house_area, house_bedrooms, house_age ]])

        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Your House price is Rs. {}".format(output))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

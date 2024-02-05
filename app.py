from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score

app = Flask(__name__)

# Load and preprocess data
matches = pd.read_csv("C:/Users/ü/Desktop/Project2/matches.csv", index_col=0)
matches["date"] = pd.to_datetime(matches["date"])
matches["target"] = (matches["result"] == "W").astype(int)
matches["venue_code"] = matches["venue"].astype("category").cat.codes
matches["opp_code"] = matches["opponent"].astype("category").cat.codes
matches["hour"] = matches["time"].str.replace(":.+", "", regex=True).astype(int)
matches["day_code"] = matches["date"].dt.dayofweek
matches.drop(columns=["comp", "notes"], inplace=True)

# Define the model
rf = RandomForestClassifier(n_estimators=50, min_samples_split=10, random_state=1)
predictors = ["venue_code", "opp_code", "hour", "day_code"]

# Train the model
train = matches[matches["date"] < '2022-01-01']
test = matches[matches["date"] >= '2022-01-01']
rf.fit(train[predictors], train["target"])

# Function to make predictions with the model
def make_predictions(input_data):
    input_df = pd.DataFrame([input_data])
    
    # Transform input_df to match the model's expectation
    # Convert date and time
    input_df["date"] = pd.to_datetime(input_df["date"])
    input_df["hour"] = input_df["time"].str.replace(":.+", "", regex=True).astype(int)
    input_df["day_code"] = input_df["date"].dt.dayofweek

    # Encode categorical variables
    input_df["venue_code"] = input_df["venue"].astype("category").cat.codes
    input_df["opp_code"] = input_df["opponent"].astype("category").cat.codes

    # Drop columns not used by the model
    input_df = input_df[predictors]

    # Make a prediction
    preds = rf.predict(input_df)
    return preds


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get data sent from the frontend
    preds = make_predictions(data)  # Get prediction
    return jsonify({'prediction': preds.tolist()})  # Send prediction back as JSON

if __name__ == '__main__':
    app.run(debug=True)
#if __name__ == '__main__':
    app.run(debug=True, port=8080)


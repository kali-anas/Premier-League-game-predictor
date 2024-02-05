import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score

# Load the data
matches = pd.read_csv("C:/Users/ü/Desktop/Project2/matches.csv", index_col=0)

# Preprocess the data
matches["date"] = pd.to_datetime(matches["date"])
matches["target"] = (matches["result"] == "W").astype(int)
matches["venue_code"] = matches["venue"].astype("category").cat.codes
matches["opp_code"] = matches["opponent"].astype("category").cat.codes
matches["hour"] = matches["time"].str.replace(":.+", "", regex=True).astype(int)
matches["day_code"] = matches["date"].dt.dayofweek
matches.drop(columns=["comp", "notes"], inplace=True)

# Train the Random Forest model
rf = RandomForestClassifier(n_estimators=50, min_samples_split=10, random_state=1)
train = matches[matches["date"] < '2022-01-01']
test = matches[matches["date"] >= '2022-01-01']
predictors = ["venue_code", "opp_code", "hour", "day_code"]
rf.fit(train[predictors], train["target"])
preds = rf.predict(test[predictors])

# Evaluate the model
accuracy = accuracy_score(test["target"], preds)
print(f'Accuracy: {accuracy}')

# Function to calculate rolling averages for given columns
def rolling_averages(group, cols):
    new_cols = [f"{c}_rolling" for c in cols]
    group = group.sort_values("date")
    rolling_stats = group[cols].rolling(3, closed='left').mean()
    group[new_cols] = rolling_stats
    group.dropna(subset=new_cols, inplace=True)
    return group

# Calculate rolling averages
cols = ["gf", "ga", "sh", "sot", "dist", "fk", "pk", "pkatt"]
matches_rolling = matches.groupby("team").apply(rolling_averages, cols=cols)
matches_rolling.reset_index(drop=True, inplace=True)

# Function to make predictions with the model
def make_predictions(data, predictors):
    train = data[data["date"] < '2022-01-01']
    test = data[data["date"] >= '2022-01-01']
    rf.fit(train[predictors], train["target"])
    preds = rf.predict(test[predictors])
    combined = pd.DataFrame(dict(actual=test["target"], predicted=preds), index=test.index)
    precision = precision_score(test["target"], preds)
    return combined, precision

# Make predictions with new features
new_cols = [f"{c}_rolling" for c in cols]
combined, precision = make_predictions(matches_rolling, predictors + new_cols)
print(f'Precision: {precision}')

# Merge predictions with the original data for analysis
combined = combined.merge(matches_rolling[["date", "team", "opponent", "result"]], left_index=True, right_index=True)

# Define the mapping (placeholder - replace with your actual mapping)
mapping = {
    'Old Team Name 1': 'New Team Name 1',
    'Old Team Name 2': 'New Team Name 2',
}

combined["new_team"] = combined["team"].map(mapping)

# Merge and analyze predictions
merged = combined.merge(combined, left_on=["date", "new_team"], right_on=["date", "opponent"])
results = merged[(merged["predicted_x"] == 1) & (merged["predicted_y"] == 0)]["actual_x"].value_counts()
print(results)



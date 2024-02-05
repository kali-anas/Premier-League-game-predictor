# Premier League Match Predictor

![Premier League Match Predictor](preview.png)

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [How it Works](#how-it-works)
- [Usage](#usage)
- [Contributions](#contributions)
- [Author](#author)
- [License](#license)

## Overview

The Premier League Match Predictor is a full-stack machine learning project developed to predict the outcomes of football matches in the English Premier League. Using data from the 2021-2022 season, this project creates predictors and trains a machine learning model to forecast the winner of each match. The primary goal is to accurately predict match results and continually improve prediction accuracy.

## Project Structure

The project consists of multiple components:

- **HTML and CSS:** The user interface is designed using HTML and CSS. It allows users to input match details and receive predictions.

- **Python Scripts:** Python scripts are used for data preprocessing, machine learning model training, and making predictions.

- **Flask Backend:** The project includes a Flask web application that serves as the backend. It exposes an endpoint for receiving match details and returning predictions.

## How it Works

### Data Collection and Preprocessing

- Data for the 2021-2022 Premier League season is collected and preprocessed. Features such as venue, opponent, time, and result are extracted and used for training.

- The data is transformed to prepare it for machine learning, including encoding categorical variables and creating new features.

### Machine Learning Model

- A machine learning model, based on a RandomForestClassifier, is trained using the preprocessed data. It learns to predict match outcomes (win or loss) based on various features.

- The model is trained on historical data, and its accuracy is evaluated using metrics such as accuracy and precision.

### Web Interface

- The user interacts with the project through a web interface. Users input match details (venue, opponent, time), and the data is sent to the Flask backend for prediction.

- The backend processes the input data, makes predictions using the trained model, and sends the predictions back to the user interface.

## Usage

To use the Premier League Match Predictor:

1. Clone the repository to your local machine.

2. Ensure you have Python and the required libraries (pandas, scikit-learn, Flask) installed.

3. Run the Flask web application (`app.py`) to start the backend.

4. Open the HTML interface in a web browser, input match details, and receive predictions.

Feel free to explore the code, make improvements, and use it to predict Premier League match outcomes.


## License

This project is open-source and available under the [MIT License](LICENSE). You are welcome to use, modify, and distribute it for both personal and commercial purposes while adhering to the license terms.


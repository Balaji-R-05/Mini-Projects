# House Price Prediction using Linear Regression

This project aims to predict house prices based on the area of the house using a Linear Regression model. The dataset consists of house areas and their corresponding prices. The model is trained to find the best fit line that can be used to make predictions for new data points.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Visualization](#visualization)
- [Theory](#theory)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Linear Regression is a simple yet powerful algorithm used for predictive modeling. This project uses Linear Regression to predict house prices based on the area of the house.

## Dataset
The dataset used in this project contains two columns:
- `area`: The area of the house in square feet.
- `price`: The price of the house.

Make sure your dataset is named `dataset.csv` and located in the same directory as your script.

## Installation
To run this project, you'll need to have Python and the following libraries installed:
- pandas
- matplotlib
- scikit-learn

You can install these libraries using pip:

```bash
pip install pandas matplotlib scikit-learn
```
## Usage
- Clone the repository or download the script to your local machine.
- Place the dataset.csv file in the same directory as your script.
- Run the script:

```bash
python house_price_prediction.py
```
- Enter the land area in square feet when prompted to get the predicted house price.

## Visualization
The script visualizes the dataset and the best fit line:

- Scatter Plot: Displays the relationship between house area and price.
- Best Fit Line: Shows the line that best represents the data according to the Linear Regression model.

## Theory
The Linear Regression model predicts house prices using the equation:

𝑌 = 𝑚*𝑋 + b

Where:

- Y is the predicted price.
- X is the input area.
- 𝑚 is the coefficient (slope).
- b is the intercept.

## Results
The script will output:

The predicted price for the given land area.
The coefficient and intercept of the trained model.
The price calculated using the theoretical formula.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.

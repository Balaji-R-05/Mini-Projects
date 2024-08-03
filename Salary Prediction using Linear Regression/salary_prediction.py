# Salary Prediction using Linear Regression

# Importing necessary libraries and modules
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
dataset = pd.read_csv("data.csv")

# Display the first few rows of the dataset for a quick look
print("Dataset preview:")
print(dataset.head())

# Visualize the dataset
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Salary vs Level")
plt.scatter(dataset.Level, dataset.Salary, color="red", marker="*")

# Segregate data into input X and output Y
X = dataset[['Level']]  # Input feature (Level)
Y = dataset['Salary']  # Output variable (Salary)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X, Y)

# Plot the best fit line
plt.plot(X, model.predict(X), color='blue', linewidth=2)
plt.show()

# Predict the salary for a given level
x = int(input("Enter level: "))
LevelResult = [[x]]
PredictedmodelResult = model.predict(LevelResult)
print(f"Predicted Salary for Level {x} is: {PredictedmodelResult[0]}")

# Theory Calculation: Y = m * X + b (m is coefficient and b is intercept)

# Coefficient (m)
m = model.coef_[0]
print(f"Coefficient (m): {m}")

# Intercept (b)
b = model.intercept_
print(f"Intercept (b): {b}")

# Calculate the predicted salary using the formula Y = mX + b
y = m * x + b
print(f"The Salary of Level {x} is: {y}")

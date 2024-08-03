# House Price Prediction using Linear Regression

# Importing necessary modules
import pandas as pd  # For data manipulation and analysis.
import matplotlib.pyplot as plt  # For data visualization.
from sklearn.linear_model import LinearRegression  # For building and training the linear regression model.

# Load Dataset
dataset = pd.read_csv("dataset.csv")

# Uncomment the lines below to inspect the dataset
# print(dataset.shape)  # Prints the number of rows and columns in the dataset.
# print(dataset.head(5))  # Prints the first 5 rows of the dataset.

# Visualize dataset
plt.xlabel("Area")
plt.ylabel("Price")
plt.scatter(dataset['area'], dataset['price'], color="red", marker="*")

# Segregate data into input X and output Y
X = dataset[['area']]  # Input feature (area)
Y = dataset['price']  # Output variable (price)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X, Y)

# Plot the best fit line
plt.plot(X, model.predict(X), color='blue', linewidth=2)
plt.show()

# Predict the price for a given land area
x = int(input("Enter the land area in square feet: "))
LandAreainSqFt = [[x]]
PredictedmodelResult = model.predict(LandAreainSqFt)
print(f"Predicted Price for {x} square feet land is: {PredictedmodelResult[0]}")

# Theory Calculation: Y = m * X + b (m is coefficient and b is intercept)

# Coefficient (m)
m = model.coef_
print(f"Coefficient (m): {m[0]}")

# Intercept (b)
b = model.intercept_
print(f"Intercept (b): {b}")

# Calculate the predicted price using the formula Y = mx + b
y = m * x + b
print(f"The Price of {x} Square feet Land is: {y[0]}")

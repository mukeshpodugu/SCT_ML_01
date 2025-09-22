# 🏡 House Price Prediction Using Linear Regression

This project is a simple machine learning model that predicts **house prices** based on their **area (square feet)** using **Linear Regression**.

## 📂 Dataset

The dataset contains two columns:  

- `Area` (in square feet)  
- `Price` (in currency, e.g., USD or INR)  

Example:

| Area (sqft) | Price |
|-------------|-------|
| 1000        | 150000 |
| 1500        | 200000 |
| 2000        | 250000 |

## ⚙️ Technologies Used

- Python  
- pandas  
- NumPy  
- scikit-learn  
- Matplotlib  

## 🛠️ How It Works

1. Load the dataset (CSV file with area and price).  
2. Split data into training and testing sets.  
3. Train a **Linear Regression** model on the training data.  
4. Predict house prices on test data.  
5. Evaluate model performance using metrics like **R² score** and **Mean Squared Error**.  
6. Visualize the regression line along with actual data points.  

## 📊 Output

- Predicted house prices for given areas.  
- Evaluation metrics (R² score, MSE).  
- A scatter plot of data points with the regression line.  

## 🖼️ Sample Visualization  

The script generates a plot:  

- 🔵 Blue dots = actual data points  
- 🔴 Red line = regression line (predicted prices)  

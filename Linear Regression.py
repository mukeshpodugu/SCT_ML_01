import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv("Housing.csv")
print(data.head())
x = data[['area']] 
y = data['price']            
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R2 Score :", r2_score(y_test, y_pred))
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, model.predict(x), color='black', label='Regression Line')
plt.xlabel('area')
plt.ylabel('price')
plt.title('price vs area')
plt.legend()
plt.show()
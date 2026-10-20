from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset from your photo - Table Part A
hours = [1,2,3,4,5,6,7,8,9,10]
scores = [30,40,45,55,65,70,80,85,90,95] 

X = [[h] for h in hours]
y = scores

model = LinearRegression()
model.fit(X, y)

entered = float(input("Enter hours studied: "))
prediction = model.predict([[entered]])

print(f"Predicted exam score: {prediction[0]:.2f}")

# Bonus
plt.scatter(X, y, color='blue', label='Actual Scores')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Student Exam Score Prediction')
plt.legend()
plt.savefig('supervised_result.png')
plt.show()
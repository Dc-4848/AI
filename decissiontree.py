import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X = np.array([[30], [32], [34], [36], [38], [40], [42], [44], [46], [48]])
y = np.array([0, 0, 0, 1, 1, 1, 1, 2, 2, 2])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
temperature_to_predict = np.array([[37]])
predicted_class = clf.predict(temperature_to_predict)
print(f'Predicted class for temperature {temperature_to_predict[0][0]}°C: {predicted_class[0]}')

# Task 1 - Data Loading and Preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data  # Features: sepal length, sepal width, petal length, petal width
y = iris.target  # Target: species (0, 1, 2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

y_train = to_categorical(y_train, 3)
y_test = to_categorical(y_test, 3)

print("Task 1: Data Loaded and Preprocessed")

# Task 2 - Neural Network Construction
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))

print("Task 2: Neural Network Built")

# Task 3 - Model Compilation and Training
from tensorflow.keras.optimizers import Adam

model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, batch_size=5, verbose=1)

print("Task 3: Model Compiled and Trained")

# Task 4 - Model Evaluation
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Task 4: Model Accuracy on Test Set: {test_accuracy * 100:.2f}%")

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from keras.models import Sequential
from keras.layers import Dense# , Dropout # // no need for dropout
from keras.optimizers import Adam
from keras.callbacks import LearningRateScheduler

# Load the dataset
file_path = 'plays.csv'
dataset = pd.read_csv(file_path)

# Extract features and labels
X = dataset[['Time Remaining','Down', 'Score Difference','Distance to First','Distance to Touchdown','Previous Play Outcome']]#, 'Outcome']]
y = dataset['Best']  # Best' is the column containing the best play aka the answer

# 'Outcome' is the fourth-to-last column
weights = np.array(dataset.iloc[:, -4])

# Encode categorical labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test, weights_train, weights_test = train_test_split(
    X, y, weights, test_size=0.3, random_state=42, stratify=y
)

# Standardize features (if needed)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the neural network model with dropout // Decided not to use dropout, harmed the model
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
#model.add(Dropout(0.3))  # Adding dropout to the first layer
model.add(Dense(32, activation='relu'))
#model.add(Dropout(0.3))  # Adding dropout to the second layer
model.add(Dense(len(label_encoder.classes_), activation='softmax'))

# Use the Adam optimizer with a learning rate scheduler
initial_learning_rate = 0.001#0.001
lr_schedule = LearningRateScheduler(lambda epoch: initial_learning_rate * 0.9 ** epoch)

#from keras.optimizers import  SGD
#optimizer = SGD(learning_rate=initial_learning_rate)
optimizer = Adam(learning_rate=initial_learning_rate)

# Compile the model
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model with sample weights and learning rate scheduler
model.fit(X_train, y_train, epochs=16, batch_size=75, validation_data=(X_test, y_test),
          sample_weight=weights_train, callbacks=[lr_schedule]) # 20, 45 // 50 100

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Make predictions on new data
new_data = X_test  # Replace with your actual new data
new_predictions = model.predict(new_data)

# Convert predictions back to class labels
predicted_classes = label_encoder.inverse_transform(new_predictions.argmax(axis=1))

# Output the selected play and accuracy
output_df = pd.DataFrame({
    'Actual_Best_Play': label_encoder.inverse_transform(y_test),
    'Predicted_Best_Play': predicted_classes,
    'Outcome': weights_test
})
output_df['Correct_Prediction'] = output_df['Actual_Best_Play'] == output_df['Predicted_Best_Play']

accuracy_on_new_data = output_df['Correct_Prediction'].mean()
print(f'Accuracy on New Data: {accuracy_on_new_data * 100:.2f}%')
print('\nPredictions on New Data:')
print(output_df)
'''
for item in output_df["Predicted_Best_Play"]:
    print(item)
'''


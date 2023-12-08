import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the dataset
file_path = 'plays.csv'
dataset = pd.read_csv(file_path)

# Extract features and labels
X = dataset[['Time Remaining', 'Down','Score Difference',  'Distance to First', 'Distance to Touchdown', 'Previous Play Outcome']]
y = dataset['Best']  # 'Best' is the column containing the best play (the answer)

# 'Outcome' is the fourth-to-last column
weights = np.array(dataset.iloc[:, -4])

# Encode categorical labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test, weights_train, weights_test = train_test_split(
    X, y, weights, test_size=0.3, random_state=42
)

# Standardize features (if needed)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the Random Forest model with sample weights
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train, sample_weight=weights_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Make predictions on new data
new_data = X_test  # Replace with your actual new data
new_predictions = rf_classifier.predict(new_data)

# Convert predictions back to class labels
predicted_classes = label_encoder.inverse_transform(new_predictions)

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

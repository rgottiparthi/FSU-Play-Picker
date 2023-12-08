import pandas as pd
import matplotlib.pyplot as plt

# Load the results CSV file
results_df = pd.read_csv('predictions_results.csv')

# Extract the first two words from each label
results_df['Short_Label'] = results_df['Actual_Best_Play'].apply(lambda x: ' '.join(x.split()[:2]))

# Calculate the likelihood of correct predictions for each play type
correct_prediction_likelihood = results_df.groupby('Short_Label')['Correct_Prediction'].mean()

# Plot a bar graph with wider bars and rotated x-axis labels
bar_width = 0.7
plt.bar(correct_prediction_likelihood.index, correct_prediction_likelihood * 100, width=bar_width)

# Rotate x-axis labels and adjust their alignment
plt.xticks(rotation='vertical', ha='center')

plt.xlabel('Short_Label')
plt.ylabel('Correct Prediction Likelihood (%)')
plt.title('Random Forest Likelihood')

# Save the plot as an image file (e.g., PNG)
plt.tight_layout()
plt.savefig('random_forest.png')

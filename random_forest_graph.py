import pandas as pd
import matplotlib.pyplot as plt

# Load the results CSV file
results_df = pd.read_csv('predictions_results.csv')

# Calculate the likelihood of correct predictions for each play type
correct_prediction_likelihood = results_df.groupby('Actual_Best_Play')['Correct_Prediction'].mean()

# Plot a bar graph with wider bars and rotated x-axis labels
bar_width = 0.7
plt.bar(correct_prediction_likelihood.index, correct_prediction_likelihood * 100, width=bar_width)

# Rotate x-axis labels and adjust their alignment
plt.xticks(rotation='vertical', ha='center')

plt.xlabel('Actual_Best_Play')
plt.ylabel('Correct Prediction Likelihood (%)')
plt.title('Correct Prediction Likelihood for Each Play Type')

# Save the plot as an image file (e.g., PNG)
plt.tight_layout()
plt.savefig('random_forest.png')

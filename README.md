=====Python Library for Play Picker=====
Contributors: Rohith, Kian, Jonas, Haleigh, Christopher Tucker

Source Code Files:

encoded_generator.py:
  Description: Encoded_generator.py repares our football play data for analysis. It encodes categorical variables into a numerical format suitable for our machine learning algorithms.
  Libraries Used: pandas
    pandas: Used for reading, processing, and writing CSV files.
  
arm.py:
  Description: Implements association rule mining on football play data. It includes functionality to preprocess data, apply the Apriori algorithm for generating frequent itemsets, and derive association rules from these itemsets.
  Libraries Used: pandas, mlxtend (for frequent_patterns such as apriori and association_rules), matplotlib.pyplot
    pandas: Essential for handling the dataset in DataFrame format.
    mlxtend.frequent_patterns (apriori, association_rules): These functions are used for association rule mining. 'apriori' helps us find frequent itemsets, and 'association_rules' is used to generate the actual rules.
    matplotlib.pyplot: Utilized for creating visualizations, specifically scatter plots to illustrate the support vs. confidence of the mined association rules.

game_parser.py:
  Description: Parses and processes game data from the 'play-by-plays' directory, extracting relevant information and structuring it for analysis.
  Libraries Used: os, csv, re, random
    os: Used for file path handling and directory traversing, particularly for accessing and listing files within the "play-by-plays" directory.
    csv: Used for reading and writing CSV files, essential for processing play-by-play text data.
    re: Used for regular expression operations for string matching.
    random: Used for generating random numbers.

keras.py:
  Description: Contains neural network models built using Keras, mainly for predictive analytics in the context of the project.
  Libraries Used: pandas, numpy, sklearn (for model_selection, preprocessing), keras

random_forest.py:
  Description: Implements a Random Forest classifier for predictive modeling, analyzing football play data to predict outcomes.
  Libraries Used: pandas, numpy, sklearn (for model_selection, ensemble, metrics, preprocessing)
  Data and Output Files:


Data Files:

plays.csv:
  Description: A CSV file containing parsed and processed play data, output from game_parser.py.

random_forest.txt:
  Description: Contains output or logs from the random_forest.py script, likely detailing the performance and predictions of the Random Forest model.
  Directories:

play-by-plays:
  Description: A directory containing text files with play-by-play descriptions of games.

association_rule_mining:
  Description: Dedicated to association rule mining, this directory contains scripts (like arm.py), output files (like encoded_plays.csv and association_rules_plot.png), and any related data for mining association rules.


Encoded Data:

encoded_plays.csv:
  Description: An encoded version of the plays data, formatted specifically for association rule mining and produced by encoded_generator.py.

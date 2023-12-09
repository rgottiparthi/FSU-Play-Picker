=====Python Library for Play Picker=====
Contributors: Rohith, Kian, Jonas, Haleigh, Christopher

Intstuctions to run the code:
	Run the “make” command.

Source Code Files with Libraries Used:

Data and output files:

plays.csv:
  Description: A CSV file containing parsed and processed play data, output from game_parser.py.

play-by-plays:
  Description: A directory containing text files with play-by-play descriptions of games.

random_forest_graph.png:
  Description: Generates a bar graph with the accuracy for each best play_type in the Random Forest model.

keras_graph.png:
  Description: Generates a bar graph with the accuracy for each best play_type in the Keras model.

Parsing Data:

game_parser.py:
  Description: Parses and processes game data from the 'play-by-plays' directory, extracting relevant information and structuring it for analysis.
  Libraries Used: os, csv, re, random
    os: Used for file path handling and directory traversing, particularly for accessing and listing files within the "play-by-plays" directory.
    csv: Used for reading and writing CSV files, essential for processing play-by-play text data.
    re: Used for regular expression operations for string matching.
    random: Used for generating random numbers.


Models:
keras.py:
  Description: Contains neural network models built using Keras, mainly for predictive analytics in the context of the project.
  Libraries Used: pandas, numpy, sklearn (for model_selection, preprocessing), keras
    pandas: Used for reading CSVs.
    numpy: Used for math operations.
    sklearn (for model_selection, preprocessing): Provides tools for data splitting and preprocessing which are used in preparing the dataset for training.
    keras: Used for building our keras model.

random_forest.py:
  Description: Implements a Random Forest classifier for predictive modeling, analyzing football play data to predict outcomes.
  Libraries Used: pandas, numpy, sklearn (for model_selection, ensemble, metrics, preprocessing)
  pandas: For reading CSV files and manipulating data,  used in preparing the dataset for the Random Forest model.
  numpy: Used for many math operations
  sklearn (for model_selection, ensemble, metrics, preprocessing): Used for splitting our datasets, implementing the Random Forest model, and evaluating model performance
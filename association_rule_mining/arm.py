import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Set Pandas options to display more rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def preprocess_data(data):
    # Convert non-boolean columns to binary
    non_boolean_columns = data.select_dtypes(exclude='bool').columns
    data[non_boolean_columns] = (data[non_boolean_columns] != 0).astype(bool)
    return data

def mine_association_rules(input_csv):
    # Load CSV data into a DataFrame
    data = pd.read_csv(input_csv)

    # Preprocess data to convert non-boolean values to binary
    data = preprocess_data(data)

    # Generate Frequent Itemsets
    min_support = 0.1
    frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)

    # Generate Association Rules
    min_confidence = 0.999
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

    return rules

if __name__ == "__main__":
    # Specify the input file path
    input_csv_path = "encoded_plays.csv"

    # Mine association rules
    mined_rules = mine_association_rules(input_csv_path)

    # Display the mined association rules
    print("Mined Association Rules:")
    print(mined_rules)

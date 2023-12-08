import pandas as pd

def encode_plays(input_csv, output_csv):
    # Load CSV data into a DataFrame
    data = pd.read_csv(input_csv)

    # Drop the "Play Description" column
    data = data.drop("Play Description", axis=1)

    # Drop the "Play Description" column
    data = data.drop("Play Number", axis=1)

    # Encode categorical variables
    data_encoded = pd.get_dummies(data)

    # Save the encoded data to a new CSV file
    data_encoded.to_csv(output_csv, index=False)

if __name__ == "__main__":
    # Specify the input and output file paths
    input_csv_path = "plays.csv"
    output_csv_path = "association_rule_mining/encoded_plays.csv"

    # Call the function to encode plays and save to a new CSV
    encode_plays(input_csv_path, output_csv_path)

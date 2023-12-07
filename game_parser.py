import os
import csv
import re

# Function to parse the play-by-play data and extract relevant information
def parse_play_by_play(file_path):
    plays = []
    play_number = 1
    current_quarter = None
    offense = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # Placeholder need to compute the time from this
            if "End of game" in line:
                continue

            # Skip lines containing "PENALTY"
            if "PENALTY" in line:
                continue

            # Check for the start of a new quarter
            if "Start of 1st Half" in line:
                current_quarter = 1
            elif "Start of Quarter #2" in line:
                current_quarter = 2
            elif "Start of 2nd Half" in line:
                current_quarter = 3
            elif "Start of Quarter #4" in line:
                current_quarter = 4

            # Check for lines that start with the down
            elif line.startswith(("1st", "2nd", "3rd", "4th")):
                down = int(line[0])
                play_type = "NONE"
                net_yards = 0
                touchdown = 0  # Initialize touchdown attribute to 0
                sack = 0  # Initialize sack attribute to 0
                first_down = 0  # Initialize first_down attribute to 0

                # Check for play types
                if "rush right" in line:
                    play_type = "rush right"
                elif "rush middle" in line:
                    play_type = "rush middle"
                elif "rush left" in line:
                    play_type = "rush left"
                elif "punt" in line:
                    play_type = "punt"
                    net_yards = 0
                elif "pass" in line:
                    play_type = "pass"
                elif "kick attempt" in line:
                    play_type = "kick attempt"

                # Use regular expression to find net yards
                match = re.search(r'(\d+)(?= yards)', line)
                if match and play_type != "punt" and play_type != "kick attempt":
                    net_yards = int(match.group())

                    # Check for "loss" in the line
                    if "loss" in line:
                        net_yards *= -1

                # Check for "TOUCHDOWN" in the line
                if "TOUCHDOWN" in line:
                    touchdown = 1

                # Check for "sacked" in the line
                if "sacked" in line:
                    sack = 1

                # Check for "1ST DOWN" in the line
                if "1ST DOWN" in line or net_yards > 10:
                    first_down = 1

                # Check for offense
                if "Florida St." in line and "drive start" in line:
                    offense = True
                    continue
                elif "drive start" in line:
                    offense = False
                    continue

                # Extract distance to first
                and_match = re.search(r'and (\d+)', line)
                distance_to_first = int(and_match.group(1)) if and_match else None

                # Skip lines containing "clock"
                if "drive start" in line:
                    continue

                if "kickoff" in line:
                    continue

                if "timeout" in line.casefold():
                    continue

                # Skip the line if offense is False
                if not offense:
                    continue

                # Calculate Outcome value
                outcome = net_yards + touchdown * 180 + first_down * 10 - sack * 10 - 3

                plays.append((current_quarter, play_number, down, play_type, net_yards, distance_to_first, touchdown, sack, first_down, outcome, line))
                play_number += 1

    return plays

# Function to write the parsed plays to a CSV file
def write_to_csv(plays, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['Quarter', 'Play Number', 'Down', 'Play Type', 'Distance to First', 'Outcome', 'Play Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for play in plays:
            writer.writerow({'Quarter': play[0], 'Play Number': play[1], 'Down': play[2], 'Play Type': play[3], 'Distance to First': play[5], 'Outcome': play[9], 'Play Description': play[10]})

if __name__ == "__main__":
    directory_path = "play-by-plays"
    csv_file = "plays.csv"

    all_plays = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            plays = parse_play_by_play(file_path)
            all_plays.extend(plays)

    write_to_csv(all_plays, csv_file)

    print(f"CSV file '{csv_file}' created successfully.")
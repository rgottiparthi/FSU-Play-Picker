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
                play_type = "NONE"
                net_yards = 0

                # Check for play types
                if "rush right" in line:
                    play_type = "rush right"
                elif "rush middle" in line:
                    play_type = "rush middle"
                elif "rush left" in line:
                    play_type = "rush left"
                elif "punt" in line:
                    play_type = "punt"
                elif "pass" in line:
                    play_type = "pass"
                elif "kick attempt" in line:
                    play_type = "kick attempt"

                # Use regular expression to find net yards
                match = re.search(r'(\d+)(?= yards)', line)
                if match:
                    net_yards = int(match.group())

                    # Check for "loss" in the line
                    if "loss" in line:
                        net_yards *= -1

                # Check for offense
                if "Florida St." in line and "drive start" in line:
                    offense = True
                    continue
                elif "drive start" in line:
                    offense = False
                    continue

                # Skip the line if offense is False
                if not offense:
                    continue

                plays.append((current_quarter, play_number, play_type, net_yards, line))
                play_number += 1

    return plays

# Function to write the parsed plays to a CSV file
def write_to_csv(plays, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['Quarter', 'Play Number', 'Play Type', 'Net Yards', 'Play Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for play in plays:
            writer.writerow({'Quarter': play[0], 'Play Number': play[1], 'Play Type': play[2], 'Net Yards': play[3], 'Play Description': play[4]})

if __name__ == "__main__":
    file_path = "play-by-plays/southern-mississippi.txt"
    csv_file = "plays.csv"

    plays = parse_play_by_play(file_path)
    write_to_csv(plays, csv_file)

    print(f"CSV file '{csv_file}' created successfully.")
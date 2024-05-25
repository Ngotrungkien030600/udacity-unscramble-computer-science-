from helpers import read_csv

# Read the contents from the CSV files
texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")

def get_unique_numbers():
    """
    Extracts unique telephone numbers from both calls and texts CSV files.

    Returns:
        set: A set containing unique telephone numbers.
    """
    unique_numbers = set()

    # Add numbers from texts.csv to the set
    for text in texts:
        unique_numbers.add(text[0])
        unique_numbers.add(text[1])

    # Add numbers from calls.csv to the set
    for call in calls:
        unique_numbers.add(call[0])
        unique_numbers.add(call[1])

    return unique_numbers

def main():
    """
    TASK 1:
    Determines the number of unique telephone numbers in the records.
    Prints a message with the count of unique telephone numbers.
    """
    unique_numbers = get_unique_numbers()
    print(f"There are {len(unique_numbers)} different telephone numbers in the records.")

if __name__ == "__main__":
    main()

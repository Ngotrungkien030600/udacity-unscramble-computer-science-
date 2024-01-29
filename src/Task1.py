from helpers import read_csv


texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")


def main():
    """
    TASK 1:
    How many different telephone numbers are there in the records?
    Print a message:
    "There are <count> different telephone numbers in the records."
    """


if __name__ == "__main__":
    main()

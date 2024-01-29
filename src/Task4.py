from helpers import read_csv


texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")


def main():
    """
    TASK 4:
    The telephone company want to identify numbers that might be doing
    telephone marketing. Create a set of possible telemarketers:
    these are numbers that make outgoing calls but never send texts,
    receive texts or receive incoming calls.

    Print a message:
    "These numbers could be telemarketers: "
    <list of numbers>
    The list of numbers should be print out one per line in lexicographic order with no duplicates.
    """
    # TODO: TASK 04 implement details
    print("TASK 04 implement")


if __name__ == "__main__":
    main()

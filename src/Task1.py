from helpers import read_csv


texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")


def get_unique_numbers():
    """Select unique telephone numbers from both calls and texts csv files

    Returns:
        list: The list contains unique telephone numbers
    """
    telephone_numbers = []

    for text, call in zip(texts, calls):
        if text[0] not in telephone_numbers:
            telephone_numbers.append(text[0])
        if text[1] not in telephone_numbers:
            telephone_numbers.append(text[1])

        if call[0] not in telephone_numbers:
            telephone_numbers.append(call[0])
        if call[1] not in telephone_numbers:
            telephone_numbers.append(call[1])

    return telephone_numbers


def main():
    """
    TASK 1:
    How many different telephone numbers are there in the records?
    Print a message:
    "There are <count> different telephone numbers in the records."
    """
    print(
        "There are {} different telephone numbers in the records.".format(
            len(get_unique_numbers())
        )
    )


if __name__ == "__main__":
    main()

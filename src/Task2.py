from helpers import read_csv


texts = read_csv(csv_files="./src/files/texts.csv")  # Read the contents from texts.csv.
calls = read_csv(csv_files="./src/files/calls.csv")  # Read the contents from calls.csv.


def get_longest_calling_duration():
    """Gets the telephone number which has the longest calling duration

    Returns:
        tuple: The telephone number and its calling duration
    """
    telephone_numbers = {}

    for caller, receiver, _, duration in calls:
        telephone_numbers[caller] = (
            int(duration)
            if caller not in telephone_numbers
            else (telephone_numbers[caller] + int(duration))
        )  # Adds the caller's number and its duration to the telephone_numbers dictionary.
        telephone_numbers[receiver] = (
            int(duration)
            if receiver not in telephone_numbers
            else (telephone_numbers[receiver] + int(duration))
        )  # Adds the receiver's number and its duration to the telephone_number dictionary

    longest_duration = 0  # longest call duration of the telephone number
    telephone = ""  # The telephone number which have the longest duration

    for key, value in telephone_numbers.items():
        if longest_duration < value:
            longest_duration = value  # get the longest call duration from telephone_numbers dictionary (maximum value of telephone_numbers dictionary)
            telephone = key  # get the telephone number which have the longest duration (key from telephone_numbers dictionary which have the maximum value)

    return (
        telephone,
        longest_duration,
    )  # max(telephone_numbers.items(), key=lambda x: x[1])


def main():
    """
    TASK 2: Which telephone number spent the longest time on the phone
    during the period? Don't forget that time spent answering a call is
    also time spent on the phone.
    Print a message:
    "<telephone number> spent the longest time, <total time> seconds, on the phone during
    September 2016.".
    """
    print(
        "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
            *get_longest_calling_duration()
        )
    )


if __name__ == "__main__":
    main()

from helpers import read_csv


texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")


def get_longest_calling_duration():
    """Gets the telephone number which has the longest calling duration

    Returns:
        tuple: The telephone number and its calling duration
    """
    telephone_numbers = {}

    for caller, receiver, timestamp, duration in calls:
        telephone_numbers[caller] = (
            int(duration)
            if caller not in telephone_numbers
            else (telephone_numbers[caller] + int(duration))
        )
        telephone_numbers[receiver] = (
            int(duration)
            if receiver not in telephone_numbers
            else (telephone_numbers[receiver] + int(duration))
        )

    longest_duration = 0
    telephone = ""

    for key, value in telephone_numbers.items():
        if longest_duration < value:
            longest_duration = value
            telephone = key

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

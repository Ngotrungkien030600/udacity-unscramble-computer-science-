from helpers import read_csv


texts = read_csv(csv_files="./src/files/texts.csv")  # Read the contents from texts.csv
calls = read_csv(csv_files="./src/files/calls.csv")  # Read the contents from calls.csv


def main():
    """
    TASK 0:
    What is the first record of texts and what is the last record of calls?
    Print messages:
    "First record of texts, <incoming number> texts <answering number> at time <time>"
    "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
    """
    print(
        "First record of texts, {} texts {} at time {}".format(
            texts[0][0]
            if len(texts) > 0
            else None,  # Get 1st item from 1st line in texts.csv if there are any contents from texts.csv, otherwise it is None value
            texts[0][1]
            if len(texts) > 0
            else None,  # Get 2nd item from 1st line in texts.csv if there are any contents from texts.csv, otherwise it is None value
            texts[0][2]
            if len(texts) > 0
            else None,  # Get 3rd item from 1st line in texts.csv if there are any contents from texts.csv, otherwise it is None value
        )
    )
    print(
        "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
            calls[-1][0]
            if len(calls) > 0
            else None,  # Get 1st item from 1st line in calls.csv if there are any contents from texts.csv, otherwise it is None value
            calls[-1][1]
            if len(calls) > 0
            else None,  # Get 2nd item from 1st line in calls.csv if there are any contents from texts.csv, otherwise it is None value
            calls[-1][2]
            if len(calls) > 0
            else None,  # Get 3rd item from 1st line in calls.csv if there are any contents from texts.csv, otherwise it is None value
            calls[-1][3]
            if len(calls) > 0
            else 0,  # Get 4th item from 1st line in calls.csv if there are any contents from texts.csv, otherwise it is 0 value
        )
    )


if __name__ == "__main__":
    main()

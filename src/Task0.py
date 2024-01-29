from helpers import read_csv


texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")


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
            texts[0][0], texts[0][1], texts[0][2]
        )
    )
    print(
        "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
            calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]
        )
    )


if __name__ == "__main__":
    main()

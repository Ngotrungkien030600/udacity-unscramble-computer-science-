from helpers import read_csv

texts = read_csv(csv_files="./src/files/texts.csv")  # Read data from texts.csv
calls = read_csv(csv_files="./src/files/calls.csv")  # Read data from calls.csv

def main():
    """
    TASK 0:
    Display the first record from the texts and the last record from the calls.
    Messages:
    "First record of texts, <incoming number> texts <answering number> at time <time>"
    "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <duration> seconds"
    """
    if texts:
        first_text = texts[0]
        print(f"First record of texts, {first_text[0]} texts {first_text[1]} at time {first_text[2]}")
    else:
        print("No texts records available")

    if calls:
        last_call = calls[-1]
        print(f"Last record of calls, {last_call[0]} calls {last_call[1]} at time {last_call[2]}, lasting {last_call[3]} seconds")
    else:
        print("No calls records available")

if __name__ == "__main__":
    main()

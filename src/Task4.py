from helpers import merge_sort, read_csv

# Read the contents from the CSV files
texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")

def main():
    """
    TASK 4:
    Identify numbers that might be doing telephone marketing. Telemarketers
    make outgoing calls but do not send texts, receive texts, or receive incoming calls.

    Print a message:
    "These numbers could be telemarketers: "
    <list of numbers>
    The list of numbers should be printed one per line in lexicographic order with no duplicates.
    """
    outgoing_texts = set()
    incoming_texts = set()
    outgoing_calls = set()
    incoming_calls = set()

    # Populate the sets with unique numbers
    for text in texts:
        outgoing_texts.add(text[0])
        incoming_texts.add(text[1])
    
    for call in calls:
        outgoing_calls.add(call[0])
        incoming_calls.add(call[1])

    # Identify potential telemarketers
    telemarketers = outgoing_calls - outgoing_texts - incoming_texts - incoming_calls

    print("These numbers could be telemarketers:")
    
    # Sort the telemarketers and print them
    sorted_telemarketers = merge_sort(list(telemarketers))
    for number in sorted_telemarketers:
        print(number)

if __name__ == "__main__":
    main()

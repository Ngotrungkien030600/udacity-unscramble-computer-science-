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
    outgoing_texts = []
    incoming_texts = []
    outgoing_calls = []
    incoming_calls = []
    
    for text, call in zip(texts, calls):
        if text[0] not in outgoing_texts:
            outgoing_texts.append(text[0])
        if text[1] not in incoming_texts:
            incoming_texts.append(text[1])
        if call[0] not in outgoing_calls:
            outgoing_calls.append(call[0])
        if call[1] not in incoming_calls:
            incoming_calls.append(call[1])
            
    telemakers = []
    
    for call in outgoing_calls:
        if call not in outgoing_texts and call not in incoming_texts and call not in incoming_calls:
            telemakers.append(call)
    
    print("These numbers could be telemarketers:")
    
    for telemaker in telemakers:
        print(telemaker)
    


if __name__ == "__main__":
    main()

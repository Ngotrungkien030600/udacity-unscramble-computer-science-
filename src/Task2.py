from helpers import read_csv

# Read the contents from the CSV files
texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")

def get_longest_calling_duration():
    """
    Determines the telephone number with the longest total calling duration.

    Returns:
        tuple: A tuple containing the telephone number and its total calling duration.
    """
    call_durations = {}

    # Aggregate call durations for each telephone number
    for caller, receiver, _, duration in calls:
        duration = int(duration)
        if caller in call_durations:
            call_durations[caller] += duration
        else:
            call_durations[caller] = duration
        
        if receiver in call_durations:
            call_durations[receiver] += duration
        else:
            call_durations[receiver] = duration

    # Find the telephone number with the longest call duration
    max_duration = 0
    max_telephone = None
    for number, total_duration in call_durations.items():
        if total_duration > max_duration:
            max_duration = total_duration
            max_telephone = number

    return max_telephone, max_duration

def main():
    """
    TASK 2: Find the telephone number that spent the longest time on the phone
    during the period. Time spent on both incoming and outgoing calls is considered.
    Print a message:
    "<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016."
    """
    longest_caller, longest_duration = get_longest_calling_duration()
    print(f"{longest_caller} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")

if __name__ == "__main__":
    main()

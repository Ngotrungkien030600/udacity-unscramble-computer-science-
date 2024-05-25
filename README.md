Overview
You'll apply the skills you've learned so far in a more realistic scenario. The five tasks are structured to give you experience with a variety of programming problems. You will receive code review of your work; this personal feedback will help you to improve your solutions.

The text and call data are provided in csv files.

The text data (text.csv) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".

What will I learn?
In this project, you will:

Apply your Python knowledge to breakdown problems into their inputs and outputs.
Perform an efficiency analysis of your solution.
Warm up your Python skills for the course.
Time complexity analysis
Task 0: Total time complexity is O(1)
The time complexity for getting the first text from texts.csv and the last call from calls.csv is O(2) ~= O(1).

Task 1: Total time complexity is O(n^2)
python
Copy code
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
The time complexity for selecting the unique telephone numbers from the function get_unique_numbers is O(n^2) (O(1) for the best case indicates that the texts.csv and calls.csv have only one content, and the worst case is O(n^2) indicates that the texts.csv and calls.csv have n contents by iterating through the entire list after reading all contents from csv files).

Task 2: Total time is O(n)
python
Copy code
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
    )
Adding all the telephone numbers dictionary and its total call duration by iterating through the read contents of CSV files takes n times, and finding the longest duration by iterating through the added telephone numbers dictionary takes n times and using the branching conditional with not in operator takes n times, so the total time is n^2 + n^2 = 2n^2, and it is concluded to O(n^2).

Task 3: Total time is O(nlog(n))
python
Copy code
bangalore_calls = [call for call in calls if call[0].startswith("(080)")]
The total time of adding the calls which start with (080) is n times for the worst case and 1 for the best case by iterating through the read texts and calls. => O(n)

python
Copy code
bangalore_receivers = [call[1] for call in bangalore_calls]
The total time of adding the incoming calls from the list of Bangalore calls is n times for the worst case and 1 for the best case by iterating over the entire list => O(n)

python
Copy code
    bangalore_receivers_area_codes = []

    for receiver in bangalore_receivers:
        if re.search(r"\(\w+\)", receiver):
            area_code = re.search(r"(\(.*?\))", receiver).group()
            if area_code not in bangalore_receivers_area_codes:
                bangalore_receivers_area_codes.append(area_code)
        elif receiver[:3].startswith("140"):
            area_code = receiver[:3]
            if area_code not in bangalore_receivers_area_codes:
                bangalore_receivers_area_codes.append(area_code)
        elif re.search(r"^[7|8|9]", receiver):
            area_code = receiver[:4]
            if area_code not in bangalore_receivers_area_codes:
                bangalore_receivers_area_codes.append(area_code)
The time of the for loop takes n times when iterating the list bangalore_receivers, and the time of invoking re.search takes m times based on the string length, and selecting the distinct area code with the not in operator takes n time, so the total times is O(n^2 * m). We can conclude it is O(n^3) because the re.search runs in the if function and the not in operator to select the distinct area_code.

python
Copy code
for code in merge_sort(bangalore_receivers_area_codes):
    print(code)
The total time for sorting the list "bangalore_receivers_area_codes" is nlog(n) for the worst case and 1 for the best case if there is only one element in the list. => O(nlog(n))

The total time for iterating through the sorted list "bangalore_receivers_area_codes" is n times => O(n)

python
Copy code
bangalore_receivers_080_prefix = [
        call for call in bangalore_receivers if call.startswith("(080)")
    ]
The total time for saving the new list "bangalore_receivers_080_prefix" from list "bangalore_receivers" takes n time for the worst case and 1 for the best case => O(n)

python
Copy code
print(
        "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
            round(
                len(bangalore_receivers_080_prefix) /
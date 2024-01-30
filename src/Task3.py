import re
from helpers import read_csv


texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")


def main():
    """
    TASK 3:
    (080) is the area code for fixed line telephones in Bangalore.
    Fixed line numbers include parentheses, so Bangalore numbers
    have the form (080)xxxxxxx.)

    Part A: Find all of the area codes and mobile prefixes called by people
    in Bangalore. In other words, the calls were initiated by "(080)" area code
    to the following area codes and mobile prefixes:
    - Fixed lines start with an area code enclosed in brackets. The area
      codes vary in length but always begin with 0.
    - Mobile numbers have no parentheses, but have a space in the middle
      of the number to help readability. The prefix of a mobile number
      is its first four digits, and they always start with 7, 8 or 9.
    - Telemarketers' numbers have no parentheses or space, but they start
      with the area code 140.

    Print the answer as part of a message:
    "The numbers called by people in Bangalore have codes:"
    <list of codes>
    The list of codes should be print out one per line in lexicographic order with no duplicates.

    Part B: What percentage of calls from fixed lines in Bangalore are made
    to fixed lines also in Bangalore? In other words, of all the calls made
    from a number starting with "(080)", what percentage of these calls
    were made to a number also starting with "(080)"?

    Print the answer as a part of a message::
    "<percentage> percent of calls from fixed lines in Bangalore are calls
    to other fixed lines in Bangalore."
    The percentage should have 2 decimal digits
    """
    bangalore_calls = [call for call in calls if call[0].startswith("(080)")]
    bangalore_receivers = [call[1] for call in bangalore_calls]
    bangalore_receivers_area_codes = []

    for receiver in bangalore_receivers:
        if re.search(r"\(\w+\)", receiver):
            area_code = re.search(r"(\(.*?\))", receiver).group()

            if area_code not in bangalore_receivers_area_codes:
                bangalore_receivers_area_codes.append(area_code)
        elif re.search(r"(^[7|8|9])", receiver):
            area_code = receiver[:4]
            if area_code not in bangalore_receivers_area_codes:
                bangalore_receivers_area_codes.append(area_code)

    print("The numbers called by people in Bangalore have codes:")
    for code in bangalore_receivers_area_codes:
        print(code)

    bangalore_receivers_080 = [
        call for call in bangalore_receivers if call.startswith("(080)")
    ]
    print(
        "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
            round(len(bangalore_receivers_080) / len(bangalore_receivers) * 100, 2)
        )
    )


if __name__ == "__main__":
    main()

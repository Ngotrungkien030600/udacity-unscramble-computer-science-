import re
from helpers import merge_sort, read_csv
# Read the contents from the CSV files
texts = read_csv(csv_files="./src/files/texts.csv")
calls = read_csv(csv_files="./src/files/calls.csv")

def extract_area_codes_and_prefixes(number):
    """
    Extracts the area code or prefix from a given telephone number.
    
    Args:
        number (str): The telephone number to extract the area code or prefix from.
    
    Returns:
        str: The extracted area code or prefix.
    """
    if number.startswith("("):  # Area code enclosed in parentheses for fixed lines
        return re.search(r"\((.*?)\)", number).group(1)
    elif " " in number and number[0] in "789":  # First digit and space indicate mobile numbers
        return number[:4]
    elif number.startswith("140"):  # Telemarketers have a specific prefix
        return "140"
    return None

def main():
    """
    TASK 3:
    Analyzes the call records to find area codes and prefixes called by Bangalore numbers and
    computes the percentage of calls from Bangalore to Bangalore.

    Part A: Identify all unique area codes and mobile prefixes called by people in Bangalore.
    Part B: Calculate the percentage of calls from fixed lines in Bangalore to other Bangalore fixed lines.
    """
    # Part A: Find area codes and mobile prefixes called by Bangalore numbers
    bangalore_calls = [call for call in calls if call[0].startswith("(080)")]
    bangalore_receivers_codes = set()

    for call in bangalore_calls:
        code = extract_area_codes_and_prefixes(call[1])
        if code:
            bangalore_receivers_codes.add(code)

    sorted_codes = merge_sort(list(bangalore_receivers_codes))

    print("The numbers called by people in Bangalore have codes:")
    for code in sorted_codes:
        print(code)

    # Part B: Calculate the percentage of calls from Bangalore to Bangalore
    bangalore_to_bangalore_calls = [
        call for call in bangalore_calls if call[1].startswith("(080)")
    ]
    percentage = (len(bangalore_to_bangalore_calls) / len(bangalore_calls)) * 100

    print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

if __name__ == "__main__":
    main()

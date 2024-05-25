import csv

def read_csv(csv_file, delimiter=","):
    """
    Reads the contents of a CSV file.

    Args:
        csv_file (str): The path to the CSV file.
        delimiter (str, optional): The character separating values in the CSV. Defaults to ",".

    Returns:
        list: A list containing the rows from the CSV file.
    """
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)
        contents = list(reader)  # Store the CSV contents in a list

    return contents  # Return the list containing CSV rows

def merge_sort(items, comparator=lambda x, y: x < y):
    """
    Sorts a list using the merge sort algorithm.

    Args:
        items (list): The list to be sorted.
        comparator (function, optional): A function defining the sorting order. Defaults to ascending order.

    Returns:
        list: The sorted list.
    """
    if len(items) > 1:
        mid = len(items) // 2  # Find the middle index
        left_half = items[:mid]  # Divide the list into left half
        right_half = items[mid:]  # Divide the list into right half

        merge_sort(left_half, comparator)  # Recursively sort the left half
        merge_sort(right_half, comparator)  # Recursively sort the right half

        i = j = k = 0  # Initialize pointers for left_half, right_half, and main list

        # Merge the sorted halves back into the main list
        while i < len(left_half) and j < len(right_half):
            if comparator(left_half[i], right_half[j]):
                items[k] = left_half[i]
                i += 1
            else:
                items[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_half
        while i < len(left_half):
            items[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_half
        while j < len(right_half):
            items[k] = right_half[j]
            j += 1
            k += 1

    return items  # Return the sorted list
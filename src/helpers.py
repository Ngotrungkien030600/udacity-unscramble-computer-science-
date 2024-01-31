import csv


def read_csv(csv_files, delimiter=","):
    """Reads contents from csv files

    Args:
        csv_files (str): The directory of csv file
        delimiter (str, optional): The csv content seperator. Defaults to ",".

    Returns:
        list: The contents from csv file
    """    
       
    with open(csv_files, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter) # Read contents from csv file
        contents = list(reader) # append all contents read from csv file to the empty lists
        
    return contents # returns multiple contents from csv file.

def merge_sort(items, order='asc'):
    """Sort multiple items with merge sort using divide and conquer methods

    Args:
        items (list): The unsorted list
        order (str, optional): The sorting order method. Defaults to 'asc'.

    Raises:
        Exception: The exception for invalid sorting order

    Returns:
        list: The sorted list
    """
    
    if len(items) > 1:
        mid_index = len(items) // 2 # Gets the middle index
        left_items = items[:mid_index] # Gets the half-left side of the list "items"
        right_items = items[mid_index:] # Gets the right-side of the list "items"
        
        merge_sort(left_items) # Recursively call to sort the half-left side
    
        merge_sort(right_items) # Recursively call to sort the half-right side
    
        left_index = right_index = main_index = 0 # Initiate the left_index for half-left side items, right_index for half-right side items and main_index for the orginal list
        if order == 'asc': # Intiate the merge sort in ascended order.
            while left_index < len(left_items) and right_index < len(right_items):
                if left_items[left_index] <= right_items[right_index]:
                    items[main_index] = left_items[left_index] # merge half-left side to the orginal list.
                    left_index += 1
                else:
                    items[main_index] = right_items[right_index] # merge half-right side to the orginal list
                    right_index += 1
                main_index += 1
        elif order == 'desc': # Intiate the merge sort in descended order.
            while left_index < len(left_items) and right_index < len(right_items):
                if left_items[left_index] >= right_items[right_index]:
                    items[main_index] = left_items[left_index]  # merge half-left side to the orginal list.
                    left_index += 1
                else:
                    items[main_index] = right_items[right_index]  # merge half-right side to the orginal list
                    right_index += 1
                main_index += 1
        else:
            raise Exception("Sorting order is not valid")    
        
        # Add the remaining items from left side to the original list.
        while left_index < len(left_items):
            items[main_index] = left_items[left_index]
            left_index += 1
            main_index += 1
        
        # Add the remaining items from right side to the original list.
        while right_index < len(right_items):
            items[main_index] = right_items[right_index]
            right_index += 1
            main_index += 1
        
        return items # The sorted list
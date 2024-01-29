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
        reader = csv.reader(f, delimiter=delimiter)
        contents = list(reader)
        
    return contents
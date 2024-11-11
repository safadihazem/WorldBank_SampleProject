import pandas as pd

def create_dictionary(dataframe):
    """
    Creates a dictionary from a dataframe mapping first names to gender.
    
    Args:
        dataframe (pd.DataFrame): DataFrame with columns 'first name' and 'gender'.
    
    Returns:
        dict: Dictionary with first names as keys and gender as values.
    """
    name_gender_dict = dict(zip(dataframe['first name'], dataframe['gender']))
    return name_gender_dict


def file_to_dict(file_path, file_type):
    """
    Reads a file and returns a dictionary with the first column as keys and the second as values.
    
    Args:
        file_path (str): The path to the file.
        file_type (str): The type of the file ('csv' or 'xlsx').
    
    Returns:
        dict: Dictionary mapping of the first column to the second column.
    """
    if file_type.lower() == 'csv':
        df = pd.read_csv(file_path, header=None)
    elif file_type.lower() == 'xlsx':
        df = pd.read_excel(file_path, header=None)
    else:
        raise ValueError("Unsupported file type. Supported types: 'csv' and 'xlsx'.")

    return df.set_index(0).to_dict()[1]

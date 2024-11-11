import pandas as pd
from utils import create_dictionary, file_to_dict

def fill_missing_gender(data, col_name, gender_col):
    """
    Fills missing gender values in the dataframe based on first name.
    
    Args:
        data (pd.DataFrame): The DataFrame containing names and gender columns.
        col_name (str): Column with the full name.
        gender_col (str): Column with gender values.
        dict1_path (str): Path to the first dictionary file.
        dict2_path (str): Path to the second dictionary file.
    
    Returns:
        pd.DataFrame: Updated DataFrame with filled-in gender values.
    """
   # Define paths to dictionary files
    dict1_path = '../data/arabic_names_with_gender.csv'
    dict2_path = '../data/dictionary2_ar.xlsx'

    # Extract first name from the specified column
    data['first name'] = data[col_name].str.split().str[0]
    
    # Load dictionaries from the specified paths
    dict1 = file_to_dict(dict1_path, 'csv')
    dict2 = file_to_dict(dict2_path, 'xlsx')
    
    # Create gender mappings
    data[gender_col] = data[gender_col].combine_first(data['first name'].map(dict1))
    data[gender_col] = data[gender_col].combine_first(data['first name'].map(dict2))
    
    # Drop the helper 'first name' column
    data = data.drop(['first name'], axis=1)
    
    return data

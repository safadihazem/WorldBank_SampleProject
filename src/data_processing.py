import pandas as pd
from utils import load_dicts  # import from utils.py to load dictionaries

def standardize_date_column(column: pd.Series) -> pd.Series:
    """
    Standardizes the date format in a given column to the format '%d/%m/%Y'.
    
    Args:
        column (pd.Series): A Series containing date values in various formats.
    
    Returns:
        pd.Series: The column with dates standardized to '%d/%m/%Y'.
    """
    column_ok = pd.to_datetime(column, errors='coerce', format="%d/%m/%Y").notnull()
    column_defect = pd.to_datetime(column, errors='coerce', format="%d/%m/%Y").isnull()

    standardized_ok = pd.to_datetime(column[column_ok], format='%d/%m/%Y')
    standardized_defect = pd.to_datetime(column[column_defect], format="%Y-%d-%m %H:%M:%S")
    standardized_defect = pd.to_datetime(standardized_defect, format='%d/%m/%Y')

    standardized_column = pd.concat([standardized_ok, standardized_defect]).sort_index()

    return standardized_column

def create_template_data(our_template: pd.DataFrame) -> pd.DataFrame:
    """
    Creates the msd_template by mapping columns from our_template based on predefined column mappings.
    
    Args:
        our_template (pd.DataFrame): The source DataFrame.
    
    Returns:
        pd.DataFrame: The created template DataFrame.
    """
    # Define column mappings
    column_mappings = {
     'HH Name': 'الاسم',
        'HH Nid': 'رقم الهوية',
        'HH Date of Birth': 'تاريخ الميلاد',
        'HH Gender': 'الجنس',
        'Total Members': 'عدد الافراد',
        'HH Age ': 'عمر رب الاسرة',
        'Mobile Number': 'رقم الموبايل',
        'M 0-23 months': 'ذكور من 0 -23 شهر',
        'M 24-59 months': 'ذكور من 24 -59 شهر',
        'M 5-11 years': 'ذكور من6 - 11 سنة',
        'M 12-17 years': 'ذكور من12 - 17 سنة',
        'M 18-59 years': 'ذكور من18 - 59 سنة',
        'M 60+ years': 'ذكور من 60 سنة فما فوق',
        'F 0-23 months': 'اناث من 0 -23 شهر',
        'F 24-59 months': 'اناث من 24 -59 شهر',
        'F 5-11 years': 'اناث من6 - 11 سنة',
        'F 12-17 years': 'اناث من12 - 17 سنة',
        'F 18-59 years': 'اناث من18 - 59 سنة',
        'F 60+ years': 'اناث من 60 سنة فما فوق',
        'Partner': 'Partner'
    }

    # Create a template DataFrame with the mapped column names
    msd_template = pd.DataFrame(columns=column_mappings.values())
    
    # Populate the msd_template DataFrame with data from our_template
    for source_col, target_col in column_mappings.items():
        if source_col in our_template.columns:
            msd_template[target_col] = our_template[source_col]

    # Set constant values
    msd_template['الوكيل'] = 'رب الأسرة نفسه'
    msd_template['الباحث'] = ''
    msd_template['نوع المساعدة'] = 'بطاقة إلكترونية'
    msd_template['الفعالية'] = 'فعال'

    return msd_template

def add_code_column(template_df: pd.DataFrame, locality_column: str) -> pd.DataFrame:
    """
    Adds a 'code' column to the template dataframe by mapping localities to codes using two dictionaries.
    
    Args:
        template_df (pd.DataFrame): The DataFrame to which the 'code' column will be added.
        locality_column (str): The name of the column in the template_df with localities to map.
    
    Returns:
        pd.DataFrame: Updated DataFrame with the 'code' column.
    """
    dict1, dict2 = load_dicts()  # Load the dictionaries from SQL
    template_df['code'] = template_df[locality_column].map(dict1)
    template_df['code'] = template_df[locality_column].map(dict2).where(template_df['code'].isna(), template_df['code'])

    return template_df

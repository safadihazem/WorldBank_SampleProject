from data_loader import load_data_from_sql_server
from data_processing import create_template_data, add_code_column, standardize_date_column
from gender_fill import fill_missing_gender
import pandas as pd

def main():
    # Load raw data from SQL Server
    query = "SELECT * FROM your_table_name"
    raw_data = load_data_from_sql_server(query)

    # Fill missing gender values
    raw_data = fill_missing_gender(data, col_name='HH Name', gender_col='HH Gender')

    # Standardize the 'HH Date of Birth' column
    raw_data['HH Date of Birth'] = standardize_date_column(raw_data['HH Date of Birth'])

    # Create the MSD template using the mapping function
    msd_template = create_template_data(our_template)

    # Add the 'code' column
    final_data = add_code_column(template_data, 'LOCALITY')

    # Write the result to the database

if __name__ == "__main__":
    main()

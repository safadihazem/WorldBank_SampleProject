import pyodbc
import pandas as pd
from ..config.config import SQL_SERVER_CONFIG  # Import SQL Server configuration

def load_data_from_sql_server(query: str) -> pd.DataFrame:
    """
    Loads data from a SQL Server database into a pandas DataFrame.
    
    Args:
        query (str): The SQL query string to fetch data from the database.
    
    Returns:
        pd.DataFrame: The data loaded into a pandas DataFrame.
    """
    # Build the connection string using the values from SQL_SERVER_CONFIG
    connection_string = f"DRIVER={SQL_SERVER_CONFIG['driver']};" \
                        f"SERVER={SQL_SERVER_CONFIG['server']};" \
                        f"PORT={SQL_SERVER_CONFIG['port']};" \
                        f"DATABASE={SQL_SERVER_CONFIG['database']};" \
                        f"UID={SQL_SERVER_CONFIG['uid']};" \
                        f"PWD={SQL_SERVER_CONFIG['pwd']}"

    # Establish the connection to the SQL Server
    try:
        connection = pyodbc.connect(connection_string)
        print("Connected to the database successfully.")
    except pyodbc.Error as e:
        print(f"Error connecting to the database: {e}")
        raise
    
    # Execute the query and load the data into a DataFrame
    try:
        df = pd.read_sql(query, connection)
        print("Data successfully loaded.")
    except Exception as e:
        print(f"Error executing query: {e}")
        raise
    finally:
        # Close the connection
        connection.close()
    
    return df

import pandas as pd
import sqlite3


def csv_to_sqlite(csv_file: str, db_file: str, table_name: str) -> None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(db_file)

    # Write the data to a table named `table_name`
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()


# Define file paths
csv_file = r'C:\Users\David\PycharmProjects\HW17-Fattal-David\E-commerce.csv'  # Path to your CSV file
db_file = r'C:\Users\David\PycharmProjects\HW17-Fattal-David\E-commerce_db.db'
table_name = 'customers'

# Convert CSV to SQLite
csv_to_sqlite(csv_file, db_file, table_name)

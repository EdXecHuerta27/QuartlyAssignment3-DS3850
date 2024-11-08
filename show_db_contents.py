import sqlite3

# Connect to the database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Function to list all tables in the database
def list_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(f"- {table[0]}")

# Function to display contents of each table
def display_table_contents():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        print(f"\nContents of table: {table_name}")
        
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = [description[1] for description in cursor.fetchall()]
        print(f"Columns: {', '.join(columns)}")
        
        # Retrieve all data in the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        # Display each row of the table
        for row in rows:
            row_data = dict(zip(columns, row))
            print(row_data)
            
        if not rows:
            print("No data in this table.")

# List tables and display their contents
list_tables()
display_table_contents()

# Close the connection
conn.close()

import sqlite3

# Connect to the database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()


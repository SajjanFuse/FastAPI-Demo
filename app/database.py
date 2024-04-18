import sqlite3 

connection = sqlite3.connect('data.db')
cursor = connection.cursor() 

# basic creation of an empty schema in the database
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
);      
""")

connection.commit()
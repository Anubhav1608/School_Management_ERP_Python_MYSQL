import mysql.connector
from mysql.connector import Error

def Create_Connection(Host_Name, User_Name, User_Password, DB_Name=None):
    Connection = None
    try:
        if DB_Name:
            Connection = mysql.connector.connect(
                host=Host_Name,
                user=User_Name,
                password=User_Password,
                database=DB_Name
            )
        else:
            Connection = mysql.connector.connect(
                host=Host_Name,
                user=User_Name,
                password=User_Password
            )
        print("Connection To MySQL DB successful")
    except Error as e:
        print(f"The Error '{e}' Occurred")
    return Connection

def Execute_Query(Connection, Query):
    Cursor = Connection.cursor()
    try:
        Cursor.execute(Query)
        Connection.commit()
        print("Query Executed Successfully")
    except Error as e:
        print(f"The Error '{e}' Occurred")

Host = "127.0.0.1" 
User    = "ANUBHAV1608"
Password = "123456@ASD"

Connection = Create_Connection(Host, User, Password)

Create_Database_Query = "CREATE DATABASE IF NOT EXISTS School_Management"
Execute_Query(Connection, Create_Database_Query)

Connection = Create_Connection(Host, User, Password, "School_Management")

Create_Circulars_Table = """
CREATE TABLE IF NOT EXISTS School_Circulars (
    Circular_ID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Content TEXT,
    File_Path VARCHAR(255),
    Is_Active BOOLEAN DEFAULT TRUE,
    Is_Deleted BOOLEAN DEFAULT FALSE,
    Is_Archived BOOLEAN DEFAULT FALSE,
    Is_Pinned BOOLEAN DEFAULT FALSE,
    Created_By INT NOT NULL, 
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Created_By) REFERENCES Users_DataBase(User_ID) ON DELETE CASCADE 
);
"""
Execute_Query(Connection, Create_Circulars_Table)

if Connection:
    Connection.close()
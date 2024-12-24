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

Create_Event_Categories_Table = """
CREATE TABLE IF NOT EXISTS School_Event_Categories (
    Category_ID INT AUTO_INCREMENT PRIMARY KEY,
    Category_Name VARCHAR(50) NOT NULL UNIQUE,
    Description TEXT
);
"""
Execute_Query(Connection, Create_Event_Categories_Table)

Create_Events_Table = """
CREATE TABLE IF NOT EXISTS School_Events (
    Event_ID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Description TEXT,
    Event_Date DATE NOT NULL,
    Start_Time TIME,
    End_Time TIME,
    Category_ID INT,
    Created_By INT NOT NULL, 
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Category_ID) REFERENCES School_Event_Categories(Category_ID) ON DELETE SET NULL,
    FOREIGN KEY (Created_By) REFERENCES Users_DataBase(User_ID) ON DELETE CASCADE 
);
"""

Execute_Query(Connection, Create_Events_Table)

if Connection:
    Connection.close()
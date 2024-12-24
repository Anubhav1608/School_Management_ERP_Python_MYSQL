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
User  = "ANUBHAV1608"
Password = "123456@ASD"

Connection = Create_Connection(Host, User, Password)

Connection = Create_Connection(Host, User, Password, "School_Management")

Create_Lost_Items_Table = """
CREATE TABLE IF NOT EXISTS Lost_Items (
    Lost_Item_ID INT AUTO_INCREMENT PRIMARY KEY,
    Item_Description TEXT NOT NULL,
    Reported_By INT NOT NULL,
    Reported_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Is_Claimed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (Reported_By) REFERENCES Users_DataBase(User_ID) ON DELETE CASCADE
);
"""
Execute_Query(Connection, Create_Lost_Items_Table)

Create_Found_Items_Table = """
CREATE TABLE IF NOT EXISTS Found_Items (
    Found_Item_ID INT AUTO_INCREMENT PRIMARY KEY,
    Item_Description TEXT NOT NULL,
    Found_By INT NOT NULL,
    Found_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Is_Claimed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (Found_By) REFERENCES Users_DataBase(User_ID) ON DELETE CASCADE
);
"""
Execute_Query(Connection, Create_Found_Items_Table)

Create_Claims_Table = """
CREATE TABLE IF NOT EXISTS Claims_For_LOST_AND_FOUND_ITEMS (
    Claim_ID INT AUTO_INCREMENT PRIMARY KEY,
    Lost_Item_ID INT,
    Found_Item_ID INT,
    Claimed_By INT NOT NULL, 
    Claimed_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Lost_Item_ID) REFERENCES Lost_Items(Lost_Item_ID) ON DELETE CASCADE,
    FOREIGN KEY (Found_Item_ID) REFERENCES Found_Items(Found_Item_ID) ON DELETE CASCADE,
    FOREIGN KEY (Claimed_By) REFERENCES Users_DataBase(User_ID) ON DELETE CASCADE
);
"""
Execute_Query(Connection, Create_Claims_Table)

if Connection:
    Connection.close()
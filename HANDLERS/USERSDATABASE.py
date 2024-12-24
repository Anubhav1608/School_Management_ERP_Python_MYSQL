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

def Create_Users_Table(Connection):
    Create_Users_Table_Query = """
    CREATE TABLE IF NOT EXISTS Users_DataBase (
        User_ID INT PRIMARY KEY,  -- Removed AUTO_INCREMENT to allow specific IDs
        Name VARCHAR(100) NOT NULL,
        Email VARCHAR(100) NOT NULL UNIQUE,
        Role ENUM('Principal', 'Vice Principal', 'Coordinator', 'Staff', 'Student', 'Parent', 'Admin') NOT NULL,
        Contact VARCHAR(15),
        Password VARCHAR(255) NOT NULL,
        Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Profile_ID INT,  
        Profile_Type ENUM('Principal', 'Vice Principal', 'Coordinator', 'Staff', 'Student') NOT NULL,
        FOREIGN KEY (Profile_ID) REFERENCES Principals_Profile(Principal_ID) ON DELETE CASCADE,
        FOREIGN KEY (Profile_ID) REFERENCES Vice_Principals_Profile(Vice_Principal_ID) ON DELETE CASCADE,
        FOREIGN KEY (Profile_ID) REFERENCES Coordinators_Profile(Coordinator_ID) ON DELETE CASCADE,
        FOREIGN KEY (Profile_ID) REFERENCES Staff_Profile(Staff_ID) ON DELETE CASCADE,
        FOREIGN KEY (Profile_ID) REFERENCES Students_Profile(Admission_Number) ON DELETE CASCADE
    );
    """
    Execute_Query(Connection, Create_Users_Table_Query)

Host = "127.0.0.1" 
User     = "ANUBHAV1608"
Password = "123456@ASD"

Connection = Create_Connection(Host, User, Password)

Create_Database_Query = "CREATE DATABASE IF NOT EXISTS School_Management"
Execute_Query(Connection, Create_Database_Query)

Connection = Create_Connection(Host, User, Password, "School_Management")

Create_Users_Table(Connection)

if Connection:
    Connection.close()
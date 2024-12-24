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
User   = "ANUBHAV1608"
Password = "123456@ASD"

Connection = Create_Connection(Host, User, Password)

Create_Database_Query = "CREATE DATABASE IF NOT EXISTS School_Management"
Execute_Query(Connection, Create_Database_Query)

Connection = Create_Connection(Host, User, Password, "School_Management")

Create_Principals_Profile_Table = """
CREATE TABLE IF NOT EXISTS Principals_Profile (
    Principal_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Gender VARCHAR(10),
    School_Email VARCHAR(100),
    Contact VARCHAR(15),
    Address TEXT,
    Nationality VARCHAR(50),
    DOB DATE,
    Joining_Date DATE,
    Qualifications TEXT,
    Experience INT,
    Salary DECIMAL(10, 2),
    Performance_Reviews TEXT,
    Photo BLOB,
    Department VARCHAR(50),
    Office_Location VARCHAR(100),
    Emergency_Contact VARCHAR(15),
    Languages_Spoken TEXT,
    Date_of_Birth_Proof BLOB
);
"""

Execute_Query(Connection, Create_Principals_Profile_Table)

Create_Vice_Principals_Profile_Table = """
CREATE TABLE IF NOT EXISTS Vice_Principals_Profile (
    Vice_Principal_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Gender VARCHAR(10),
    School_Email VARCHAR(100),
    Contact VARCHAR(15),
    Address TEXT,
    Nationality VARCHAR(50),
    DOB DATE,
    Joining_Date DATE,
    Qualifications TEXT,
    Experience INT,
    Salary DECIMAL(10, 2),
    Performance_Reviews TEXT,
    Photo BLOB,
    Department VARCHAR(50),
    Office_Location VARCHAR(100),
    Emergency_Contact VARCHAR(15),
    Languages_Spoken TEXT,
    Date_of_Birth_Proof BLOB
);
"""

Execute_Query(Connection, Create_Vice_Principals_Profile_Table)

Create_Coordinators_Profile_Table = """
CREATE TABLE IF NOT EXISTS Coordinators_Profile (
    Coordinator_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Gender VARCHAR(10),
    School_Email VARCHAR(100),
    Contact VARCHAR(15),
    Address TEXT,
    Nationality VARCHAR(50),
    DOB DATE,
    Joining_Date DATE,
    Qualifications TEXT,
    Experience INT,
    Salary DECIMAL(10, 2),
    Performance_Reviews TEXT,
    Photo BLOB,
    Department VARCHAR(50),
    Office_Location VARCHAR(100),
    Emergency_Contact VARCHAR(15),
    Languages_Spoken TEXT,
    Date_of_Birth_Proof BLOB
);
"""

Execute_Query(Connection, Create_Coordinators_Profile_Table)

Create_Staff_Profile_Table = """
CREATE TABLE IF NOT EXISTS Staff_Profile (
    Staff_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Gender VARCHAR(10),
    School_Email VARCHAR(100),
    Contact VARCHAR(15),
    Address TEXT,
    Nationality VARCHAR(50),
    DOB DATE,
    Joining_Date DATE,
    Designation VARCHAR(50),
    Salary DECIMAL(10, 2),
    Performance_Reviews TEXT,
    Photo BLOB,
    Department VARCHAR(50),
    Office_Location VARCHAR(100),
    Emergency_Contact VARCHAR(15),
    Languages_Spoken TEXT,
    Date_of_Birth_Proof BLOB
);
"""

Execute_Query (Connection, Create_Staff_Profile_Table)

if Connection:
    Connection.close()
    print("MySQL Connection Is Closed")
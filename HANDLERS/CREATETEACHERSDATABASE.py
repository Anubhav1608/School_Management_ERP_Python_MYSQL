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

Create_Database_Query = "CREATE DATABASE IF NOT EXISTS School_Management"
Execute_Query(Connection, Create_Database_Query)

Connection = Create_Connection(Host, User, Password, "School_Management")

Create_Teachers_Profile_Table = """
CREATE TABLE Teachers_Profile (
    Teacher_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Gender VARCHAR(10),
    School_Email VARCHAR(100),
    Teacher_Email VARCHAR(100),
    Address TEXT,
    Blood_Group VARCHAR(10),
    Emergency_Contact VARCHAR(15),
    Nationality VARCHAR(50),
    Address_Line2 TEXT,
    City VARCHAR(50),
    State VARCHAR(50),
    Postal_Code VARCHAR(10),
    Photo BLOB,
    TPIN VARCHAR(20) NOT NULL,
    DOB DATE,
    Contact VARCHAR(15),
    Qualifications TEXT,
    Designation VARCHAR(50),
    Subject_Taught VARCHAR(100),
    Subjects_Specialization TEXT,
    Years_of_Experience INT,
    Joining_Date DATE,
    Last_Promotion_Date DATE,
    Salary DECIMAL(10, 2),
    Performance_Reviews TEXT,
    Professional_Development TEXT,
    Teaching_Philosophy TEXT
);
"""

Execute_Query(Connection, Create_Teachers_Profile_Table)

Create_Certificates_Table = """
CREATE TABLE Teachers_Certificates (
    Certificate_ID INT AUTO_INCREMENT PRIMARY KEY,
    Teacher_ID INT,
    Certificate_Name VARCHAR(100),
    Certificate_File BLOB,
    Issuing_Organization VARCHAR(100),
    Issue_Date DATE,
    Expiration_Date DATE,
    Description TEXT,
    FOREIGN KEY (Teacher_ID) REFERENCES Teachers_Profile(Teacher_ID) ON DELETE CASCADE
);
"""

Execute_Query(Connection, Create_Certificates_Table)

if Connection:
    Connection.close()
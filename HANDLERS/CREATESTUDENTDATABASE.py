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
User = "ANUBHAV1608"
Password = "123456@ASD"

Connection = Create_Connection(Host, User, Password)

Create_Database_Query = "CREATE DATABASE School_Management"
Execute_Query(Connection, Create_Database_Query)

Connection = Create_Connection(Host, User, Password, "School_Management")

Create_Students_Profile_Table = """
CREATE TABLE Students_Profile (
    Admission_Number INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Father_Name VARCHAR(100),
    Mother_Name VARCHAR(100),
    Address TEXT,
    Contact VARCHAR(15),
    Emergency_Contact VARCHAR(15),
    Nationality VARCHAR(50),
    Gender VARCHAR(10),
    Student_School_Email VARCHAR(100),
    Parents_Email VARCHAR(100),
    School_House VARCHAR(50),
    DOB DATE,
    Date_of_Admission DATE,
    Previous_School VARCHAR(100),
    Current_Class VARCHAR(10),
    Current_Class_Section VARCHAR(10),
    Blood_Group VARCHAR(10),
    Current_Class_Roll_Number INT,
    Extracurricular_Activities TEXT,
    Medical_History TEXT,
    Allergies TEXT,
    Photo BLOB,
    Aadhar_Card BLOB,
    Father_Aadhar_Card BLOB,
    Mother_Aadhar_Card BLOB,
    Birth_Certificate BLOB,
    Transfer_Certificate BLOB,
    Father_Occupation VARCHAR(100),
    Mother_Occupation VARCHAR(100),
    Performance_Reports BLOB,
    Scholarship_Status VARCHAR(50),
    Language_Proficiency TEXT
);
"""

Execute_Query(Connection, Create_Students_Profile_Table)

if Connection:
    Connection.close()
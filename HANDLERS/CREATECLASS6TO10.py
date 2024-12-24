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

while True:
    Class_Num = input("Enter The Class Number (6-10) or Type 'Exit' To Quit: ")
    
    if Class_Num.upper() == 'EXIT':
        break
    
    if Class_Num not in ['6', '7', '8', '9', '10']:
        print("Invalid Class Number. Please Enter A Number Between 6 and 10.")
        continue

    Section = input("Enter The Section (A, B, C, D): ").upper()
    
    if Section not in ['A', 'B', 'C', 'D']:
        print("Invalid Section. Please Enter A, B, C, or D.")
        continue

    Class_Name = f"Class_{Class_Num}_{Section}"

    Class_Teacher_Id = input("Enter the Class Teacher ID: ")

    Create_Class_Table = f"""
    CREATE TABLE IF NOT EXISTS {Class_Name} (
        Class_ID INT AUTO_INCREMENT PRIMARY KEY,
        Class_Teacher_Id INT NULL,  -- Allow NULL for foreign key
        Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (Class_Teacher_Id) REFERENCES Teachers_Profile(Teacher_ID) ON DELETE SET NULL
    );
    """
    Execute_Query(Connection, Create_Class_Table)

    Create_Students_Table = f"""
    CREATE TABLE IF NOT EXISTS Students_{Class_Name} (
        Student_ID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100) NOT NULL,
        Roll_Number INT NOT NULL UNIQUE,
        Email VARCHAR(100) NOT NULL UNIQUE,
        Contact VARCHAR(15),
        Class_ID INT NOT NULL,
        Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (Class_ID) REFERENCES {Class_Name}(Class_ID) ON DELETE CASCADE
    );
    """
    Execute_Query(Connection, Create_Students_Table)

    Create_Attendance_Table = f"""
    CREATE TABLE IF NOT EXISTS Attendance_{Class_Name} (
        Attendance_ID INT AUTO_INCREMENT PRIMARY KEY,
        Student_ID INT NOT NULL,
        Attendance_Date DATE NOT NULL,
        Status ENUM('Present', 'Absent') NOT NULL,
        Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE (Student_ID, Attendance_Date),  -- Ensure unique attendance record per student per day
        FOREIGN KEY (Student_ID) REFERENCES Students_{Class_Name}(Student_ID) ON DELETE CASCADE
    );
    """
    Execute_Query(Connection, Create_Attendance_Table)

    Create_Subject_Teachers_Table = f"""
    CREATE TABLE IF NOT EXISTS Subject_Teachers_{Class_Name} (
        Subject_Teacher_ID INT AUTO_INCREMENT PRIMARY KEY,
        Teacher_ID INT NOT NULL,
        Class_ID INT NOT NULL,
        Class_Name VARCHAR(50) NOT NULL,  -- Added Class_Name to identify the class
        Subject VARCHAR(100) NOT NULL,
        Created_At TIM ESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (Teacher_ID) REFERENCES Teachers_Profile(Teacher_ID) ON DELETE CASCADE,
        FOREIGN KEY (Class_ID) REFERENCES {Class_Name}(Class_ID) ON DELETE CASCADE
    );
    """
    Execute_Query(Connection, Create_Subject_Teachers_Table)

if Connection:
    Connection.close()
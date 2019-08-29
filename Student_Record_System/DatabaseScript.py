import sqlite3
# This will be the backend script to handle all the methods and functions subject to the Database


def studentResults():
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE studentRecord(id INTEGER PRIMARY KEY, \
     StdID text, FirstName text, Lastname text, Course text, Maths text, English text, \
     AdvancedMaths text, Economics text, Accounting text, Geography text, \
     Biology text, PhysScience text, Chemistry text, TotalGrade text, Average text, ClassRank text)")
    con.commit()
    con.close()

def addStudent(StdID, FirstName, Lastname, Course, Maths, English, AdvancedMaths, Economics, Accounting, Geography,
                Biology, PhysScience, Chemistry, TotalGrade, Average, ClassRank):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("INSERT INTO studentRecord VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                (StdID, FirstName, Lastname, Course, Maths, English, AdvancedMaths, Economics, Accounting, Geography, Biology, PhysScience, Chemistry, TotalGrade, Average, ClassRank))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM studentRecord")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteData(id):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("DELETE FROM studentRecord WHERE id=?", (id,))
    con.commit()
    con.close()

def searchDatabase(StdID):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM studentRecord WHERE StdID=?", (StdID,))
    rows=cur.fetchall()
    con.close()
    return rows


def updateDatabase(StdID = "", FirstName = "", Lastname = "",Course = "", Maths = "", English = "", AdvancedMaths = "", Economics = "", Accounting = "", \
                   Geography = "",Biology = "",PhysScience = "",Chemistry = "", TotalGrade = "", Average = "", ClassRank = "" ):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("UPDATE studentRecord SET StdID=? OR, FirstName=? OR, Lastname=? OR, Course=? OR, Maths=? OR, English=? OR, AdvancedMaths=? OR, Economics=? OR, \
                Accounting=? OR, Geography=? OR, Biology=? OR, PhysScience=? OR, Chemistry=? OR, TotalGrade=? OR, Averaged=? OR, ClassRank=? ", (StdID, FirstName, Lastname, \
                Course, Maths, English, AdvancedMaths, Economics, Accounting, Geography, Biology, PhysScience, Chemistry, TotalGrade, Average, ClassRank))
    rows=cur.fetchall()
    con.close()



# def UpdateDatabase():

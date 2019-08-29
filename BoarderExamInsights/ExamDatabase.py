import sqlite3


import sqlite3
# This will be the backend script to handle all the methods and functions subject to the Database


def studentResults():
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE studentRecord(id INTEGER PRIMARY KEY, \
     FirstName text, Lastname text, YearLevel text, Sub1 text, Sub2 text, \
     Sub3 text, Sub4 text, Sub5 text, Sub6 text, \
     Sub7 text, Sub8 text, Conf1 text, Conf2 text, \
     Conf3 text, Conf4 text, Conf5 text, Conf6 text, \
     Conf7 text, Conf8 text, TotalConf text, AverageConf text)")
    con.commit()
    con.close()

def addStudent(FirstName, Lastname, YearLevel, Sub1, Sub2, Sub3, Sub4, Sub5, Sub6, Sub7,
                Sub8, Conf1, Conf2, Conf3, Conf4, Conf5, Conf6, Conf7, Conf8, TotalConf, AverageConf):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("INSERT INTO studentRecord VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                (FirstName, Lastname, YearLevel, Sub1, Sub2, Sub3, Sub4, Sub5, Sub6, Sub7, Sub8, Conf1, Conf2, Conf3, Conf4, Conf5, Conf6, Conf7, Conf8, TotalConf, AverageConf))
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

def searchDatabase(FirstName):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM studentRecord WHERE FirstName=?", (FirstName,))
    rows=cur.fetchall()
    con.close()
    return rows


# studentResults()


# def updateDatabase(FirstName, Lastname, YearLevel, Sub1, Sub2, Sub3, Sub4, Sub5, Sub6, Sub7,
#                 Sub8, Conf1, Conf2, Conf3, Conf4, Conf5, Conf6, Conf7, Conf8, TotalConf, AverageConf ):
#     con = sqlite3.connect("studentRecord.db")
#     cur = con.cursor()
#     cur.execute("UPDATE studentRecord SET StdID=? OR, FirstName=? OR, Lastname=? OR, Course=? OR, Maths=? OR, English=? OR, AdvancedMaths=? OR, Economics=? OR, \
#                 Accounting=? OR, Geography=? OR, Biology=? OR, PhysScience=? OR, Chemistry=? OR, TotalGrade=? OR, Averaged=? OR, ClassRank=? ", (StdID, FirstName, Lastname, \
#                 Course, Maths, English, AdvancedMaths, Economics, Accounting, Geography, Biology, PhysScience, Chemistry, TotalGrade, Average, ClassRank))
#     rows=cur.fetchall()
#     con.close()

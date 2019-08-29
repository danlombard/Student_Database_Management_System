#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:48:00 2019

@author: daniel
"""
from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import datetime
import time
import DatabaseScript
#Frontend

class Student:

   def __init__(self,root):
       self.root = root
       self.root.title("Student Records Database System")
       self.root.geometry("1350x750")
       self.root.config(bg="#B5644C")



       StdID = StringVar()
       FirstName = StringVar()
       Lastname = StringVar()
       Course = StringVar()
       English = StringVar()
       PhysScience = StringVar()
       Chemistry = StringVar()
       Biology = StringVar()
       Maths = StringVar()
       AdvancedMaths = StringVar()
       Economics = StringVar()
       Accounting = StringVar()
       Geography = StringVar()
       TotalGrade = StringVar()
       Average = StringVar()
       ClassRank = StringVar()
       DateOfIssue = StringVar()

       #============================================== FUNCTIONS ==================================================================================

       def Exit():
           ExitCommand = tkinter.messagebox.askyesno("Quit Student Management System", "Do you want to quit?")
           if ExitCommand > 0:
               root.destroy()
               return

       def Clear():
            StdID.set("")
            FirstName.set("")
            Lastname.set("")
            Course.set("")
            English.set("")
            PhysScience.set("")
            Chemistry.set("")
            Biology.set("")
            Maths.set("")
            AdvancedMaths.set("")
            Economics.set("")
            Accounting.set("")
            Geography.set("")
            TotalGrade.set("")
            Average.set("")
            ClassRank.set("")


       def AverageScore():

            subjectCount = 0
            ScoreSum = 0
            if Maths.get() != '':
                unit1 = float(Maths.get())
                ScoreSum += unit1
                subjectCount += 1
            if PhysScience.get() != '':
                unit2 = float(PhysScience.get())
                ScoreSum += unit2
                subjectCount +=1
            if Chemistry.get() != '':
                unit3 = float(Chemistry.get())
                ScoreSum += unit3
                subjectCount +=1
            if Biology.get() != '':
                unit4 = float(Biology.get())
                ScoreSum += unit4
                subjectCount +=1
            if AdvancedMaths.get() != '':
                unit5 = float(AdvancedMaths.get())
                ScoreSum += unit5
                subjectCount +=1
            if Economics.get() != '':
                unit6 = float(Economics.get())
                ScoreSum += unit6
                subjectCount +=1
            if Accounting.get() != '':
                unit7 = float(Accounting.get())
                ScoreSum += unit7
                subjectCount +=1
            if Geography.get() != '':
                unit8 = float(Geography.get())
                ScoreSum += unit8
                subjectCount +=1
            if English.get() != '':
                unit9 = float(English.get())
                ScoreSum += unit9
                subjectCount +=1

            UnitAverage = ScoreSum/subjectCount
            UnitTotal = ScoreSum
            TotalGrade.set(UnitTotal)
            Average.set(UnitAverage)

            if (UnitAverage >= 80):
                ClassRank.set("High Distinction")
            elif (UnitAverage >= 70):
                ClassRank.set("Distinction")
            elif (UnitAverage >= 60):
                ClassRank.set("Credit")
            elif (UnitAverage >= 50):
                ClassRank.set("Pass")
            elif (UnitAverage >= 40):
                ClassRank.set("Fail")

            DateOfIssue.set(time.strftime("%d/%m/%Y"))
            self.textSummary.delete('1.0', END)
            self.textSummary.insert(END, 'Student ID: \t  '  + StdID.get() + '\t  ' + DateOfIssue.get() + '\n')
            self.textSummary.insert(END, 'Firstname: \t  '  + FirstName.get() + '\t  ' + '\n')
            self.textSummary.insert(END, 'Surname: \t  '  + Lastname.get() + '\t  ' + '\n')
            self.textSummary.insert(END, '========================================='  + '\n')

            if Maths.get() != '':
                self.textSummary.insert(END, 'Maths: \t\t\t  '  + Maths.get() + '\t  ' + '\n')
            if PhysScience.get() != '':
                self.textSummary.insert(END, 'Physical Sciences: \t\t\t  '  + PhysScience.get() + '\t  ' + '\n')
            if Chemistry.get() != '':
                self.textSummary.insert(END, 'Chemistry: \t\t\t  '  + Chemistry.get() + '\t  ' + '\n')
            if Biology.get() != '':
                self.textSummary.insert(END, 'Biology: \t\t\t  '  + Biology.get() + '\t  ' +  '\n')
            if AdvancedMaths.get() != '':
                self.textSummary.insert(END, 'Advanced Maths: \t\t\t  '  + AdvancedMaths.get() + '\t  ' +  '\n')
            if Economics.get() != '':
                self.textSummary.insert(END, 'Economics: \t\t\t  '  + Economics.get() + '\t  ' +  '\n')
            if Accounting.get() != '':
                self.textSummary.insert(END, 'Accounting: \t\t\t  '  + Accounting.get() + '\t  ' +  '\n')
            if Geography.get() != '':
                self.textSummary.insert(END, 'Geography: \t\t\t  '  + Geography.get() + '\t  ' +  '\n')
            if English.get() != '':
                self.textSummary.insert(END, 'English: \t\t\t  '  + English.get() + '\t  ' +  '\n')

            self.textSummary.insert(END, '========================================='  + '\n')
            self.textSummary.insert(END, 'Average: \t\t\t  '  + Average.get() + '\t  ' + '\n')
            self.textSummary.insert(END, 'Rank: \t\t\t '  + ClassRank.get() + '\t  ' + '\n')





       #============================================== Functions subject to the Database ====================================================================

       def addData():
           AverageScore()
           if(len(StdID.get()) != 0):
               DatabaseScript.addStudent(StdID.get(), FirstName.get(), Lastname.get(), Course.get(), Maths.get(), English.get(), AdvancedMaths.get(), Economics.get(), Accounting.get(), Geography.get(),
                               Biology.get(), PhysScience.get(), Chemistry.get(), TotalGrade.get(), Average.get(), ClassRank.get())
               StudentList.delete(0, END)
               StudentList.insert(END, (StdID.get(), FirstName.get(), Lastname.get(), Course.get(), Maths.get(), English.get(), AdvancedMaths.get(), Economics.get(), Accounting.get(), Geography.get(),
                               Biology.get(), PhysScience.get(), Chemistry.get(), TotalGrade.get(), Average.get(), ClassRank.get()))

       def searchDb():
           StudentList.delete(0, END)
           for row in DatabaseScript.searchDatabase(StdID.get()):
               StudentList.insert(END, row, str(""))

       def DisplayData():
           StudentList.delete(0, END)
           for row in DatabaseScript.viewData():
               StudentList.insert(END, row, str(""))

       def DeleteData():
           if(len(StdID.get()) != 0):
               DatabaseScript.deleteData(sd[0])
               Clear()
               DisplayData()

       def updateDb():
           if (len(StdID.get())!= 0):
               DatabaseScript.deleteData(sd[0])
           if (len(StdID.get())!= 0):
               DatabaseScript.addStudent(StdID.get(), FirstName.get(), Lastname.get(), Course.get(), Maths.get(), English.get(), AdvancedMaths.get(), Economics.get(), Accounting.get(), Geography.get(),
                               Biology.get(), PhysScience.get(), Chemistry.get(), TotalGrade.get(), Average.get(), ClassRank.get())
               StudentList.delete(0, END)
               StudentList.insert(END, (StdID.get(), FirstName.get(), Lastname.get(), Course.get(), Maths.get(), English.get(), AdvancedMaths.get(), Economics.get(), Accounting.get(), Geography.get(),
                               Biology.get(), PhysScience.get(), Chemistry.get(), TotalGrade.get(), Average.get(), ClassRank.get()))
           AverageScore()

       def StdRecord(event):
           global sd
           studentSearch = StudentList.curselection()[0]
           sd = StudentList.get(studentSearch)

           self.TextStd.delete(0, END)
           self.TextStd.insert(END, sd[1])
           self.TextFirstName.delete(0, END)
           self.TextFirstName.insert(END, sd[2])
           self.TextLastName.delete(0, END)
           self.TextLastName.insert(END, sd[3])
           self.cbCourse.delete(0, END)
           self.cbCourse.insert(END, sd[4])
           self.TextMaths.delete(0, END)
           self.TextMaths.insert(END, sd[5])
           self.TextEng.delete(0, END)
           self.TextEng.insert(END, sd[6])
           self.TextAdMaths.delete(0, END)
           self.TextAdMaths.insert(END, sd[7])
           self.TextEco.delete(0, END)
           self.TextEco.insert(END, sd[8])
           self.TextAcc.delete(0, END)
           self.TextAcc.insert(END, sd[9])
           self.TextGeo.delete(0, END)
           self.TextGeo.insert(END, sd[10])
           self.TextBio.delete(0, END)
           self.TextBio.insert(END, sd[11])
           self.TextPs.delete(0, END)
           self.TextPs.insert(END, sd[12])
           self.TextChem.delete(0, END)
           self.TextChem.insert(END, sd[13])
           self.TextTotalGrade.delete(0, END)
           self.TextTotalGrade.insert(END, sd[14])
           self.TextAvg.delete(0, END)
           self.TextAvg.insert(END, sd[15])
           self.TextRank.delete(0, END)
           self.TextRank.insert(END, sd[16])



       #============================================== Main Frame ====================================================================#

       MainFrame = Frame(self.root, bg = "#43414E")
       MainFrame.grid()

       DF1 = Frame(MainFrame, bd = 1, width = 1350, height = 400, padx = 20, pady = 20, relief = RIDGE, bg = "#43414E")
       DF1.pack(side = BOTTOM)

       DF2 = Frame(DF1, bd = 1, width = 1350, height = 200, padx = 20, pady = 20, bg = "#ddd5d3")
       DF2.pack(side = TOP)

       DFButton = Frame(DF1, bd = 1, width = 1350, height = 200, padx = 55, pady = 10, relief = RIDGE, bg = "#ddd5d3")
       DFButton.pack(side = BOTTOM)

       DF = Frame(MainFrame, bd = 1, width = 1350, height = 400, padx = 20, pady = 20, relief = RIDGE, bg = "#43414E")
       DF.pack(side = TOP)

       DFLeft = LabelFrame(DF, bd = 1, width = 450, height = 200, padx = 20, pady = 5,  relief = RIDGE, bg = "#ddd5d3",
                            font = ('Open Sans', 25), text = "Student Details")
       DFLeft.pack(side = LEFT)

       DFRight = LabelFrame(DF, bd = 1, width = 450, height = 200, padx = 20, pady = 15, relief = RIDGE, bg = "#ddd5d3",
                            font = ('Open Sans', 25), text = "Academic Summary")
       DFRight.pack(side = RIGHT)

       #============================================== WIDGET ==================================================================================#
       self.lblStd = Label(DFLeft, font = ('Open Sans', 15), text = "Student ID", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblStd.grid(row = 0, column = 0, sticky = W)
       self.TextStd = Entry(DFLeft, font = ('Open Sans', 15), textvariable = StdID, bg = "#f7f7f7")
       self.TextStd.grid(row=0, column=1)

       self.lblFirstName = Label(DFLeft, font = ('Open Sans', 15), text = "First Name", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblFirstName.grid(row = 1, column = 0, sticky = W)
       self.TextFirstName = Entry(DFLeft, font = ('Open Sans', 15), textvariable = FirstName, bg = "#f7f7f7")
       self.TextFirstName.grid(row=1, column=1)

       self.lblLastName = Label(DFLeft, font = ('Open Sans', 15), text = "Last Name", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblLastName.grid(row = 2, column = 0, sticky = W)
       self.TextLastName = Entry(DFLeft, font = ('Open Sans', 15), textvariable = Lastname, bg = "#f7f7f7")
       self.TextLastName.grid(row=2, column=1)

       self.lblCourse = Label(DFLeft, font = ('Open Sans', 15), text = "Course Code", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblCourse.grid(row = 3, column = 0, sticky = W)
       self.cbCourse = ttk.Combobox(DFLeft, font = ('Open Sans', 15), textvariable = Course, state = 'readonly')
       self.cbCourse['value'] = (" ", "67823", "67824", "67825", "67826", "67827", "67828")
       self.cbCourse.current(0)
       self.cbCourse.grid(row=3, column = 1, padx=20)

       self.lblEng = Label(DFLeft, font = ('Open Sans', 15), text = "English", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblEng.grid(row = 4, column = 0, sticky = W)
       self.TextEng = Entry(DFLeft, font = ('Open Sans', 15), textvariable = English, bg = "#f7f7f7")
       self.TextEng.grid(row=4, column=1)

       self.lblPs = Label(DFLeft, font = ('Open Sans', 15), text = "Physical Science", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblPs.grid(row = 5, column = 0, sticky = W)
       self.TextPs = Entry(DFLeft, font = ('Open Sans', 15), textvariable = PhysScience, bg = "#f7f7f7")
       self.TextPs.grid(row=5, column=1)

       self.lblChem = Label(DFLeft, font = ('Open Sans', 15), text = "Chemistry", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblChem.grid(row = 6, column = 0, sticky = W)
       self.TextChem = Entry(DFLeft, font = ('Open Sans', 15), textvariable = Chemistry, bg = "#f7f7f7")
       self.TextChem.grid(row=6, column=1)

       self.lblBio = Label(DFLeft, font = ('Open Sans', 15), text = "Biology", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblBio.grid(row = 7, column = 0, sticky = W)
       self.TextBio = Entry(DFLeft, font = ('Open Sans', 15), textvariable = Biology, bg = "#f7f7f7")
       self.TextBio.grid(row=7, column=1)

       self.lblMaths = Label(DFLeft, font = ('Open Sans', 15), text = "Maths", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblMaths.grid(row = 0, column = 2, sticky = W)
       self.TextMaths = Entry(DFLeft, font = ('Open Sans', 15), textvariable = Maths, bg = "#f7f7f7")
       self.TextMaths.grid(row=0, column=3)

       self.lblAdMaths = Label(DFLeft, font = ('Open Sans', 15), text = "Advanced Maths", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblAdMaths.grid(row = 1, column = 2, sticky = W)
       self.TextAdMaths = Entry(DFLeft, font = ('Open Sans', 15), textvariable = AdvancedMaths, bg = "#f7f7f7")
       self.TextAdMaths.grid(row=1, column=3)

       self.lblEco = Label(DFLeft, font = ('Open Sans', 15), text = "Economics", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblEco.grid(row = 2, column = 2, sticky = W)
       self.TextEco = Entry(DFLeft, font = ('Open Sans', 15), textvariable = Economics, bg = "#f7f7f7")
       self.TextEco.grid(row=2, column=3)

       self.lblAcc = Label(DFLeft, font = ('Open Sans', 15), text = "Accounting", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblAcc.grid(row = 3, column = 2, sticky = W)
       self.TextAcc = Entry(DFLeft, font = ('Open Sans', 15), textvariable = Accounting, bg = "#f7f7f7")
       self.TextAcc.grid(row=3, column=3)

       self.lblGeo = Label(DFLeft, font = ('Open Sans', 15), text = "Geography", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblGeo.grid(row = 4, column = 2, sticky = W)
       self.TextGeo = Entry(DFLeft, font = ('Open Sans', 15), textvariable = Geography, bg = "#f7f7f7")
       self.TextGeo.grid(row=4, column=3)

       self.lblTotalGrade = Label(DFLeft, font = ('Open Sans', 15), text = "Total Grade", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblTotalGrade.grid(row = 5, column = 2, sticky = W)
       self.TextTotalGrade = Entry(DFLeft, font = ('Open Sans', 15), textvariable = TotalGrade, bg = "#f7f7f7")
       self.TextTotalGrade.grid(row=5, column=3)

       self.lblAvg = Label(DFLeft, font = ('Open Sans', 15), text = "Average", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblAvg.grid(row = 6, column = 2, sticky = W)
       self.TextAvg = Entry(DFLeft, font = ('Open Sans', 15), textvariable = Average, bg = "#f7f7f7")
       self.TextAvg.grid(row=6, column=3)

       self.lblRank = Label(DFLeft, font = ('Open Sans', 15), text = "Class Rank", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblRank.grid(row = 7, column = 2, sticky = W)
       self.TextRank = Entry(DFLeft, font = ('Open Sans', 15), textvariable = ClassRank, bg = "#f7f7f7")
       self.TextRank.grid(row=7, column=3)


        #============================================== Student Summary ==================================================================================

       self.textSummary = Text(DFRight, height = 22, width = 40, bd = 1, font=('Open Sans', 12))
       self.textSummary.grid(row = 0, column = 0)

        #============================================== List Box ==================================================================================

       scrollbar = Scrollbar(DF2)
       scrollbar.grid(row=0, column=1, sticky = 'ns')

       StudentList = Listbox(DF2, width = 141, height = 7, font = ('Open Sans', 12), yscrollcommand=scrollbar.set)
       StudentList.bind('<Double-Button>', StdRecord)


       StudentList.grid(row = 0, column = 0, padx = 8)
       scrollbar.config(command=StudentList.yview)

       #============================================== Button Frame ==================================================================================

       self.AddData = Button(DFButton, text = 'Add New', font = ('Open Sans', 12), height = 1, width = 16, bd = 2, padx = 13, command = addData)
       self.AddData.grid(row=0,column=0)

       self.DisplayData = Button(DFButton, text = 'Display', font = ('Open Sans', 12), height = 1, width = 16, bd = 2, padx = 13, command = DisplayData)
       self.DisplayData.grid(row=0,column=1)

       self.ClearData = Button(DFButton, text = 'Clear', font = ('Open Sans', 12), height = 1, width = 16, bd = 2, padx = 13, command = Clear)
       self.ClearData.grid(row=0,column=2)

       self.DeleteData = Button(DFButton, text = 'Delete', font = ('Open Sans', 12), height = 1, width = 16, bd = 2, padx = 13, command = DeleteData)
       self.DeleteData.grid(row=0,column=3)

       self.SearchData = Button(DFButton, text = 'Search', font = ('Open Sans', 12), height = 1, width = 16, bd = 2, padx = 13, command = searchDb)
       self.SearchData.grid(row=0,column=4)

       self.UpdateData = Button(DFButton, text = 'Update', font = ('Open Sans', 12), height = 1, width = 16, bd = 2, padx = 13, command = updateDb)
       self.UpdateData.grid(row=0,column=5)

       self.ExitData = Button(DFButton, text = 'Exit', font = ('Open Sans', 12), height = 1, width = 16, bd = 2, padx = 13, command = Exit)
       self.ExitData.grid(row=0,column=6)



if __name__ == '__main__':
   root = Tk()
   application = Student(root)
   root.mainloop()

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
import ExamDatabase
#Frontend

class Student:

   def __init__(self,root):
       self.root = root
       self.root.title("St Pats Senior Exam Prep")
       self.root.geometry("1350x1000")
       self.root.config(bg="#B5644C")


       FirstName = StringVar()
       Lastname = StringVar()
       YearLevel = StringVar()
       Sub1 = StringVar()
       Sub2 = StringVar()
       Sub3 = StringVar()
       Sub4 = StringVar()
       Sub5 = StringVar()
       Sub6 = StringVar()
       Sub7 = StringVar()
       Sub8 = StringVar()
       Conf1 = StringVar()
       Conf2 = StringVar()
       Conf3 = StringVar()
       Conf4 = StringVar()
       Conf5 = StringVar()
       Conf6 = StringVar()
       Conf7 = StringVar()
       Conf8 = StringVar()
       TotalConf = StringVar()
       AverageConf = StringVar()


       #============================================== FUNCTIONS ==================================================================================

       def Exit():
           ExitCommand = tkinter.messagebox.askyesno("Quit Student Management System", "Do you want to quit?")
           if ExitCommand > 0:
               root.destroy()
               return

       def Clear():
            FirstName.set("")
            Lastname.set("")
            YearLevel.set("")
            Sub1.set("")
            Sub2.set("")
            Sub3.set("")
            Sub4.set("")
            Sub5.set("")
            Sub6.set("")
            Sub7.set("")
            Sub8.set("")
            Conf1.set("")
            Conf2.set("")
            Conf3.set("")
            Conf4.set("")
            Conf5.set("")
            Conf6.set("")
            Conf7.set("")
            Conf8.set("")
            TotalConf.set("")
            AverageConf.set("")


       def AverageScore():

            subjectCount = 0
            ScoreSum = 0
            if Conf1.get() != '':
                unit1 = float(Conf1.get())
                ScoreSum += unit1
                subjectCount += 1
            if Conf2.get() != '':
                unit2 = float(Conf2.get())
                ScoreSum += unit2
                subjectCount +=1
            if Conf3.get() != '':
                unit3 = float(Conf3.get())
                ScoreSum += unit3
                subjectCount +=1
            if Conf4.get() != '':
                unit4 = float(Conf4.get())
                ScoreSum += unit4
                subjectCount +=1
            if Conf5.get() != '':
                unit5 = float(Conf5.get())
                ScoreSum += unit5
                subjectCount +=1
            if Conf6.get() != '':
                unit6 = float(Conf6.get())
                ScoreSum += unit6
                subjectCount +=1
            if Conf7.get() != '':
                unit7 = float(Conf7.get())
                ScoreSum += unit7
                subjectCount +=1
            if Conf8.get() != '':
                unit8 = float(Conf8.get())
                ScoreSum += unit8
                subjectCount +=1

            UnitAverage = ScoreSum/subjectCount
            UnitTotal = ScoreSum
            TotalConf.set(UnitTotal)
            AverageConf.set(UnitAverage)

       #============================================== Functions subject to the Database ====================================================================

       def addData():
           AverageScore()
           if(len(FirstName.get()) != 0):
               ExamDatabase.addStudent(FirstName.get(), Lastname.get(), YearLevel.get(), Sub1.get(), Sub2.get(), Sub3.get(), Sub4.get(), Sub5.get(), Sub6.get(),
                               Sub7.get(), Sub8.get(), Conf1.get(), Conf2.get(), Conf3.get(), Conf4.get(), Conf5.get(), Conf6.get(), Conf7.get(), Conf8.get(), TotalConf.get(), AverageConf.get())
               StudentList.delete(0, END)
               StudentList.insert(END, (FirstName.get(), Lastname.get(), YearLevel.get(), Sub1.get(), Sub2.get(), Sub3.get(), Sub4.get(), Sub5.get(), Sub6.get(),
                               Sub7.get(), Sub8.get(), Conf1.get(), Conf2.get(), Conf3.get(), Conf4.get(), Conf5.get(), Conf6.get(), Conf7.get(), Conf8.get(), TotalConf.get(), AverageConf.get()))

       def searchDb():
           StudentList.delete(0, END)
           for row in ExamDatabase.searchDatabase(FirstName.get()):
               StudentList.insert(END, row, str(""))

       def DisplayData():
           StudentList.delete(0, END)
           for row in ExamDatabase.viewData():
               StudentList.insert(END, row, str(""))

       def updateDb():
           if (len(FirstName.get())!= 0):
               ExamDatabase.deleteData(sd[0])
           if (len(FirstName.get())!= 0):
               ExamDatabase.addStudent(FirstName.get(), Lastname.get(), YearLevel.get(), Sub1.get(), Sub2.get(), Sub3.get(), Sub4.get(), Sub5.get(), Sub6.get(),
                               Sub7.get(), Sub8.get(), Conf1.get(), Conf2.get(), Conf3.get(), Conf4.get(), Conf5.get(), Conf6.get(), Conf7.get(), Conf8.get(), TotalConf.get(), AverageConf.get())
               StudentList.delete(0, END)
               StudentList.insert(END, (FirstName.get(), Lastname.get(), YearLevel.get(), Sub1.get(), Sub2.get(), Sub3.get(), Sub4.get(), Sub5.get(), Sub6.get(),
                               Sub7.get(), Sub8.get(), Conf1.get(), Conf2.get(), Conf3.get(), Conf4.get(), Conf5.get(), Conf6.get(), Conf7.get(), Conf8.get(), TotalConf.get(), AverageConf.get()))
           AverageScore()

       def DeleteData():
           if(len(FirstName.get()) != 0):
               ExamDatabase.deleteData(sd[0])
               Clear()
               DisplayData()

       def StdRecord(event):
           global sd
           studentSearch = StudentList.curselection()[0]
           sd = StudentList.get(studentSearch)

           self.TextFirstName.delete(0, END)
           self.TextFirstName.insert(END, sd[1])
           self.TextLastName.delete(0, END)
           self.TextLastName.insert(END, sd[2])
           self.cbYearLevel.delete(0, END)
           self.cbYearLevel.insert(END, sd[3])
           self.cbSub1.delete(0, END)
           self.cbSub1.insert(END, sd[4])
           self.cbSub2.delete(0, END)
           self.cbSub2.insert(END, sd[5])
           self.cbSub3.delete(0, END)
           self.cbSub3.insert(END, sd[6])
           self.cbSub4.delete(0, END)
           self.cbSub4.insert(END, sd[7])
           self.cbSub5.delete(0, END)
           self.cbSub5.insert(END, sd[8])
           self.cbSub6.delete(0, END)
           self.cbSub6.insert(END, sd[9])
           self.cbSub7.delete(0, END)
           self.cbSub7.insert(END, sd[10])
           self.cbSub8.delete(0, END)
           self.cbSub8.insert(END, sd[11])
           self.lblConf1.delete(0, END)
           self.lblConf1.insert(END, sd[12])
           self.lblConf2.delete(0, END)
           self.lblConf2.insert(END, sd[13])
           self.lblConf3.delete(0, END)
           self.lblConf3.insert(END, sd[14])
           self.lblConf4.delete(0, END)
           self.lblConf4.insert(END, sd[15])
           self.lblConf5.delete(0, END)
           self.lblConf5.insert(END, sd[16])
           self.lblConf6.delete(0, END)
           self.lblConf6.insert(END, sd[17])
           self.lblConf7.delete(0, END)
           self.lblConf7.insert(END, sd[18])
           self.lblConf8.delete(0, END)
           self.lblConf8.insert(END, sd[19])
           self.lblConf8.delete(0, END)
           self.lblConf8.insert(END, sd[20])
           self.lblConf8.delete(0, END)
           self.lblConf8.insert(END, sd[21])




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

       DFLeft = LabelFrame(DF, bd = 1, width = 450, height = 200, padx = 20, pady = 125,  relief = RIDGE, bg = "#ddd5d3",
                            font = ('Open Sans', 25), text = "Student Details")
       DFLeft.pack(side = LEFT)

       DFRight = LabelFrame(DF, bd = 1, width = 450, height = 200, padx = 20, pady = 15, relief = RIDGE, bg = "#ddd5d3",
                            font = ('Open Sans', 25), text = "Subject Selection")
       DFRight.pack(side = RIGHT)

       #============================================== WIDGET ==================================================================================#


       self.lblFirstName = Label(DFLeft, font = ('Open Sans', 15), text = "First Name", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblFirstName.grid(row = 0, column = 0, sticky = W)
       self.TextFirstName = Entry(DFLeft, font = ('Open Sans', 15), textvariable = FirstName, bg = "#f7f7f7")
       self.TextFirstName.grid(row=0, column=1)

       self.lblLastName = Label(DFLeft, font = ('Open Sans', 15), text = "Last Name", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblLastName.grid(row = 1, column = 0, sticky = W)
       self.TextLastName = Entry(DFLeft, font = ('Open Sans', 15), textvariable = Lastname, bg = "#f7f7f7")
       self.TextLastName.grid(row=1, column=1)

       self.lblYearLevel = Label(DFLeft, font = ('Open Sans', 15), text = "Year Level", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblYearLevel.grid(row = 3, column = 0, sticky = W)
       self.cbYearLevel = ttk.Combobox(DFLeft, font = ('Open Sans', 15), textvariable = YearLevel, state = 'readonly')
       self.cbYearLevel['value'] = (" ", "11", "12")
       self.cbYearLevel.grid(row=3, column = 1, padx=20)

       self.lblStd = Label(DFLeft, font = ('Open Sans', 15), text = "Total Confidence", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblStd.grid(row = 4, column = 0, sticky = W)
       self.TextStd = Entry(DFLeft, font = ('Open Sans', 15), textvariable = TotalConf, bg = "#f7f7f7")
       self.TextStd.grid(row=4, column=1)

       self.lblStd = Label(DFLeft, font = ('Open Sans', 15), text = "Average Confidence", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblStd.grid(row = 5, column = 0, sticky = W)
       self.TextStd = Entry(DFLeft, font = ('Open Sans', 15), textvariable = AverageConf, bg = "#f7f7f7")
       self.TextStd.grid(row=5, column=1)





       #============================================== Right side Subject Selction ==================================================================================#


       self.lblSub = Label(DFRight, font = ('Open Sans', 15), text = "Subject", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblSub.grid(row = 0, column = 1, sticky = W)

       self.cbSub1 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Sub1, state = 'readonly')
       self.cbSub1['value'] = ("VCAL", "English", "Accounting", "Business Management", "Criminology",  "Economics", "History", "Humanities",  "Industry & Enterprise", "International Studies",  "Legal Studies",  "Australian Business",  "Empires At Work",  "Transition", "Japanese",  "Music",  "Philosophy",  "Religion & Society", "Religious Education", "Text & Traditions",  "Design Technology",  "Food Studies",  "Food Technology", "Product Design & Technology", "Systems Engineering",
       "Building & Construction", "Computing",   "Informatics", "Software Development",  "Information & Communication Technology",  "Linguistics",  "Employment Pathways", "Biology",  "Physics",  "Chemistry",  "Psychology",  "Science & Society",
       "Forensic Science", "The Science of Human Conflict",   "Studio Art",  "Art",  "Media",  "Photography",  "Theatre Studies",  "Architectural Design",  "Visual Communication",  "Health",
       "Physical Education",  "Outdoor & Environmental Studies", "Sport",  "Health & Human Development",  "Wilderness Skills",  "Foundation Maths ",   "Further Maths",  "General Maths",
       "Mathematical Methods",  "Maths",  "Mathematics - Advanced",  "Mathematics - Pre-Methods",  "Mathematics - Standard",  "Modified Mathematics",  "Specialist Mathematics",  "Transition Mathematics")
       self.cbSub1.grid(row=1, column = 1, padx=20, pady = 10)


       self.cbSub2 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Sub2, state = 'readonly')
       self.cbSub2['value'] = ("VCAL", "English", "Accounting", "Business Management", "Criminology",  "Economics", "History", "Humanities",  "Industry & Enterprise", "International Studies",  "Legal Studies",  "Australian Business",  "Empires At Work",  "Transition", "Japanese",  "Music",  "Philosophy",  "Religion & Society", "Religious Education", "Text & Traditions",  "Design Technology",  "Food Studies",  "Food Technology", "Product Design & Technology", "Systems Engineering",
       "Building & Construction", "Computing",   "Informatics", "Software Development",  "Information & Communication Technology",  "Linguistics",  "Employment Pathways", "Biology",  "Physics",  "Chemistry",  "Psychology",  "Science & Society",
       "Forensic Science", "The Science of Human Conflict",   "Studio Art",  "Art",  "Media",  "Photography",  "Theatre Studies",  "Architectural Design",  "Visual Communication",  "Health",
       "Physical Education",  "Outdoor & Environmental Studies", "Sport",  "Health & Human Development",  "Wilderness Skills",  "Foundation Maths ",   "Further Maths",  "General Maths",
       "Mathematical Methods",  "Maths",  "Mathematics - Advanced",  "Mathematics - Pre-Methods",  "Mathematics - Standard",  "Modified Mathematics",  "Specialist Mathematics",  "Transition Mathematics")
       self.cbSub2.grid(row=2, column = 1, padx=20, pady = 10)

       self.cbSub3 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Sub3, state = 'readonly')
       self.cbSub3['value'] = ("VCAL", "English", "Accounting", "Business Management", "Criminology",  "Economics", "History", "Humanities",  "Industry & Enterprise", "International Studies",  "Legal Studies",  "Australian Business",  "Empires At Work",  "Transition", "Japanese",  "Music",  "Philosophy",  "Religion & Society", "Religious Education", "Text & Traditions",  "Design Technology",  "Food Studies",  "Food Technology", "Product Design & Technology", "Systems Engineering",
       "Building & Construction", "Computing",   "Informatics", "Software Development",  "Information & Communication Technology",  "Linguistics",  "Employment Pathways", "Biology",  "Physics",  "Chemistry",  "Psychology",  "Science & Society",
       "Forensic Science", "The Science of Human Conflict",   "Studio Art",  "Art",  "Media",  "Photography",  "Theatre Studies",  "Architectural Design",  "Visual Communication",  "Health",
       "Physical Education",  "Outdoor & Environmental Studies", "Sport",  "Health & Human Development",  "Wilderness Skills",  "Foundation Maths ",   "Further Maths",  "General Maths",
       "Mathematical Methods",  "Maths",  "Mathematics - Advanced",  "Mathematics - Pre-Methods",  "Mathematics - Standard",  "Modified Mathematics",  "Specialist Mathematics",  "Transition Mathematics")
       self.cbSub3.grid(row=3, column = 1, padx=20, pady = 10)


       self.cbSub4 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Sub4, state = 'readonly')
       self.cbSub4['value'] = ("VCAL", "English", "Accounting", "Business Management", "Criminology",  "Economics", "History", "Humanities",  "Industry & Enterprise", "International Studies",  "Legal Studies",  "Australian Business",  "Empires At Work",  "Transition", "Japanese",  "Music",  "Philosophy",  "Religion & Society", "Religious Education", "Text & Traditions",  "Design Technology",  "Food Studies",  "Food Technology", "Product Design & Technology", "Systems Engineering",
       "Building & Construction", "Computing",   "Informatics", "Software Development",  "Information & Communication Technology",  "Linguistics",  "Employment Pathways", "Biology",  "Physics",  "Chemistry",  "Psychology",  "Science & Society",
       "Forensic Science", "The Science of Human Conflict",   "Studio Art",  "Art",  "Media",  "Photography",  "Theatre Studies",  "Architectural Design",  "Visual Communication",  "Health",
       "Physical Education",  "Outdoor & Environmental Studies", "Sport",  "Health & Human Development",  "Wilderness Skills",  "Foundation Maths ",   "Further Maths",  "General Maths",
       "Mathematical Methods",  "Maths",  "Mathematics - Advanced",  "Mathematics - Pre-Methods",  "Mathematics - Standard",  "Modified Mathematics",  "Specialist Mathematics",  "Transition Mathematics")
       self.cbSub4.grid(row=4, column = 1, padx=20, pady = 10)

       self.cbSub5 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Sub5, state = 'readonly')
       self.cbSub5['value'] = ("VCAL", "English", "Accounting", "Business Management", "Criminology",  "Economics", "History", "Humanities",  "Industry & Enterprise", "International Studies",  "Legal Studies",  "Australian Business",  "Empires At Work",  "Transition", "Japanese",  "Music",  "Philosophy",  "Religion & Society", "Religious Education", "Text & Traditions",  "Design Technology",  "Food Studies",  "Food Technology", "Product Design & Technology", "Systems Engineering",
       "Building & Construction", "Computing",   "Informatics", "Software Development",  "Information & Communication Technology",  "Linguistics",  "Employment Pathways", "Biology",  "Physics",  "Chemistry",  "Psychology",  "Science & Society",
       "Forensic Science", "The Science of Human Conflict",   "Studio Art",  "Art",  "Media",  "Photography",  "Theatre Studies",  "Architectural Design",  "Visual Communication",  "Health",
       "Physical Education",  "Outdoor & Environmental Studies", "Sport",  "Health & Human Development",  "Wilderness Skills",  "Foundation Maths ",   "Further Maths",  "General Maths",
       "Mathematical Methods",  "Maths",  "Mathematics - Advanced",  "Mathematics - Pre-Methods",  "Mathematics - Standard",  "Modified Mathematics",  "Specialist Mathematics",  "Transition Mathematics")
       self.cbSub5.grid(row=5, column = 1, padx=20, pady = 10)


       self.cbSub6 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Sub6, state = 'readonly')
       self.cbSub6['value'] = ("VCAL", "English", "Accounting", "Business Management", "Criminology",  "Economics", "History", "Humanities",  "Industry & Enterprise", "International Studies",  "Legal Studies",  "Australian Business",  "Empires At Work",  "Transition", "Japanese",  "Music",  "Philosophy",  "Religion & Society", "Religious Education", "Text & Traditions",  "Design Technology",  "Food Studies",  "Food Technology", "Product Design & Technology", "Systems Engineering",
       "Building & Construction", "Computing",   "Informatics", "Software Development",  "Information & Communication Technology",  "Linguistics",  "Employment Pathways", "Biology",  "Physics",  "Chemistry",  "Psychology",  "Science & Society",
       "Forensic Science", "The Science of Human Conflict",   "Studio Art",  "Art",  "Media",  "Photography",  "Theatre Studies",  "Architectural Design",  "Visual Communication",  "Health",
       "Physical Education",  "Outdoor & Environmental Studies", "Sport",  "Health & Human Development",  "Wilderness Skills",  "Foundation Maths ",   "Further Maths",  "General Maths",
       "Mathematical Methods",  "Maths",  "Mathematics - Advanced",  "Mathematics - Pre-Methods",  "Mathematics - Standard",  "Modified Mathematics",  "Specialist Mathematics",  "Transition Mathematics")
       self.cbSub6.grid(row=6, column = 1, padx=20, pady = 10)

       self.cbSub7 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Sub7, state = 'readonly')
       self.cbSub7['value'] = ("VCAL", "English", "Accounting", "Business Management", "Criminology",  "Economics", "History", "Humanities",  "Industry & Enterprise", "International Studies",  "Legal Studies",  "Australian Business",  "Empires At Work",  "Transition", "Japanese",  "Music",  "Philosophy",  "Religion & Society", "Religious Education", "Text & Traditions",  "Design Technology",  "Food Studies",  "Food Technology", "Product Design & Technology", "Systems Engineering",
       "Building & Construction", "Computing",   "Informatics", "Software Development",  "Information & Communication Technology",  "Linguistics",  "Employment Pathways", "Biology",  "Physics",  "Chemistry",  "Psychology",  "Science & Society",
       "Forensic Science", "The Science of Human Conflict",   "Studio Art",  "Art",  "Media",  "Photography",  "Theatre Studies",  "Architectural Design",  "Visual Communication",  "Health",
       "Physical Education",  "Outdoor & Environmental Studies", "Sport",  "Health & Human Development",  "Wilderness Skills",  "Foundation Maths ",   "Further Maths",  "General Maths",
       "Mathematical Methods",  "Maths",  "Mathematics - Advanced",  "Mathematics - Pre-Methods",  "Mathematics - Standard",  "Modified Mathematics",  "Specialist Mathematics",  "Transition Mathematics")
       self.cbSub7.grid(row=7, column = 1, padx=20, pady = 10)

       self.cbSub8 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Sub8, state = 'readonly')
       self.cbSub8['value'] = ("VCAL", "English", "Accounting", "Business Management", "Criminology",  "Economics", "History", "Humanities",  "Industry & Enterprise", "International Studies",  "Legal Studies",  "Australian Business",  "Empires At Work",  "Transition", "Japanese",  "Music",  "Philosophy",  "Religion & Society", "Religious Education", "Text & Traditions",  "Design Technology",  "Food Studies",  "Food Technology", "Product Design & Technology", "Systems Engineering",
       "Building & Construction", "Computing",   "Informatics", "Software Development",  "Information & Communication Technology",  "Linguistics",  "Employment Pathways", "Biology",  "Physics",  "Chemistry",  "Psychology",  "Science & Society",
       "Forensic Science", "The Science of Human Conflict",   "Studio Art",  "Art",  "Media",  "Photography",  "Theatre Studies",  "Architectural Design",  "Visual Communication",  "Health",
       "Physical Education",  "Outdoor & Environmental Studies", "Sport",  "Health & Human Development",  "Wilderness Skills",  "Foundation Maths ",   "Further Maths",  "General Maths",
       "Mathematical Methods",  "Maths",  "Mathematics - Advanced",  "Mathematics - Pre-Methods",  "Mathematics - Standard",  "Modified Mathematics",  "Specialist Mathematics",  "Transition Mathematics")
       self.cbSub8.grid(row=8, column = 1, padx=20, pady = 10)


       #============================================== Confidence Level ==================================================================================#


       self.lblConf = Label(DFRight, font = ('Open Sans', 15), text = "Confidence (0-10)", padx = 10, pady = 10, bg = "#ddd5d3")
       self.lblConf.grid(row = 0, column = 2, sticky = W)
       self.lblConf1 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Conf1, state = 'readonly')
       self.lblConf1['value'] = (" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
       self.lblConf1.grid(row=1, column = 2, padx=20, pady = 10)


       self.lblConf2 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Conf2, state = 'readonly')
       self.lblConf2['value'] = (" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
       self.lblConf2.grid(row=2, column = 2, padx=20, pady = 10)

       self.lblConf3 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Conf3, state = 'readonly')
       self.lblConf3['value'] = (" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
       self.lblConf3.grid(row=3, column = 2, padx=20, pady = 10)


       self.lblConf4 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Conf4, state = 'readonly')
       self.lblConf4['value'] = (" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
       self.lblConf4.grid(row=4, column = 2, padx=20, pady = 10)

       self.lblConf5 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Conf5, state = 'readonly')
       self.lblConf5['value'] = (" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
       self.lblConf5.grid(row=5, column = 2, padx=20, pady = 10)


       self.lblConf6 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Conf6, state = 'readonly')
       self.lblConf6['value'] = (" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
       self.lblConf6.grid(row=6, column = 2, padx=20, pady = 10)

       self.lblConf7 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Conf7, state = 'readonly')
       self.lblConf7['value'] = (" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
       self.lblConf7.grid(row=7, column = 2, padx=20, pady = 10)


       self.lblConf8 = ttk.Combobox(DFRight, font = ('Open Sans', 15), textvariable = Conf8, state = 'readonly')
       self.lblConf8['value'] = (" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
       self.lblConf8.grid(row=8, column = 2, padx=20, pady = 10)



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

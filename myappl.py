from tkinter import *
from tkinter import messagebox
from xml.etree.ElementTree import tostring
import mysql.connector
import tkinter.font as tkFont
import ast


import tkinter as tk					
from tkinter import ttk
from tkinter.ttk import Treeview
from turtle import bgcolor
# from pyparsing import identbodychars

########## ---- MACHINE LEARNING MODEL
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


root = Tk()
root.title('MEDEX DIAGNOSIS SYSTEM')
root.iconbitmap('hospital.ico')
root.geometry('1166x718')
root.state('zoomed')
root.resizable(0, 0)
root.configure(bg='#fff')
# root.option_add('Microsoft YaHei UI Light', '19')
# root.resizable(False,False)


def signin():
    username = user.get()
    password = code.get()

    file = open('datasheet.txt','r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()


    # print(r.keys())
    # print(r.values())


    if username in r.keys() and password == r[username]:
        window = Toplevel(root)
        window.title("MEDEX")
        window.geometry("1166x718")
        window.state('zoomed')
        window.iconbitmap('hospital.ico')
        # window.configure(bg='#fff')
        # window.resizable(False,False)

        #DIAGNOSIS SCREEN
        def diagnosis():
            screen = Toplevel(window)
            screen.title('MEDEX SYSTEM')
            screen.geometry('1166x718')
            screen.state('zoomed')
            screen.iconbitmap('hospital.ico')
            screen.configure(bg='#fff')
            # screen.option_add('*Font','Microsoft')
            # default_font = tkFont.nametofont("TkDefaultFont")
            # default_font.configure(size=48)


            df = pd.read_csv("malariadataset.csv")

            X = df[['headache','runny_nose','sneezing','sore_throat','fever','chills','body_ache','abdominal_pain','poor_appetite','rash','conjunctivitis','sweating','nausea','vomiting','diarrhea']]
            Y = df['prognosis']


            # with sklearn
            # regr = linear_model.LinearRegression()
            # regr.fit(X, Y)


            # TEST
            X = df.drop(columns='prognosis', axis=1)
            Y = df['prognosis']

            # Split train test
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

            model = LogisticRegression()

            #training the logistic regression model using train data
            model.fit(X_train, Y_train)



            # DB FUNCTIONS
            # REGISTER PATIENT
            def regpatient():
                flag_validation = True
                global firstname
                firstname = t1.get()
                global middlename
                middlename = t2.get()
                global surname
                surname = t3.get()
                global gender
                gender = t4.get()
                global age
                age = t5.get()
                global occupation
                occupation = t6.get()
                global maritalstatus
                maritalstatus = t7.get()
                global telephone
                telephone = t8.get()
                global address
                address = t9.get()
                global nationalid
                nationalid = t10.get()

                if firstname == '' or middlename == '' or surname == '' or gender == '' or age == '' or occupation == '' or maritalstatus == '' or telephone == '' or address == '' or nationalid == '':
                    flag_validation = False

                if(flag_validation):  
                    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="medexdiagnosis", auth_plugin="mysql_native_password")
                    mycursor = mydb.cursor()

                    query = "INSERT INTO patientrecords (firstname, middlename, surname, gender, age, occupation, maritalstatus, telephone, address, nationalid) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    mycursor.execute(query, (firstname, middlename, surname, gender, age, occupation, maritalstatus, telephone, address, nationalid))
                    mydb.commit()
                    tabControl.select(1)

                else:
                    err.config(fg='red')   # foreground color
                    err.config(bg='yellow') # background color
                    my_str.set("Check Inputs.")    
                # clear()

            ####################--------- dbconnection
            # mydb = mysql.connector.connect(host="localhost", user="root", password="", database="medexdiagnosis", auth_plugin="mysql_native_password")
            # mycursor = mydb.cursor()

            tabControl = ttk.Notebook(screen)
            # tabControl.configure(bg='#fffff')

            # def hide():
                # tabControl.hide(1)

            tab1 = ttk.Frame(tabControl)
            tab2 = ttk.Frame(tabControl)
            tab3 = ttk.Frame(tabControl)
            tab4 = ttk.Frame(tabControl)

            # tab1.configure(bgcolor='#fff')

            tabControl.add(tab1, text ='PATIENT DATA')
            tabControl.add(tab2, text ='DIAGNOSIS')
            tabControl.add(tab3, text ='PRESCRIPTION')
            tabControl.add(tab4, text ='PRESCRIPTION')
            tabControl.pack(expand = 1, fill ="both")

            # patient form variables
            t1 = StringVar()
            t2 = StringVar()
            t3 = StringVar()
            t4 = StringVar()
            t4.set("Male")
            t5 = StringVar()
            t6 = StringVar()
            t7 = StringVar()
            t8 = StringVar()
            t9 = StringVar()
            t10 = StringVar()
            t11 = StringVar()
            t12 = StringVar()
            t13 = StringVar()
            t14 = StringVar()
            t15 = StringVar()
            t16 = StringVar()
            my_str = StringVar()



            # Instructions Label
            label = Label(tab1, text='Instructions\nPlease Enter the patient"s data',font=('Microsoft YaHei UI Light',11))
            label.grid(row=0, column=0, padx=5, pady=3)

            # First Input input and label
            label1 = Label(tab1, text='First Name',font=('Microsoft YaHei UI Light',9,'bold'))
            label1.grid(row=1, column=0, padx=5, pady=3)
            entry1 = Entry(tab1, textvariable=t1,font=('Microsoft YaHei UI Light',9))
            entry1.grid(row=1, column=1, padx=5, pady=3)

            #Second Input
            label2 = Label(tab1, text='Middle Name',font=('Microsoft YaHei UI Light',9,'bold'))
            label2.grid(row=2, column=0, padx=5, pady=3)
            entry2 = Entry(tab1, textvariable=t2,font=('Microsoft YaHei UI Light',9))
            entry2.grid(row=2, column=1, padx=5, pady=3)

            #Third input
            label3 = Label(tab1, text='Last Name',font=('Microsoft YaHei UI Light',9,'bold'))
            label3.grid(row=3, column=0, padx=5, pady=3)
            entry3 = Entry(tab1, textvariable=t3,font=('Microsoft YaHei UI Light',9))
            entry3.grid(row=3, column=1, padx=5, pady=3)

            label4 = Label(tab1, text='Gender *',font=('Microsoft YaHei UI Light',9,'bold'))
            label4.grid(row=4, column=0, padx=5, pady=3)
            entry4 = ttk.Combobox(tab1, text='Male', width=20, textvariable = t4, value='Male')
            entry4['values'] = (' Male',
                                ' Female',
                                ' Rather Not Say')
            entry4.current()
            # entry3.place(x=90,y=202)
            entry4.grid(row=4, column=1)

            ####---------  --- ------error input
            err = tk.Label(tab1,  textvariable=my_str, width=10 )  
            err.grid(row=14,column=1) 
            my_str.set("")

            #Fourth Input
            label5 = Label(tab1, text='Age',font=('Microsoft YaHei UI Light',9,'bold'))
            label5.grid(row=5, column=0, padx=5, pady=3)
            entry5 = Entry(tab1, textvariable=t5,font=('Microsoft YaHei UI Light',9))
            entry5.grid(row=5, column=1, padx=5, pady=3)

            label6 = Label(tab1, text='Y - M - D',font=('Microsoft YaHei UI Light',9,'bold'))
            label6.grid(row=5, column=3, padx=5, pady=3)

            #Fifth Input
            label6 = Label(tab1, text='Occupation',font=('Microsoft YaHei UI Light',9,'bold'))
            label6.grid(row=6, column=0, padx=5, pady=3)
            entry6 = Entry(tab1, textvariable=t6,font=('Microsoft YaHei UI Light',9))
            entry6.grid(row=6, column=1, padx=5, pady=3)

            #Sixth Input
            label7 = Label(tab1, text='Marital Status',font=('Microsoft YaHei UI Light',9,'bold'))
            label7.grid(row=7, column=0, padx=5, pady=3)
            entry7 = Entry(tab1, textvariable=t7,font=('Microsoft YaHei UI Light',9))
            entry7.grid(row=7, column=1, padx=5, pady=3)

            #Seventh Input
            label8 = Label(tab1, text='Telephone',font=('Microsoft YaHei UI Light',9,'bold'))
            label8.grid(row=8, column=0, padx=5, pady=3)
            entry8 = Entry(tab1, textvariable=t8,font=('Microsoft YaHei UI Light',9))
            entry8.grid(row=8, column=1, padx=5, pady=3)

            #Eighth Input
            label9 = Label(tab1, text='Address',font=('Microsoft YaHei UI Light',9,'bold'))
            label9.grid(row=9, column=0, padx=5, pady=3)
            entry9 = Entry(tab1, textvariable=t9,font=('Microsoft YaHei UI Light',9))
            entry9.grid(row=9, column=1, padx=5, pady=3)

            #Ninth Input
            label10 = Label(tab1, text='National ID',font=('Microsoft YaHei UI Light',9,'bold'))
            label10.grid(row=10, column=0, padx=5, pady=3)
            entry10 = Entry(tab1, textvariable=t10,font=('Microsoft YaHei UI Light',9))
            entry10.grid(row=10, column=1, padx=5, pady=3)

            registerbtn = Button(tab1,width=15,pady=7,text='ADD PATIENT',bg='#57a1f8',fg='white',border=0,command=regpatient)
            registerbtn.grid(row=11, column=1, padx=5, pady=3)


            #@@@@@@@@@@@@@@@@@@@@@@------------------ END OF PATIENT INFO FORM

            tabControl.add(tab2, text ='DIAGNOSIS')

            # q = StringVar()
            t1s = StringVar()
            t2s = StringVar()
            t3s = StringVar()
            t4s = StringVar()
            t5s = StringVar()
            t6s = StringVar()
            t7s = StringVar()
            t8s = StringVar()
            t9s = StringVar()
            t10s = StringVar()
            t11s = StringVar()
            t12s = StringVar()
            t13s = StringVar()
            t14s = StringVar()
            t15s = StringVar()
            t1ss = StringVar()

            # Instructions Label
            labels = Label(tab2, text='Instructions\nPlease Enter 1 (Yes) or 0 (No)',font=('Microsoft YaHei UI Light',11))
            labels.grid(row=0, column=0, padx=5, pady=3)

            # Instructions Label
            labelss = Label(tab2, text='Doctor\'s Input\nPlease Specify the Severity',font=('Microsoft YaHei UI Light',11))
            labelss.grid(row=0, column=4, padx=5, pady=3)


            # First symptom input and label
            label1s = Label(tab2, text='Headache',font=('Microsoft YaHei UI Light',9,'bold'))
            label1s.grid(row=1, column=0, padx=5, pady=3)
            entry1s = Entry(tab2, textvariable=t1s,font=('Microsoft YaHei UI Light',11))
            entry1s.grid(row=1, column=1, padx=5, pady=3)

            #Second Symptom
            label2s = Label(tab2, text='Runny Nose',font=('Microsoft YaHei UI Light',11))
            label2s.grid(row=2, column=0, padx=5, pady=3)
            entry2s = Entry(tab2, textvariable=t2s,font=('Microsoft YaHei UI Light',11))
            entry2s.grid(row=2, column=1, padx=5, pady=3)

            #Third Symptom
            label3s = Label(tab2, text='Sneezing',font=('Microsoft YaHei UI Light',11))
            label3s.grid(row=3, column=0, padx=5, pady=3)
            entry3s = Entry(tab2, textvariable=t3s,font=('Microsoft YaHei UI Light',11))
            entry3s.grid(row=3, column=1, padx=5, pady=3)

            #Fourth Symptom
            label4s = Label(tab2, text='Sore Throat',font=('Microsoft YaHei UI Light',11))
            label4s.grid(row=4, column=0, padx=5, pady=3)
            entry4s = Entry(tab2, textvariable=t4s,font=('Microsoft YaHei UI Light',11))
            entry4s.grid(row=4, column=1, padx=5, pady=3)

            #Fifth Symptom
            label5s = Label(tab2, text='Fever',font=('Microsoft YaHei UI Light',11))
            label5s.grid(row=5, column=0, padx=5, pady=3)
            entry5s = Entry(tab2, textvariable=t5s,font=('Microsoft YaHei UI Light',11))
            entry5s.grid(row=5, column=1, padx=5, pady=3)

            #Sixth Symptom
            label6s = Label(tab2, text='Chills',font=('Microsoft YaHei UI Light',11))
            label6s.grid(row=6, column=0, padx=5, pady=3)
            entry6s = Entry(tab2, textvariable=t6s,font=('Microsoft YaHei UI Light',11))
            entry6s.grid(row=6, column=1, padx=5, pady=3)

            #Seventh Symptom
            label7s = Label(tab2, text='Body Ache',font=('Microsoft YaHei UI Light',11))
            label7s.grid(row=7, column=0, padx=5, pady=3)
            entry7s = Entry(tab2, textvariable=t7s,font=('Microsoft YaHei UI Light',11))
            entry7s.grid(row=7, column=1, padx=5, pady=3)

            #Eighth Symptom
            label8s = Label(tab2, text='Abdominal Pain',font=('Microsoft YaHei UI Light',11))
            label8s.grid(row=8, column=0, padx=5, pady=3)
            entry8s = Entry(tab2, textvariable=t8s,font=('Microsoft YaHei UI Light',11))
            entry8s.grid(row=8, column=1, padx=5, pady=3)

            #Ninth Symptom
            label9s = Label(tab2, text='Poor Appetite',font=('Microsoft YaHei UI Light',11))
            label9s.grid(row=9, column=0, padx=5, pady=3)
            entry9s = Entry(tab2, textvariable=t9s,font=('Microsoft YaHei UI Light',11))
            entry9s.grid(row=9, column=1, padx=5, pady=3)

            #Tenth Symptom
            label10s = Label(tab2, text='Rash',font=('Microsoft YaHei UI Light',11))
            label10s.grid(row=10, column=0, padx=5, pady=3)
            entry10s = Entry(tab2, textvariable=t10s,font=('Microsoft YaHei UI Light',11))
            entry10s.grid(row=10, column=1, padx=5, pady=3)

            #Eleventh Symptom
            label11s = Label(tab2, text='Conjunctivitis',font=('Microsoft YaHei UI Light',11))
            label11s.grid(row=11, column=0, padx=5, pady=3)
            entry11s = Entry(tab2, textvariable=t11s,font=('Microsoft YaHei UI Light',11))
            entry11s.grid(row=11, column=1, padx=5, pady=3)

            #Twelveth Symptom
            label12s = Label(tab2, text='Sweating',font=('Microsoft YaHei UI Light',11))
            label12s.grid(row=12, column=0, padx=5, pady=3)
            entry12s = Entry(tab2, textvariable=t12s,font=('Microsoft YaHei UI Light',11))
            entry12s.grid(row=12, column=1, padx=5, pady=3)

            #Thirteenth Symptom
            label13s = Label(tab2, text='Nausea',font=('Microsoft YaHei UI Light',11))
            label13s.grid(row=13, column=0, padx=5, pady=3)
            entry13s = Entry(tab2, textvariable=t13s,font=('Microsoft YaHei UI Light',11))
            entry13s.grid(row=13, column=1, padx=5, pady=3)

            #Fourteenth Symptom
            label14s = Label(tab2, text='Vomiting',font=('Microsoft YaHei UI Light',11))
            label14s.grid(row=14, column=0, padx=5, pady=3)
            entry14s = Entry(tab2, textvariable=t14s,font=('Microsoft YaHei UI Light',11))
            entry14s.grid(row=14, column=1, padx=5, pady=3)

            #Fifth Symptom
            label15s = Label(tab2, text='Diarrhea',font=('Microsoft YaHei UI Light',11))
            label15s.grid(row=15, column=0, padx=5, pady=3)
            entry15s = Entry(tab2, textvariable=t15s,font=('Microsoft YaHei UI Light',11))
            entry15s.grid(row=15, column=1, padx=5, pady=3)




            # Doctor specify severity and label
            label1ss = Label(tab2, text='Severity',font=('Microsoft YaHei UI Light',9,'bold'))
            label1ss.grid(row=1, column=4, padx=5, pady=3)
            entry1ss = ttk.Combobox(tab2, text='Minor', width=20, textvariable = t1ss, value='Minor')
            entry1ss['values'] = (' Minor',
                                ' Moderate',
                                ' Major',
                                ' Critical')
            entry1ss.current()
            # entry3.place(x=90,y=202)
            entry1ss.grid(row=2, column=4)

            def values():
                global Headache #First Symptom Input
                Headache = int(entry1s.get())

                global Runny_Nose #Second Symptom Input
                Runny_Nose = int(entry2s.get())

                global Sneezing #Third Symptom Input
                Sneezing = int(entry3s.get())

                global Sore_Throat #Fourth Symptom Input
                Sore_Throat = int(entry4s.get())

                global Fever #Fifth Symptom Input
                Fever = int(entry5s.get())

                global Chills #Sixth Symptom Input
                Chills = int(entry6s.get())

                global Body_Ache #Seventh Symptom Input
                Body_Ache = int(entry7s.get())

                global Abdominal_Pain #Eighth Symptom Input
                Abdominal_Pain = int(entry8s.get())

                global Poor_Appetite #Ninth Symptom Input
                Poor_Appetite = int(entry9s.get())

                global Rash #Tenth Symptom Input
                Rash = int(entry10s.get())

                global Conjunctivitis #Eleventh Symptom Input
                Conjunctivitis = int(entry11s.get())

                global Sweating #Twelveth Symptom Input
                Sweating = int(entry12s.get())

                global Nausea #Thirteenth Symptom Input
                Nausea = int(entry13s.get())

                global Vomiting #Fourteenth Symptom Input
                Vomiting = int(entry14s.get())

                global Diarrhea #Second Symptom Input
                Diarrhea = int(entry15s.get())

                global Severity #Second Symptom Input
                Severity = entry1ss.get()

                prediction = model.predict([[Headache,Runny_Nose,Sneezing,Sore_Throat,Fever,Chills,Body_Ache,Abdominal_Pain,Poor_Appetite,Rash,Conjunctivitis,Sweating,Nausea,Vomiting,Diarrhea]])

                Prediction_result = ('Predicted Disease: ', model.predict([[Headache,Runny_Nose,Sneezing,Sore_Throat,Fever,Chills,Body_Ache,Abdominal_Pain,Poor_Appetite,Rash,Conjunctivitis,Sweating,Nausea,Vomiting,Diarrhea]]))
                label_Prediction = Label(tab3, text=prediction, bg='#57a1f8',font=('Microsoft YaHei UI Light',11))
                label_Prediction.grid(row=8, column=1, padx=5, pady=3)

                prediction = model.predict([[Headache,Runny_Nose,Sneezing,Sore_Throat,Fever,Chills,Body_Ache,Abdominal_Pain,Poor_Appetite,Rash,Conjunctivitis,Sweating,Nausea,Vomiting,Diarrhea]])

                arr = np.array(prediction)

                global firstname #Second Symptom Input
                firstname = t1.get()

                global middlename #Second Symptom Input
                middlename = t2.get()

                global surname
                surname = t3.get()

                global age
                age = t4.get()

                # global diagnosis
                # diagnosis = tostring(arr)
                #Convert to string 
                diagnosis = np.array_str(arr)

                # class NumpyMySQLConverter(mysql.connector.conversion.MySQLConverter):
                #     def _int64_to_mysql(self, value):
                #         return int(value)



                mydb = mysql.connector.connect(host="localhost", user="root", password="", database="medexdiagnosis", auth_plugin="mysql_native_password")
                # mydb.set_converter_class(NumpyMySQLConverter)

                mycursor = mydb.cursor()

                slct = "SELECT patientid FROM patientrecords WHERE firstname = %s and middlename = %s and surname = %s"
                mycursor.execute(slct, (firstname, middlename, surname))
                id = mycursor.fetchone()

                print(id)
                mydb.commit()

                # s=''.join(id)

                s = ' '.join(map(str, id))

                print(s)

                sql = "INSERT INTO diagnosisrecords(patientid, firstname, middlename, surname, age, disease, severity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                # val = (firstname, middlename, surname, diagnosis, Severity)
                mycursor.execute(sql, (s, firstname, middlename, surname, age, diagnosis, Severity))
                mydb.commit()  
                # regpatient()  

                # mydb = mysql.connector.connect(host="localhost", user="root", password="", database="medexdiagnosis", auth_plugin="mysql_native_password")
                # mycursor = mydb.cursor()

                # Prescriptions and Advice
                if (prediction == 'Malaria'):
                    Result = ('Please consider prescibing the following for the patient:\n1: Aralen/tab\n2: Qualaquin/tab\n3: Plaquenil/tab\n4: Mefloquine\n\n You can instruct the patient to do the following:\nPlease do not sleep in open air and cover your full skin\n')
                    Result0 = Label(tab3, text=Result, bg='#57a1f8',fg='black')
                    Result0.grid(row=11, column=1, padx=5, pady=3)
                elif (prediction == 'Typhoid'):
                    Result = ('Please consider prescibing the following for the patient:\n1: Chloramphenicol/tab\n2: Amoxicillin/tab\n3: Ciprofloxacin/tab\n4: Azithromycin/tab\n\nYou can instruct the patient to do the following:\nPlease do complete bed rest and take soft Diet\n')
                    Result0 = Label(tab3, text=Result, bg='orange')
                    Result0.grid(row=1, column=1, padx=5, pady=3)
                elif (prediction == 'Cold'):
                    Result = ('Please consider prescibing the following for the patient:\n1: Tylenol/tab\n2: Panadol/tab\n3: Nasal Spray\n\nYou can instruct the patient to do the following:\nPlease wear warm clothes\n')
                    Result0 = Label(tab3, text=Result, bg='orange')
                    Result0.grid(row=1, column=1, padx=5, pady=3)
                elif (prediction == 'Flu'):
                    Result = ('Please consider prescibing the following for the patient:\n1: Tamiflu/tab\n2: Panadol/tab\n3: Zanamivir/tab\n\nYou can instruct the patient to do the following:\nPlease take a warm bath and do salt gargling\n')
                    Result0 = Label(tab3, text=Result, bg='orange')
                    Result0.grid(row=1, column=1, padx=5, pady=3)
                elif (prediction == 'Measles'):
                    Result = ('Please consider prescibing the following for the patient:\n1: Tylenol/tab\n2: Aleve/tab\n3: Advil/tab\n4: Vitamin A\n\nYou can instruct the patient to do the following:\nPlease Get rest and use more liquid\n')
                    Result0 = Label(tab3, text=Result, bg='orange')
                    Result0.grid(row=1, column=1, padx=5, pady=3)
                elif (prediction == 'Invalid Input'):
                    Result = ('Please consider specify valid input and try againd\n')
                    Result0 = Label(tab3, text=Result, bg='orange')
                    Result0.grid(row=1, column=1, padx=5, pady=3)
                tabControl.select(2)       

            my_button = Button(tab2, width=39,text="Diagnose Disease",bg='#57a1f8',fg='white',border=0, command=values)
            my_button.grid(row=17, column=1, padx=2, pady=3)
            
            screen.mainloop()
        def statistics():
            ws  = Toplevel(window)
            ws.title('DIAGNOSIS REPORTS')
            ws.geometry('1166x718')
            ws.state('zoomed')
            ws.iconbitmap('hospital.ico')
            ws.configure(bg='#fff')

            set = ttk.Treeview(ws)
            set.pack()


            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="medexdiagnosis", auth_plugin="mysql_native_password")
            # mydb.set_converter_class(NumpyMySQLConverter)

            mycursor = mydb.cursor()

            # MALARIA COUNT
            malaria = 'Malaria'

            slct = "SELECT COUNT(disease) FROM diagnosisrecords WHERE disease LIKE '%"+malaria+"%'"
            mycursor.execute(slct)
            malariast = mycursor.fetchone()

            mydb.commit()


            # TYPHOID COUNT
            typhoid = 'Typhoid'
            slct = "SELECT COUNT(disease) FROM diagnosisrecords WHERE disease LIKE '%"+typhoid+"%'"
            mycursor.execute(slct)
            typhoidst = mycursor.fetchone()

            mydb.commit()


            # COLD COUNT
            cold = 'Cold'
            slct = "SELECT COUNT(disease) FROM diagnosisrecords WHERE disease LIKE '%"+cold+"%'"
            mycursor.execute(slct)
            coldst = mycursor.fetchone()

            mydb.commit()


            # FLU COUNT
            flu = 'Flu'
            slct = "SELECT COUNT(disease) FROM diagnosisrecords WHERE disease LIKE '%"+flu+"%'"
            mycursor.execute(slct)
            flust = mycursor.fetchone()

            mydb.commit()


            # MEASLES COUNT
            measles = 'Measles'
            slct = "SELECT COUNT(disease) FROM diagnosisrecords WHERE disease LIKE '%"+flu+"%'"
            mycursor.execute(slct)
            measlesst = mycursor.fetchone()

            mydb.commit()


            # AGE COUNTS
            # MALARIA COUNT UNDER 10
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 10 and disease LIKE '%"+malaria+"%'"
            mycursor.execute(slct)
            malariab10 = mycursor.fetchone()

            mydb.commit()


            # MALARIA COUNT 11-18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 18 and disease LIKE '%"+malaria+"%'"
            mycursor.execute(slct)
            malaria18 = mycursor.fetchone()

            mydb.commit()

            # MALARIA COUNT OVER 18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age > 18 and disease LIKE '%"+malaria+"%'"
            mycursor.execute(slct)
            malaria1835 = mycursor.fetchone()

            mydb.commit()



            # TYPHOID COUNT UNDER 10
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 10 and disease LIKE '%"+typhoid+"%'"
            mycursor.execute(slct)
            typhb10 = mycursor.fetchone()

            mydb.commit()


            # TYPHOID COUNT 11-18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 18 and disease LIKE '%"+typhoid+"%'"
            mycursor.execute(slct)
            typh18 = mycursor.fetchone()

            mydb.commit()

            # TYPHOID COUNT OVER 18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age > 18 and disease LIKE '%"+typhoid+"%'"
            mycursor.execute(slct)
            typh1835 = mycursor.fetchone()

            mydb.commit()



            # COLD COUNT UNDER 10
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 10 and disease LIKE '%"+cold+"%'"
            mycursor.execute(slct)
            coldb10 = mycursor.fetchone()

            mydb.commit()


            # COLD COUNT 11-18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 18 and disease LIKE '%"+cold+"%'"
            mycursor.execute(slct)
            cold18 = mycursor.fetchone()

            mydb.commit()

            # COLD COUNT OVER 18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age > 18 and disease LIKE '%"+cold+"%'"
            mycursor.execute(slct)
            cold1835 = mycursor.fetchone()

            mydb.commit()


            # FLU COUNT UNDER 10
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 10 and disease LIKE '%"+flu+"%'"
            mycursor.execute(slct)
            flub10 = mycursor.fetchone()

            mydb.commit()


            # COLD COUNT 11-18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 18 and disease LIKE '%"+flu+"%'"
            mycursor.execute(slct)
            flu18 = mycursor.fetchone()

            mydb.commit()

            # FLU COUNT OVER 18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age > 18 and disease LIKE '%"+flu+"%'"
            mycursor.execute(slct)
            flu1835 = mycursor.fetchone()

            mydb.commit()




            
            # MSLS COUNT UNDER 10
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 10 and disease LIKE '%"+measles+"%'"
            mycursor.execute(slct)
            mslsb10 = mycursor.fetchone()

            mydb.commit()


            # COLD COUNT 11-18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age <= 18 and disease LIKE '%"+measles+"%'"
            mycursor.execute(slct)
            msls18 = mycursor.fetchone()

            mydb.commit()

            # FLU COUNT OVER 18
            malaria = 'Malaria'

            slct = "SELECT COUNT(age) FROM diagnosisrecords WHERE age > 18 and disease LIKE '%"+measles+"%'"
            mycursor.execute(slct)
            msls1835 = mycursor.fetchone()

            mydb.commit()


            set['columns']= ('Disease', 'Total','0-10', '11-18','19-35')
            set.column("#0", width=0,  stretch=NO)
            set.column("Disease",anchor=CENTER, width=200)
            set.column("Total",anchor=CENTER, width=200)
            set.column("0-10",anchor=CENTER, width=200)
            set.column("11-18",anchor=CENTER, width=200)
            set.column("19-35",anchor=CENTER, width=200)

            set.heading("#0",text="",anchor=CENTER)
            set.heading("Disease",text="Disease",anchor=CENTER)
            set.heading("Total",text="Total",anchor=CENTER)
            set.heading("0-10",text="0-10",anchor=CENTER)
            set.heading("11-18",text="11-18",anchor=CENTER)
            set.heading("19-35",text="19-35",anchor=CENTER)


            set.insert(parent='',index='end',iid=0,text='',
            values=('Malaria',malariast,malariab10,malaria18,malaria1835))
            set.insert(parent='',index='end',iid=1,text='',
            values=('Typhoid',typhoidst,typhb10,typh18,typh1835))
            set.insert(parent='',index='end',iid=2,text='',
            values=('Cold',coldst,coldb10,cold18,cold1835))
            set.insert(parent='',index='end',iid=3,text='',
            values=('Flu',flust,flub10,flu18,flu1835))
            set.insert(parent='',index='end',iid=4,text='',
            values=('Measles',measlesst,mslsb10,msls18,msls1835))

            ws.mainloop()

        # PATIENT RECORDS WINDOW
        def patientrecords():
            patientw = Toplevel(window)
            patientw.title("PATIENT RECORDS")
            patientw.geometry("1166x718")
            patientw.iconbitmap('hospital.ico')
            # patientw.geometry('1166x718')
            patientw.state('zoomed')
            # patientw.iconbitmap('googleiCo.ico')
            patientw.configure(bg='#fff')
            # window.configure(bg='#fff')
            # window.resizable(False,False)

            q = StringVar()
            t1 = StringVar()
            t2 = StringVar()
            t3 = StringVar()
            t4 = StringVar()
            t5 = StringVar()
            t6 = StringVar()
            t7 = StringVar()
            t8 = StringVar()
            # t3 = StringVar()

            # Add image file
            bg = PhotoImage(file = "mainbg.png")

            # Show image using label
            label1 = Label(patientw, image = bg)
            label1.place(x = 0, y = 0)

            # mainlabel = Label(window, text='MEDEX DIAGNOSIS SYSTEM',font=('Microsoft YaHei UI Light',30),bg='#57a1f8',fg='white')
            # mainlabel.grid(row=0, column=0, padx=300, pady=10, rowspan=4, columnspan=6)


            def update(rows):
                trv.delete(*trv.get_children())
                for i in rows:
                    trv.insert('', 'end', values=i)

            def getrow(event):
                rowid = trv.identify_row(event.y)
                item = trv.item(trv.focus())  
                t1.set(item['values'][0])
                t2.set(item['values'][1])
                t3.set(item['values'][2])
                t4.set(item['values'][3])
                t5.set(item['values'][4])
                t6.set(item['values'][5])
                t7.set(item['values'][6])
                t8.set(item['values'][7])

            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="medexdiagnosis", auth_plugin="mysql_native_passowrd")
            cursor = mydb.cursor()

            wrapper1 = LabelFrame(patientw, text="PATIENT DATA")
            wrapper2 = LabelFrame(patientw, text="Search")
            wrapper3 = LabelFrame(patientw, text="Customer Data")

            wrapper1.pack(fill="both", expand="yes", padx=5, pady=5)
            # wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
            # wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

            trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6), show="headings", height="50")
            trv.pack()

            trv.heading(1, text="First Name")
            # trv.heading(2, text="Middle Name")
            trv.heading(2, text="SurName")
            trv.heading(3, text="Gender")
            trv.heading(4, text="Age")
            trv.heading(5, text="Occupation")
            # trv.heading(7, text="Marital Status")
            trv.heading(6, text="Address")


            trv.bind('<Double 1>', getrow)

            query = "SELECT firstname, surname, gender, age, occupation, address from patientrecords"
            cursor.execute(query)
            rows = cursor.fetchall()
            update(rows)
            # ,command=regpatient

            patientw.mainloop() 

        # MAIN PAGE GUI WINDOW    
        # Add image file
        bg = PhotoImage(file = "bgmain.png")

        # Show image using label
        label1 = Label(window, image = bg)
        label1.place(x = 0, y = 0)

        mainlabel = Label(window, text='MEDEX DIAGNOSIS SYSTEM',font=('Microsoft YaHei UI Light',30),fg='white')
        mainlabel.grid(row=0, column=0, padx=300, pady=10, rowspan=4, columnspan=6)

        # ,command=regpatient

        registerbtn = Button(window,width=35,padx=10,pady=10,text='NEW PATIENT',bg='#57a1f8',fg='white',border=0,command=diagnosis)
        registerbtn.grid(row=6, column=0, pady=10)

        existing = Button(window,width=35,padx=10,pady=10,text='EXISTING PATIENT',bg='#57a1f8',fg='white',border=0)
        existing.grid(row=7, column=0, pady=10)

        patientrecords = Button(window,width=35,padx=10,pady=10,text='PATIENT RECORDS',bg='#57a1f8',fg='white',border=0, command=patientrecords)
        patientrecords.grid(row=8, column=0, pady=10)

        statistics = Button(window,width=35,padx=10,pady=10,text='PATIENT STATISTICS',bg='#57a1f8',fg='white',border=0, command=statistics)
        statistics.grid(row=9, column=0, pady=10)

        devtools = Button(window,width=35,padx=10,pady=10,text='DEVELOPER TOOLS',bg='#57a1f8',fg='white',border=0)
        devtools.grid(row=10, column=0, pady=10)

        hellodr = Label(window, text='Welcome!',font=('Microsoft YaHei UI Light',17),bg='#57a1f8',fg='white')
        hellodr.grid(row=6, column=0, padx=300, pady=10, rowspan=4, columnspan=6)

        window.mainloop()

    else:
        messagebox.showerror('Invalid','Invalid  Username or Password')   

#############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def signup_command():
    window = Toplevel(root)

    window.title("MEDEX DIAGNOSIS SYSTEM - Sign Up")
    window.geometry("1166x718")
    window.configure(bg='#fff')
    window.resizable(False,False)



    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()


        if password == confirm_password:
            try:
                file = open('datasheet.txt','r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt','w')
                w = file.write(str(r))

                messagebox.showinfo('Sign Up','Successful!')
                window.destroy()

            except:
                    file = open('datasheet.txt','w')
                    pp = str({'Username':'Password'})
                    file.write(pp)
                    file.close()
        else:
            messagebox.showerror('Invalid','Both Password should match')            



    def signin():
        window.destroy()

    img = PhotoImage(file='login.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)

    frame = Frame(window,width=350,height=390,bg='white')
    frame.place(x=480,y=50)



    heading = Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    #################---------------------------
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')


    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


    #################---------------------------
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')


    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


    #################---------------------------
    def on_enter(e):
        confirm_code.delete(0,'end')

    def on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0,'Confirm Password')


    confirm_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0, 'Confirm Passowrd')
    confirm_code.bind("<FocusIn>",on_enter)
    confirm_code.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)


    ##############-----------

    Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label = Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=90,y=340)

    signin = Button(frame,width=6,text='Sign In',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signin)
    signin.place(x=200,y=340)



    window.mainloop()

###############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


img = PhotoImage(file='login1.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading = Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

########################-----------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')


user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

# ##############---------------------------

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0,'Password')


code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#############################################################
Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)


root.mainloop()
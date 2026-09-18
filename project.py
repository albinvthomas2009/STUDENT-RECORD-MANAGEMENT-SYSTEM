import mysql.connector as sql

def login():
    global user,password
    user = input("Enter the username: ").lower()
    password = input("Enter the password:")
    if user == 'root' and password == '30042009':
        print("SUCCESSFULLY LOGGED IN \n")
    else:
        print("USERNAME OR PASSWORD IS WRONG")
            

def connector():
    global dbcon,cursor
    dbcon = sql.connect(host='localhost',username=user,passwd=password,database='school')
    cursor = dbcon.cursor()

def add_student():
    global ans
    admno = int(input("Enter the Admission Number: "))
    name = input("Enter the Name: ").title()
    cls = input("Enter the Class: ")
    section = input("Enter the Secton: ").upper()
    stream = input("Enter the Stream Number: ").upper()
    gender = input("Enter the Gender: ").upper()
    DOB = input("Enter the DOB: ")
    sqlstr = "Insert into STUDENTS values('{}','{}','{}','{}','{}','{}','{}')".format(admno,name,cls,section,stream,gender,DOB)
    cursor.execute(sqlstr)
    ans = input("Enter more records?(Y/N): ").lower()
    dbcon.commit()

def add_faculty():
    global ans
    ans = 'y'
    f_id = input("Enter the Faculty ID: ").upper()
    f_name = input("Enter the Faculty Name: ").title()
    subject = input("Enter the subject: ").upper()
    sqlstr = "INSERT INTO FACULTY VALUES('{}','{}','{}')".format(f_id,f_name,subject)
    cursor.execute(sqlstr)
    ans = input("Enter more records?(Y/N): ").lower()
    dbcon.commit()
    
def display():
    sqlstr = 'Select * from STUDENTS'
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    for i in data:
        print(i)

def find_admno(adm_no):
    sqlstr = "Select * from STUDENTS where ADM_NO = ({})".format(adm_no)
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    for i in data:
        print(i)

def find_name(name):
    sqlstr = "Select * from STUDENTS where NAME = ('{}')".format(name)
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    for i in data:
        print(i)

def find_fid(f_id):
    sqlstr = "Select * from FACULTY where FACULTY_ID = ('{}')".format(f_id)
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    for i in data:
        print(i)    

def find_fname(f_name):
    sqlstr = "Select * from FACULTY where FACULTY_NAME = ('{}')".format(f_name)
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    for i in data:
        print(i)

def find_subject(subject):
    sqlstr = "Select * from FACULTY where SUBJECT = ('{}')".format(subject)
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    for i in data:
        print(i)
    
def sort_class(cls):
    sqlstr = "Select * from STUDENTS where CLASS = ('{}')".format(cls)
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    for i in data:
        print(i)

def sort_section(section):
    sqlstr = "Select * from STUDENTS where SECTION = ('{}')".format(section)
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    for i in data:
        print(i)

def sort_stream(stream):
    sqlstr = "Select * from STUDENTS S,STREAM ST WHERE S.STREAM_NO = ST.STREAM_NO AND ST.STREAM_NAME = ('{}')".format(stream)
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    for i in data:
        print(i)

def update_name(adm_no,name):
    sqlstr = "Update STUDENTS set NAME = ('{}') where ADM_NO = ({})".format(name,adm_no)
    cursor.execute(sqlstr)
    dbcon.commit()
    print("Data Updated Successfully")
    
def update_class(adm_no,cls):
    sqlstr = "Update STUDENTS set CLASS = ('{}') where ADM_NO = ({})".format(cls,adm_no)
    cursor.execute(sqlstr)
    print("Data Updated Successfully")
    dbcon.commit()
def update_section(adm_no,section):
    sqlstr = "Update STUDENTS set SECTION = ('{}') where ADM_NO = ({})".format(section,adm_no)
    cursor.execute(sqlstr)
    print("Data Updated Successfully")
    dbcon.commit()
    
def update_dob(adm_no,dob):
    sqlstr = "Update STUDENTS set DOB = ('{}') where ADM_NO = ({})".format(dob,adm_no)
    cursor.execute(sqlstr)
    print("Data Updated Successfully")
    dbcon.commit()

def update_faculty_name(f_id,name):
    sqlstr = "Update FACULTY set FACULTY_NAME = ('{}') where FACULTY_ID = ('{}')".format(name,f_id)
    cursor.execute(sqlstr)
    print("Data Updated Successfully")
    dbcon.commit()    

def update_faculty_subject(f_id,subject):
    sqlstr = "Update FACULTY set SUBJECT = ('{}') where FACULTY_ID = ('{}')".format(subject,f_id)
    cursor.execute(sqlstr)
    print("Data Updated Successfully")
    dbcon.commit()

def delete_admno(adm_no):
    sqlstr = "Delete from STUDENTS where ADM_NO = ({})".format(adm_no)
    cursor.execute(sqlstr)
    print("Data Deleted Successfully")
    dbcon.commit()    

def delete_name(name):
    sqlstr = "Delete from STUDENTS where NAME = ('{}')".format(name)
    cursor.execute(sqlstr)
    print("Data Deleted Successfully")
    dbcon.commit()

def delete_faculty_fid(f_id):
    sqlstr = "Delete from FACULTY where FACULTY_ID = ('{}')".format(f_id)
    cursor.execute(sqlstr)
    print("Data Deleted Successfully")
    dbcon.commit()
    
def delete_faculty_name(f_name):
    sqlstr = "Delete from FACULTY where FACULTY_NAME = ('{}')".format(f_name)
    cursor.execute(sqlstr)
    print("Data Deleted Successfully")
    dbcon.commit()
    



print('''
==================================
 STUDENT RECORD MANAGEMENT SYSTEM
==================================
''')

loop = 1
while loop == 1:
    print('1. LOGIN IN')
    print('2. EXIT \n')
    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        login()        
        loop+=1
        while loop == 2:
            connector()
            print('1. ADD DETAILS')
            print('2. FIND DETAILS')
            print('3. SORT DETAILS')
            print('4. UPDATE DETAILS')
            print('5. DELETE DETAILS')
            print('6. EXIT \n')
            menu = int(input("Enter your choice: "))
            print()

            
            if menu == 1:
                print('1. ADD STUDENT DETAILS')
                print('2. ADD FACULTY DETAILS \n')
                add_menu = int(input("Enter your choice: "))
                print()
                if add_menu == 1:
                    ans = 'y'
                    while ans == 'y':
                        add_student()
                elif add_menu == 2:
                    ans = 'y'
                    while ans == 'y':
                        add_faculty()
                else:
                    print("INVALID CHOICE")

                    
            elif menu == 2:
                print("1. STUDENT DETAILS")
                print("2. FACULTY DETAILS \n")
                find_menu = int(input("Enter your choice: "))
                print()
                if find_menu == 1:
                    print("1. FIND BY ADMISSION NUMBER")
                    print("2. FIND BY NAME \n")
                    find_sub_menu = int(input("Enter your choice: "))
                    print()
                    if find_sub_menu == 1:
                        adm_no = int(input("Enter the Admission Number to be found: "))
                        find_admno(adm_no)
                        print()
                    elif find_sub_menu == 2:
                        name = input("Enter the Name to be found: ").title()
                        find_name(name)
                        print()
                    else:
                        print("INVALID CHOICE")
                elif find_menu == 2:
                    print("1. FIND BY ID")
                    print("2. FIND BY NAME")
                    print("3. FIND BY SUBJECT \n")
                    find_sub_menu = int(input("Enter your choice: "))
                    print()
                    if find_sub_menu == 1:
                        f_id = input("Enter the Faculty ID to be found: ").upper()
                        find_fid(f_id)
                        print()
                    elif find_sub_menu == 2:
                        f_name = input("Enter the Faculty Name to be found: ").upper()
                        find_fname(f_name)
                        print()
                    elif find_sub_menu == 3:
                        subject = input("Enter the Subject to be found: ").upper()
                        find_subject(subject)
                        print()
                    else:
                        print("INVALID CHOICE")

                        
            elif menu == 3:
                print("1. SORT BY CLASS")
                print("2. SORT BY SECTION")
                print("3. SORT BY STREAM \n")
                sort_menu = int(input("Enter your choice: "))
                print()
                if sort_menu == 1:
                    cls = input("Enter the Class: ").upper()
                    sort_class(cls)
                    print()
                elif sort_menu == 2:
                    section = input("Enter the Section: ").upper()
                    sort_section(section)
                    print()
                elif sort_menu == 3:
                    print("Available Streams are:\n BIO-MATHS \n BIO-IP \n BIO-PSYCHOLOGY \n COMPUTER-MATHS")
                    stream = input("Enter the Stream Name: ").upper()
                    if stream in ['BIO-MATHS','BIO-IP','BIO-PSYCHOLOGY','COMPUTER-MATHS']:
                        sort_stream(stream)
                        print()
                    else:
                        print("ENTER THE STREAM NAME IN THE ABOVE MENTIONED FORMAT")
                else:
                    print("INVALID CHOICE")


            elif menu == 4:
                print("1. UPDATE STUDENT DETAILS")
                print("2. UPDATE FACULTY DETAILS \n")
                update_menu = int(input("Enter your choice: "))
                print()
                if update_menu == 1:
                    print("1. UPDATE NAME")
                    print("2. UPDATE CLASS")
                    print("3. UPDATE SECTION")
                    print("4. UPDATE DOB \n")
                    update_sub_menu = int(input("Enter your choice: "))
                    print()
                    if update_sub_menu == 1:
                        adm_no = input("Enter the Admission Number: ")
                        name = input("Enter the New Name: ").title()
                        update_name(adm_no,name)
                        print()
                    elif update_sub_menu == 2:
                        adm_no = input("Enter the Admission Number: ")
                        cls = input("Enter the New Class: ").upper()
                        update_class(adm_no,cls)
                        print()
                    elif update_sub_menu == 3:
                        adm_no = input("Enter the Admission Number: ")
                        section = input("Enter the New Section: ").upper()
                        update_section(adm_no,section)
                        print()
                    elif update_sub_menu == 4:
                        adm_no = input("Enter the Admission Number: ")
                        dob = input("Enter the New DOB in the format(yyyy-mm-dd): ")
                        update_dob(adm_no,dob)
                        print()
                    else:
                        print("INVALID CHOICE")
                elif update_menu == 2:
                    print("1. UPDATE NAME")
                    print("2. UPDATE SUBJECT \n")
                    update_sub_menu = int(input("Enter your choice: "))
                    print()
                    if update_sub_menu == 1:
                        f_id = input("Enter the Faculty ID: ").upper()
                        name = input("Enter the New Name: ").upper()
                        update_faculty_name(f_id,name)
                        print()
                    elif update_sub_menu == 2:
                        f_id = input("Enter the Faculty ID: ").upper()
                        subject = input("Enter the New Subject: ").upper()
                        update_faculty_subject(f_id,subject)
                        print()
                    else:
                        print("INVALID CHOICE")

                        
            elif menu == 5:
                print("1. DELETE STUDENT DETAILS")
                print("2. DELETE FACULTY DETAILS \n")
                delete_menu = int(input("Enter your choice: "))
                print()
                if delete_menu == 1:
                    print("1. DELETE WITH ADMISSION NUMBER")
                    print("2. DELETE WITH NAME \n")
                    delete_sub_menu = int(input("Enter your choice: "))
                    print()
                    if delete_sub_menu == 1:
                        adm_no = int(input("Enter the Admission Number to be DELETED: "))
                        delete_admno(adm_no)
                        print()
                    elif delete_sub_menu == 2:
                        name = input("Enter the Name to be DELETED: ").title()
                        delete_name(name)
                        print()
                    else:
                        print("INVALID CHOICE")
                elif delete_menu == 2:
                    print("1. DELETE WITH FACULTY ID")
                    print("2. DELETE WITH FACULTY NAME \n")
                    delete_sub_menu = int(input("Enter your choice: "))
                    print()
                    if delete_sub_menu == 1:
                        f_id = int(input("Enter the Faculty ID to be DELETED: ")).upper()
                        delete_faculty_fid(f_id)
                        print()
                    elif delete_sub_menu == 2:
                        f_name = input("Enter the Faculty Name to be DELETED: ").upper()
                        delete_faculty_name(f_name)
                        print()
                    else:
                        print("INVALID CHOICE")

                        
            elif menu == 6:
                print("THANK YOU")
                break
            else:
                print("INVALID CHOICE")            
    elif choice == 2:
        print('THANK YOU')
        break
    else:
        print("INVALID CHOICE")
    
    
    

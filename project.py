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
                print('2. ADD FACULTY DETAILS')
                add_menu = int(input("Enter your choice: "))
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
                print("2. FACULTY DETAILS")
                find_menu = int(input("Enter your choice: "))
                if find_menu == 1:
                    print("1. FIND BY ADMISSION NUMBER")
                    print("2. FIND BY NAME")
                    find_sub_menu = int(input("Enter your choice: "))
                    if find_sub_menu == 1:
                        adm_no = int(input("Enter the Admission Number to be found: ")).upper()
                        find_admno(adm_no)
                    elif find_sub_menu == 2:
                        name = input("Enter the Name to be found: ").title()
                        find_name(name)
                    else:
                        print("INVALID CHOICE")
                elif find_menu == 2:
                    print("1. FIND BY ID")
                    print("2. FIND BY NAME")
                    print("3. FIND BY SUBJECT")
                    find_sub_menu = int(input("Enter your choice: "))
                    if find_sub_menu == 1:
                        f_id = input("Enter the Faculty ID to be found: ").upper()
                        find_fid(f_id)
                    elif find_sub_menu == 2:
                        f_name = input("Enter the Faculty Name to be found: ").upper()
                        find_fname(f_name)
                    elif find_sub_menu == 3:
                        subject = input("Enter the Subject to be found: ").upper()
                        find_subject(subject)
                    else:
                        print("INVALID CHOICE")
            elif menu == 3:
                print("1. SORT BY CLASS")
                print("2. SORT BY SECTION")
                print("3. SORT BY STREAM")
                sort_menu = int(input("Enter your choice: "))
                if sort_menu == 1:
                    cls = input("Enter the Class: ")
                    sort_class(cls)
                elif sort_menu == 2:
                    section = input("Enter the Section: ").upper()
                    sort_section(section)
                elif sort_menu == 3:
                    print("Available Streams are:\n BIO-MATHS \n BIO-IP \n BIO-PSYCHOLOGY \n COMPUTER-MATHS")
                    stream = input("Enter the Stream Name: ").upper()
                    if stream in ['BIO-MATHS','BIO-IP','BIO-PSYCHOLOGY','COMPUTER-MATHS']:
                        sort_stream(stream)
                    else:
                        print("ENTER THE STREAM NAME IN THE ABOVE MENTIONED FORMAT")
                else:
                    print("INVALID CHOICE")


            elif menu == 4:
                print("1. UPDATE STUDENT DETAILS")
                print("2. UPDATE FACULTY DETAILS")
                update_menu = int(input("Enter your choice: "))
                if update_menu == 1:
                    print("1. UPDATE NAME")
                    print("2. UPDATE CLASS")
                    print("3. UPDATE SECTION")
                    print("4. UPDATE DOB")
                    update_sub_menu = int(input("Enter your choice: "))
                    if update_sub_menu == 1:
                        adm_no = input("Enter the Admission Number: ")
                        name = input("Enter the New Name: ")
                        update_name(adm_no,name)
                    elif update_sub_menu == 2:
                        adm_no = input("Enter the Admission Number: ")
                        cls = input("Enter the New Class: ")
                        update_class(adm_no,cls)
                    elif update_sub_menu == 3:
                        adm_no = input("Enter the Admission Number: ")
                        section = input("Enter the New Section: ")
                        update_section(adm_no,section)
                    elif update_sub_menu == 4:
                        adm_no = input("Enter the Admission Number: ")
                        dob = input("Enter the New DOB in the format(yyyy-mm-dd): ")
                        update_dob(adm_no,dob)
                    else:
                        print("INVALID CHOICE")
                elif update_menu == 2:
                    print("1. UPDATE NAME")
                    print("2. UPDATE SUBJECT")
                    update_sub_menu = int(input("Enter your choice: "))
                    if update_sub_menu == 1:
                        f_id = input("Enter the Faculty ID: ")
                        name = input("Enter the New Name: ")
                        update_faculty_name(f_id,name)
                    elif update_sub_menu == 2:
                        f_id = input("Enter the Faculty ID: ")
                        subject = input("Enter the New Subject: ")
                        update_faculty_subject(f_id,subject)
                    else:
                        print("INVALID CHOICE")
                        
                          

            elif menu == 5:
                print("1. DELETE STUDENT DETAILS")
                print("2. DELETE FACULTY DETAILS")
                delete_menu = int(input("Enter your choice: "))
                if delete_menu == 1:
                    print("1. DELETE WITH ADMISSION NUMBER")
                    print("2. DELETE WITH NAME")
                    delete_sub_menu = int(input("Enter your choice: "))
                    
                        
                
                    
                        
                

                
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
    
    
    

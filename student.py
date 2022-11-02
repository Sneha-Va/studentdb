import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='studentdb')
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add student')
    print('2 view all students')
    print('3 search a student')
    print('4 update the student')
    print('5 delete a student')
    print('6 exit')
    
    choice=int(input('enter the option:'))
    if(choice==1):
        print('student enter selected')
        name=input('enter the name')
        admnumber=input("enter admission number")
        rollnumber=input('enter rollnumber')
        college=input("enter the college name")
        sql='INSERT INTO `students`(`Name`, `rollnumber`, `admnumber`, `college`) VALUES (%s,%s,%s,%s)'
        data=(name,rollnumber,admnumber,college)
        mycursor.execute(sql,data)
        mydb.commit()
        print("view student")
    if(choice==2):
        print("view student")
    elif(choice==3):
        print('search a student')
    elif(choice==4):
        print('update the student')
    elif(choice==5):
        print('delete the student')
    elif(choice==6):
        break  
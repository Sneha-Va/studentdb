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
    print('6 insert mark')
    print('7 view all mark')
    print('8 subjectwise  mark')
    print('9. indiviual mark')
    print('10 exit')
    
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
       sql='SELECT * FROM `students`'
       mycursor.execute(sql)
       result=mycursor.fetchall()
       for i in result:
           print(i)
    elif(choice==3):
        print('search a student')
        admnumber=input("enter the admission number")
        sql='SELECT `id`, `name`, `rollnumber`, `admnumber`, `college` FROM `students` WHERE `admnumber`='+admnumber
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update the student')
        admnumber=input("enter admission number:")
        name=input('enter the name to be updated:')
        rollnumber=input('enter rollnumber to be updated:')
        college=input("enter the college name to be updated")
        sql="UPDATE `students` SET `name`='"+name+"',`rollnumber`='"+rollnumber+"',`college`='"+college+"' WHERE `admnumber`=" +admnumber
        mycursor.execute(sql)
        mydb.commit()
        print("data successfully updated")
    elif(choice==5):
        print('delete the student')
        admnumber=input("enter admission number:")
        sql='DELETE FROM `students` WHERE `admnumber`='+admnumber
        mycursor.execute(sql)
        mydb.commit()
    elif(choice==6):
        print("insert mark")
        admnumber=input("enter the admisson number" )
        sql='SELECT `id` FROM `students` WHERE `admnumber`='+admnumber
        mycursor.execute(sql)
        result=mycursor.fetchall()
        id=0
        for i in result:
           id=str(i[0])
        print('student id is:',id)
        physicsmark=input("enter physics  mark")
        chemistrymark=input("enter chemstry marks")
        mathsmark=input("enter maths mark")
        sql="INSERT INTO `marks`( `studentid`, `physicsmark`, `chemistrymark`, `mathsmark`) VALUES (%s,%s,%s,%s)"
        data=(id,physicsmark,chemistrymark,mathsmark)
        mycursor.execute(sql,data)
        mydb.commit()
    elif(choice==7):
        print("view  mark")
        print("view mark")
        sql="SELECT s.`name`, s.`rollnumber`, s.`admnumber`,s. `college`,m.physicsmark,m.chemistrymark,m.mathsmark FROM `students` s JOIN marks m ON s.id =m.studentid"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==8):
        print("subjectwise mark")
        subname=input("enter subjectname")
    if (subname=='physics'):
        sql="SELECT AVG ('physicsmark')FROM `marks`"
    elif (subname=='chemistry'):
        sql="SELECT AVG ('chemistrymark')FROM `marks`"
    elif (subname=='physics'):
        sql="SELECT AVG ('mathsmark')FROM `marks`"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
            
    elif(choice==9):
        print("individual marks")
        admnumber=input("enter the student admmision number")
        sql='SELECT `id` FROM `students` WHERE `admnumber`='+admnumber
        mycursor.execute(sql)
        result=mycursor.fetchall()
        id=0
        for i in result:
           id=str(i[0])
        sql="SELECT s.`name`, s.`rollnumber`, s.`admnumber`,s. `college`,m.physicsmark,m.chemistrymark,m.mathsmark FROM `students` s JOIN marks m ON s.id =m.studentid WHERE `admnumber`="+admnumber
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        
    
    elif(choice==10):
        break
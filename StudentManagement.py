import pyodbc

conn=pyodbc.connect(
    'DRIVER={SQL Server};' 
    'SERVER=DESKTOP-FVECEG9;' 
    'DATABASE=StudentManagement;'
    'Trusted_Connection=yes;'
)
cursor=conn.cursor()
#add student
def add_student():
    name=input("Enter name:")
    age=int(input("Enter age:"))
    city=input("Enter city:")

    query='''
    INSERT INTO Students(name,age,city)
    VALUES(?,?,?)
'''
    cursor.execute(query,(name,age,city))
    conn.commit()
    print("student addes successfully")

#view student
def view_students():
    cursor.execute("SELECT FROM Students")
    rows=cursor.fetchall()
    print("\n Student Record\n")
    for row in rows:
        print(f"ID:{row.id}")
        print(f"Name:{row.name}")
        print(f"age:{row.age}")
        print(f"City:{row.city}")

    print("-----------")

#update student
def update_student():
    student_id=int(input("Enter student id to update:"))
    new_city=input("Enter new city:")
    new_age=int(input("Enter new age:"))    

    query='''
    UPDATE Students
    SET city=?
    WHERE id=? 
'''    
    cursor.execute(query,(student_id,new_city,new_age ))
    conn.commit()
    print("Student added successfully")

#delete student
def delete_student():
    student_id=int(input("Enter student id to delete:")) 
    query='''
    DELETE FROM Students
    WHERE id=?
'''   
    cursor.execute(query,(student_id))
    conn.commit()
    print("Student deleted succesfully")

#main menu
while True:
    print("\n Student Management System\n")
    print("1.add student") 
    print("2.view student")
    print("3.update student ")
    print("4.delete student")
    print("5.Exit")
       
    choice=input("enter your choice:")
    if choice=='1':
        add_student()
    elif choice=='2':
        view_students()
    elif choice=='3':
        update_student()
    elif choice=='4':
        delete_student()
    elif choice=='5':
        print("Thank you")
        break
    else:
        print("invalid choice")

conn.close()        
                        

from flask import Flask,render_template , request,redirect,url_for 
import pyodbc
app=Flask(__name__)
conn=pyodbc.connect(
    'DRIVER={SQL Server};' 
    'SERVER=DESKTOP-FVECEG9;'
    'DATABASE=StudentManagement;'
    'Trusted_Connection=yes;'
)
cursor=conn.cursor()
@app.route('/')
def index():
     return render_template('index.html')
@app.route('/add',methods=['GET','POST'])
def add_student():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        query="INSERT INTO Students(name,age,city)VALUES(?,?,?)"
        cursor.execute(query,(name,age,city))
        conn.commit() 
        return redirect(url_for('view_students'))
    return render_template('add_student.html')
@app.route('/view')
def view_students():
    cursor.execute("SELECT * FROM Students")
    students=cursor.fetchall()
    return render_template('view_students.html',students=students)
@app.route('/update',methods=['GET','POST'])
def update_student():
    if request.method=='POST':
        student_id=request.form['id']
        age=request.form['age']
        city=request.form['city']
        query="UPDATE Students SET age=?,city=? WHERE id=?" 
        cursor.execute(query,(age,city,student_id))
        conn.commit()
        return redirect(url_for('view_students'))
    return render_template('update_student.html')
@app.route('/delete',methods=['GET','POST'])
def delete_student():
    if request.method=='POST':
        student_id=request.form['id']
        query="DELETE from students WHERE id=?"
        cursor.execute(query,(student_id))
        conn.commit()
        return redirect(url_for('view_students'))
    return render_template('delete_student.html')
@app.route('/exit')
def exit_page():
    return render_template('thankyou.html')
if __name__=='__main__':
    app.run(debug=True)

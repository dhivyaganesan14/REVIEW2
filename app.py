from flask import Flask, render_template,request,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
app.config['MYSQL_USER'] = 'kalyani'
app.config['MYSQL_PASSWORD'] = 'Kalyani96!'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'flaskapp'
app.secret_key = 'many random bytes'
mysql= MySQL(app)

def registerStudent(form):
    studentdetails=form
    Roll_No=studentdetails['stdid']
    First_Name=studentdetails['name']
    Middle_Name=studentdetails['name2']
    Last_Name=studentdetails['name3'] 
    Age=studentdetails['age']
    Year=studentdetails['year']
    Department=studentdetails['dept']
    Sem_No=studentdetails['semno'] 
    date=studentdetails['date']
    Password=studentdetails['pass']
    Ph_no=studentdetails['num'] 
    Email=studentdetails['email']
    cur=mysql.connection.cursor()
    cur.execute("SELECT * from student WHERE Email=%s",[Email])
    search = cur.fetchall()
    if search:
        return render_template('index.html')
    else:
        cur.execute("INSERT INTO student(Roll_No,First_Name,Middle_Name,Last_Name,Age,Year,Department,Sem_No,date,Password,Ph_no,Email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Roll_No,First_Name,Middle_Name,Last_Name,Age,Year,Department,Sem_No,date,Password,Ph_no,Email))
        mysql.connection.commit()
        cur.close()
        return render_template('home.html') 
    return render_template('index.html',name=First_Name)  



def registerFaculty(form):
    facultydetails= form
    First_Name=facultydetails['name']
    Middle_Name =facultydetails['name2']
    Last_Name=facultydetails['name3']
    Department=facultydetails['dept']
    Password=facultydetails['pass']
    Email=facultydetails['email']
    faculty_id=facultydetails['facid']
    course_name=facultydetails['coun']
    course_id=facultydetails['couid']
    cur=mysql.connection.cursor()
    cur.execute("SELECT * from faculty WHERE Email=%s",[Email])
    search = cur.fetchall()
    if search:
        cur.execute("INSERT INTO faculty(First_Name,Middle_Name,Last_Name,Password,Email,faculty_id,course_name,course_id,Department) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(First_Name,Middle_Name,Last_Name,Password,Email,faculty_id,course_name,course_id,Department))
        return render_template('index.html')
    else:
       
        mysql.connection.commit()
        cur.close()
        return render_template('faculty.html') 
    return render_template('index.html')

        
   
    

def registerAdmin(form):
    admindetails=form
    First_Name =admindetails['name']
    Middle_Name=admindetails['name2']
    Last_Name =admindetails['name3']
    Password =admindetails['pass']
    Email=str(admindetails['email'])
    mod_id=admindetails['modid']
    cur=mysql.connection.cursor()        
    cur.execute("SELECT * from admin WHERE Email=%s",[Email])
    search = cur.fetchall()
    if search:
        
        return render_template('index.html')
    else:
        cur.execute("INSERT INTO admin(First_Name,Middle_Name,Last_Name,Password,Email,mod_id) VALUES(%s,%s,%s,%s,%s,%s)",(First_Name,Middle_Name,Last_Name,Password,Email,mod_id))
        mysql.connection.commit()
        cur.close()
        return render_template('home.html') 
    return render_template('index.html')
    
    #registration logic

@app.route('/', methods=['GET','POST'])
def indexFn():
    #msg =''
    if request.method == 'POST':
        #fetch form data
        userDestails=request.form
        fname=userDestails['name']
        idlog=userDestails['idlog']
        mail=userDestails['email']
        password=userDestails['pass']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO login(fname,idlog,mail,password) VALUES(%s, %s,%s,%s)",(fname,idlog,mail,password))
        mysql.connection.commit()
        cur.close()
        return render_template('home.html')
    return render_template('index.html')   

@app.route('/login', methods=['POST'])
def login():
    #msg =''
    if request.method == 'POST' and 'email' in request.form and 'pass' in request.form:
        
        useremail = request.form['email']
        userpassword = request.form['pass']
        check=request.form['user']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if check=='student':
            cursor.execute('SELECT * FROM student')
            flag=cursor.fetchall()
            email_ids=[]
            passwd=[]
            for i in flag:
                email_ids.append(i['Email'])
                passwd.append(i['Password'])
            if useremail in email_ids and userpassword in passwd:                
                return render_template('home.html')
            else:
                return render_template('index.html')
        elif check=='faculty':
            cursor.execute('SELECT * FROM faculty')
            flag2=cursor.fetchall()
            email2_ids=[]
            passwd2=[]
            for i in flag2:
                email2_ids.append(i['Email'])
                passwd2.append(i['Password'])
            if useremail in email2_ids and userpassword in passwd2:                
                return render_template('faculty.html')
            else:
                return render_template('index.html')
        elif check=='admin':
            cursor.execute('SELECT * FROM admin')
            flag3=cursor.fetchall()
            email3_ids=[]
            passwd3=[]
            for i in flag3:
                email3_ids.append(i['Email'])
                passwd3.append(i['Password'])
            if useremail in email3_ids and userpassword in passwd3:                
                return render_template('home.html')
            else:
                return render_template('index.html')
        
      
     
    



@app.route('/register', methods=['GET','POST'])
def submit():
    #get the details from request
    if (request.args.get('type') == 'student'):
        registerStudent(request.form)    
    
    if(request.args.get('type')== 'faculty'):
        registerFaculty(request.form)    
    
    if(request.args.get('type')== 'admin'):
        registerAdmin(request.form)    
    return render_template('index.html')

@app.route('/question', methods=['GET','POST'])
def question():
    if request.method == 'POST':
      
        Questiondetails=request.form
        unique_id=Questiondetails['unique']
        course_id=Questiondetails['question']
        doubt =Questiondetails['Input']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO doubt(unique_id,course_id,doubt) VALUES(%s,%s, %s)",(unique_id,course_id,doubt))
        mysql.connection.commit()
        cur.close()
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM doubt")
        questions = cur.fetchall()
        cur.execute("SELECT * FROM answers")
        answers = cur.fetchall()
        return render_template('forum.html',questions=questions, answers=answers)
    
@app.route('/answer', methods=['GET','POST'])
def answer():
    if request.method == 'POST':
      
        Answerdetails=request.form
        diff_id=Answerdetails['uni']
        answer=Answerdetails['answer']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO answers(diff_id,answer) VALUES(%s,%s)",(diff_id,answer))
        mysql.connection.commit()
        cur.close()
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM doubt")
        questions = cur.fetchall()
        cur.execute("SELECT * FROM answers")
        answers = cur.fetchall()
        return render_template('forum.html',questions=questions, answers=answers)
    
@app.route('/about-us', methods=['GET'])
def about_us():
    return render_template('about-us.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/course', methods=['GET'])
def course():
    return render_template('course.html')

@app.route('/forum', methods=['GET'])
def forum():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM doubt")
    questions = cur.fetchall()
    cur.execute("SELECT * FROM answers")
    answers = cur.fetchall()
    return render_template('forum.html',questions=questions, answers=answers)

@app.route('/review', methods=['GET'])
def review():
    return render_template('review.html')

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/faculty', methods=['GET'])
def faculty():
    return render_template('faculty.html')

if __name__=="__main__":
    app.secret_key='12345'
    app.run('127.0.0.1', 5000, debug=True)


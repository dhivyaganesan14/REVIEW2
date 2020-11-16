from flask import Flask, render_template,request
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
app.config['MYSQL_USER'] = 'kalyani'
app.config['MYSQL_PASSWORD'] = 'Kalyani96!'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'flaskapp'
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
    cur.execute("INSERT INTO student(Roll_No,First_Name,Middle_Name,Last_Name,Age,Year,Department,Sem_No,date,Password,Ph_no,Email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Roll_No,First_Name,Middle_Name,Last_Name,Age,Year,Department,Sem_No,date,Password,Ph_no,Email))
    mysql.connection.commit()
    cur.close()
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
    cur.execute("INSERT INTO faculty(First_Name,Middle_Name,Last_Name,Password,Email,faculty_id,course_name,course_id,Department) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(First_Name,Middle_Name,Last_Name,Password,Email,faculty_id,course_name,course_id,Department))
    mysql.connection.commit()
    cur.close()
    return render_template('index.html',name=First_Name) 

        
   
    

def registerAdmin(form):
    admindetails=form
    First_Name =admindetails['name']
    Middle_Name=admindetails['name2']
    Last_Name =admindetails['name3']
    Password =admindetails['pass']
    Email=str(admindetails['email'])
    mod_id=admindetails['modid']
    cur=mysql.connection.cursor()
    
    query = "SELECT * from admin WHERE Email=dhivya123@gmail.com"
    # query = "SELECT * from admin WHERE Email=dhivya123@gmail.com"    
    search=cur.execute(query)
    if search:
        return render_template('index.html')
    else:
        cur.execute("INSERT INTO admin(First_Name,Middle_Name,Last_Name,Password,Email,mod_id) VALUES(%s,%s,%s,%s,%s,%s)",(First_Name,Middle_Name,Last_Name,Password,Email,mod_id))
        mysql.connection.commit()
        cur.close()
        return render_template('home.html') 
    return render_template('index.html')

"""
    if user = flaskapp.query.filter(flaskapp.Email==Email).first(): 
        return render_template('index.html')
    else:
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO admin(First_Name,Middle_Name,Last_Name,Password,Email,mod_id) VALUES(%s,%s,%s,%s,%s,%s)",(First_Name,Middle_Name,Last_Name,Password,Email,mod_id))
        mysql.connection.commit()
        cur.close()
        return render_template('home.html') 
    return render_template('index.html')
    
 """   
    
    #registration logic

@app.route('/', methods=['GET','POST'])
def login():
    #msg =''
    if request.method == 'POST':
        #fetch form data
        userDestails=request.form
        fname=userDestails['name']
        idlog=userDestails['idlog']
        mail=userDestails['email']
        password=userDestails['pass']
        # Check if account exists using MySQL
       # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #cursor.execute('SELECT * FROM ADMIN WHERE Email = %(Email)s AND Password = %(Password)d')
        # Fetch one record and return result
        #account = cursor.fetchone()
        # If account exists in accounts table in out database
       # if account:
            #userDestails['fname'] = account['fname']
         #   mail=account['Email']
        #    password=account['Password']
            # Redirect to home page
          #  return 'Logged in successfully!'
        #else:
            # Account doesnt exist or username/password incorrect
         #   msg = 'Incorrect username/password!'

          
       # pwCheck = .execute("SELECT password FROM users WHERE email = :mail", {"uname": mail}).fetchone()

        #if pwCheck == password:
        #   return render_template("home.html")
        #else:
         #   return render_template("index.html", logintry="Login Failure")
   
   # else:
    #    return render_template("login.html")
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO login(fname,idlog,mail,password) VALUES(%s, %s,%s,%s)",(fname,idlog,mail,password))
        mysql.connection.commit()
        cur.close()
        return render_template('home.html')
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
        course_id=Questiondetails['question']
        doubt =Questiondetails['Input']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO doubt(course_id,doubt) VALUES(%s, %s)",(course_id,doubt))
        mysql.connection.commit()
        cur.close()
    return render_template('forum.html', first=course_id,second=doubt)
    




    
      



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
    return render_template('forum.html')

@app.route('/review', methods=['GET'])
def review():
    return render_template('review.html')

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run('127.0.0.1', 5000, debug=True)


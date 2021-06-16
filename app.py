from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.config['SECRET_KEY']='11'
@app.route('/')
def index():
    return render_template('home.html')

def eo(num1):
    if num1%2==0 :
        return 'even'
    else :
        return 'odd'

@app.route('/numbers')
def numbers():
    return render_template("even_odd.html")

@app.route("/even_odd",methods=["post"])
def even_odd():
    num2 = request.form.get("number")
    num2=int(num2)
    result = eo(num2)
    return render_template("even_odd.html",result=result)

@app.route('/reverseletters',methods = ['post'])
def reverseletters():

    rev = request.form.get('letters')
    result1=rs(rev)
    return render_template('reverseletters.html',result1=result1)

@app.route('/getletters')
def let():
    return render_template('reverseletters.html')


def rs(str1):
    

    rev_str=''
    for i in str1 :
        rev_str=i+rev_str
    return rev_str


@app.route("/getq1")
def getq1():
    return render_template("q1.html")

@app.route('/q1',methods=["post"])
def q1():
    userinput =request.form.get('select')
    message=''
    score=session.get('your_score',0)
    if userinput =="1":
        score = score+50
        message="Congarts thats the corrrect answer"
    else:
        message="Sorry incorrect answer"
    session['your_score'] = score
    return render_template("q2.html",message =message,score=score)


@app.route('/q2',methods = ['post'])
def q2():
    userinput =request.form.get('select')
    message=''
    score=session.get('your_score',0)
    if userinput =="4":
        score = score+50
        message="Congarts thats the corrrect answer"
    else:
        message="Sorry incorrect answer"
    session['your_score'] = score
    return render_template("q3.html",message =message,score = score)


@app.route('/q3',methods = ['post'])
def q3():
    userinput =request.form.get('select')
    message=''
    score=session.get('your_score',0)

    if userinput =="2":
        score = score+50
        message="Congarts thats the corrrect answer"
    else:
        message="Sorry incorrect answer"
    session['user_score'] = score
    return render_template("q4.html",message =message,score = score)



@app.route('/q4',methods = ['post'])
def q4():
    userinput =request.form.get('select')
    message=''
    score=session.get('your_score',0)
    if userinput =="3":
        score = score+50
        message="Congarts thats the corrrect answer"
    else:
        message="Sorry incorrect answer"
    session['user_score'] = score
    return render_template("q5.html",message =message,score = score)


@app.route('/q5',methods = ['post'])
def q5():
    userinput =request.form.get('select')
    message=''
    score=session.get('your_score',0)
    if userinput =="4":
        score = score+50
        message="Congarts thats the corrrect answer"
    else:
        message="Sorry incorrect answer"
    session['your_score'] = score
    return render_template("q6.html",message =message,score = score)


@app.route('/q6',methods = ['post'])
def q6():
    userinput =request.form.get('select')
    message=''
    score=session.get('your_score',0)
    if userinput =="2":
        score = score+50
        message="Congarts thats the corrrect answer"
    else:
        message="Sorry incorrect answer"
    session['your_score'] = score
    return render_template("home.html",message =message,score = score)


@app.route('/coding')
def coding():
    return render_template('coding.html')
    
@app.route('/login')
def login():
    return render_template('loginpage.html')
@app.route('/validateuser', methods = ['post'])
def validateuser():
    username = request.form.get('username')
    password = request.form.get('password')
    print(session.get('user1'))
    if username == session.get('user1') and password == session.get('pass2'):
        print('login successful')
        session['user']=username
        return render_template('q1.html',message = 'login successful')
    else:
        print('intake unsuccessful')
        return redirect('/login')
    
@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/thankyou', methods = ['post'])
def thankyou():
   username1 = request.form.get('username')
   password2 = request.form.get('password')
   email = request.form.get('email')
   city = request.form.get('city')
   session['user1']=username1
   session['pass2']=password2
   return render_template('/loginpage.html',message = 'registration successful')
  

"""
1. creating html file 
2.accepting user input
3. validatingthe input
"""










if __name__ == '__main__':
    app.run(debug=True)


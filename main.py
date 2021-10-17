from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os


app = Flask(__name__)
app.static_folder = 'static'

app.secret_key = os.urandom(24)


conn = mysql.connector.connect(host="sql6.freesqldatabase.com", user="sql6444733", password="sipdWf1gH1", database="sql6444733")
cursor = conn.cursor()


@app.route('/')
def ahome():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def registration():
    return render_template('register.html')


@app.route('/newuserinput')
def newuserinput():
    return render_template('newuserinput.html')


@app.route('/newuser')
def newuser():
    if 'ID' in session:
        return redirect('/newuserinput')
    else:
        return redirect('/register')


@app.route('/login_validation', methods=["GET","POST"])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM `users_healthyapp` WHERE `Email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
    users = cursor.fetchall()
    if len(users) > 0:
        session['ID'] = users[0][0]
        return redirect('/index')
    else:
        return redirect('/')


@app.route('/add_user', methods=["POST"])
def add_user():
    uname = request.form.get('uname')
    uemail = request.form.get('uemail')
    upassword = request.form.get('upassword')

    cursor.execute("""INSERT INTO `users_healthyapp`(`ID`,`Name`,`Email`,`password`) VALUES(NULL,'{}','{}','{}')""".format(uname, uemail, upassword))
    conn.commit()

    cursor.execute("""SELECT * FROM `users_healthyapp` WHERE `Email` LIKE '{}'""".format(uemail))
    myuser = cursor.fetchall()
    session['ID'] = myuser[0][0]
    return redirect('/newuserinput')


@app.route('/service')
def service():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about-usdiet.html')


@app.route('/add_newuser', methods=["POST"])
def add_newuser():
    name = request.form.get('nuser_name')
    email = request.form.get('nemail')
    age_user = request.form.get('age')
    gender_user = request.form.get('gender')
    weight_user = request.form.get('weight')
    height_user = request.form.get('height')
    health_issue_user = request.form.get('health_issue')
    cursor.execute("""INSERT INTO `newuser`(`userID`,`Email`,`Name`,`Age`,`Gender`,`Weight(in kgs)`,`Height(in m)`,`Health issues`) VALUES(NULL,'{}','{}','{}','{}','{}','{}','{}')""".format(name, email, age_user, gender_user, weight_user, height_user, health_issue_user))
    conn.commit()

    cursor.execute("""SELECT * FROM `newuser` WHERE `Email` LIKE '{}'""".format(email))
    new_user = cursor.fetchall()
    session['userID'] = new_user[0][0]
    return redirect('/index')


@app.route('/users')
def users():
    cursor.execute("SELECT * FROM newuser")
    userdetails = cursor.fetchall()
    return render_template('users.html', userdetails=userdetails)


@app.route('/dietician')
def logindietician():
    return render_template('dietician.html')


@app.route('/dieticianregister')
def registrationdietician():
    return render_template('dieticianreg.html')


@app.route('/dieticianafterlogin')
def afterlogindietician():
    return render_template('dieticianafterlogin.html')


@app.route('/newmentor')
def newmentor():
    if 'mentorID' in session:
        return redirect('/dieticianafterlogin')
    else:
        return redirect('/dieticianregister')


@app.route('/mentorlogin_validation', methods=["GET","POST"])
def mentorlogin_validation():
    memail = request.form.get('dietemail')
    mpassword = request.form.get('dietpassword')

    cursor.execute("""SELECT * FROM `dietician` WHERE `mentoremail` LIKE '{}' AND `mentorpassword` LIKE '{}'""".format(memail, mpassword))
    mentors = cursor.fetchall()
    if len(mentors) > 0:
        session['mentorID'] = mentors[0][0]
        return redirect('/dieticianafterlogin')
    else:
        return redirect('/')


@app.route('/mentoradd_user', methods=["GET","POST"])
def mentoradd_user():
    plannername = request.form.get('dieticianname')
    planneremail = request.form.get('dieticianemail')
    plannerpassword = request.form.get('dieticianpassword')

    cursor.execute("""INSERT INTO `dietician`(`mentorID`,`mentorname`,`mentoremail`,`mentorpassword`) VALUES(NULL,'{}','{}','{}')""".format(plannername, planneremail, plannerpassword))
    conn.commit()

    cursor.execute("""SELECT * FROM `dietician` WHERE `mentoremail` LIKE '{}'""".format(planneremail))
    mymentoruser = cursor.fetchall()
    session['mentorID'] = mymentoruser[0][0]
    return redirect('/deiticianafterlogin')


@app.route('/add_mentornewuser', methods=["GET","POST"])
def add_mentornewuser():
    mentordietname = request.form.get('mentorusername')
    mentordietemail = request.form.get('mentorsemail')
    mentordietage = request.form.get('mentorage')
    mentordietgender = request.form.get('mentorgender')
    duration = request.form.get('time')
    diseaserelated = request.form.get('disease')
    dietplan = request.form.get('diet-plan')
    cursor.execute("""INSERT INTO `mentor_dietplan`(`dieticianID`, `Email`, `Name`, `Age`, `Gender`, `Time`, `Disease`, `Recipe`) VALUES(NULL, '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(mentordietname, mentordietemail, mentordietage, mentordietgender, duration, diseaserelated, dietplan))
    conn.commit()

    cursor.execute("""SELECT * FROM `mentor_dietplan` WHERE `Email` LIKE '{}'""".format(mentordietemail))
    mentorsgotID = cursor.fetchall()
    session['dieticianID'] = mentorsgotID[0][0]
    return redirect('/dieticianprofile')


#@app.route('/mentorprofile')
#def mentorprofile():
 #   cursor.execute("""SELECT * FROM `mentor_dietplan`""")
  #  mentorkey = cursor.fetchall()
   # return render_template('dieticianprofile.html', mentorkey=mentorkey)


@app.route('/menu-thy')
def thyroidmenu():
    return render_template('menu-thy.html')


@app.route('/mealoption')
def tothemenupage():
    return render_template('mealoption.html')


@app.route('/menu-nancy')
def menunancy():
    return render_template('menu nancy.html')


@app.route('/menu-pcos')
def spellingmistake():
    return render_template('mneu-pcos.html')


@app.route('/menu-dia')
def diabetesmenu():
    return render_template('menu-dia.html')

@app.route('/diseases')
def kindsofdiseases():
    return render_template('diseases.html')


@app.route('/index-diet')
def indexdiet():
    return render_template('index-diet.html')

@app.route('/index')
def indexpage():
    return render_template('index.html')

@app.route('/exercise')
def gotoexercise():
    return render_template('exercise.html')

@app.route('/custom-diet')
def customdiet():
    return render_template('customdiet.html')

@app.route('/servicesdiet')
def diet():
    return render_template('servicesdiet.html')

@app.route('/dieticianprofile')
def profile():
    return render_template('dieticianprofile.html')

@app.route('/record-dia')
def recorddia():
    return render_template('record-dia.html')

@app.route('/record-thy')
def recordthy():
    return render_template('record-thy.html')

@app.route('/record-pcos')
def recordpcos():
    return render_template('record-pcos.html')

@app.route('/profile')
def profileofuser():
    return render_template('profile.html')

@app.route('/user_input_diet', methods=["POST"])
def userdietplan():
    breakfast_user = request.form.get('break_fast')
    lunch_user = request.form.get('lunch')
    dinner_user = request.form.get('dinner')
    cursor.execute("""INSERT INTO `user_diet_input`(`Breakfast`, `Lunch`, `Dinner`) VALUES('{}', '{}', '{}')""".format(breakfast_user,lunch_user,dinner_user))
    conn.commit()

   # cursor.execute("""SELECT * FROM `mentor_dietplan` WHERE `Email` LIKE '{}'""".format(mentordietemail))
   # mentorsgotID = cursor.fetchall()
   # session['dieticianID'] = mentorsgotID[0][0]
    return redirect('/index')


@app.route('/user_diet')
def usersdiet():
    cursor.execute("SELECT * FROM user_diet_plan")
    userdietdetails = cursor.fetchall()
    return render_template('user_diet_show.html', userdietdetails=userdietdetails)


@app.route('/add_plan', methods=["POST"])
def adddietplan():
    breakfast_add_diet = request.form.get('break_fast_diet')
    lunch_add_diet = request.form.get('lunch_diet')
    dinner_add_diet = request.form.get('dinner_diet')
    cursor.execute("""INSERT INTO `add_diet_plan`(`Breakfast`, `Lunch`, `Dinner`) VALUES('{}', '{}', '{}')""".format(breakfast_add_diet, lunch_add_diet, dinner_add_diet))
    conn.commit()
    
    return redirect('/index-diet')
    
@app.route('/add_diet')
def adddiet():
    cursor.execute("SELECT * FROM add_diet_plan")
    adddietdetails = cursor.fetchall()
    return render_template('add_diet_dietician.html', adddietdetails=adddietdetails)


@app.route('/logout')
def logout():
    session.pop('ID')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

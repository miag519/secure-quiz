import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable. 
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')
    
@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    error = None
    if 'which1' in session:
        error = "no going back! try again"
    else:
        session["which1"]=request.form['which1']
        return render_template('page2.html')
    session.clear()
    return render_template('home.html', error=error)


@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    error = None
    if 'which2' in session:
        error = "no going back! try again"
    else:
        session["which2"]=request.form['which2']
        return render_template('page3.html')
    session.clear()
    return render_template('home.html', error=error)
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    error = None
    if 'which3' in session:
        error = "no going back! try again"
    else:
        session["which3"]=request.form['which3']
        return render_template('page4.html')
    session.clear()
    return render_template('home.html', error=error)
    
@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    error = None
    if 'which4' in session:
        error = "no going back! try again"
    else:
        session["which4"]=request.form['which4']
        return render_template('page5.html')
    session.clear()
    return render_template('home.html', error=error)
    
@app.route('/page6',methods=['GET','POST'])
def renderPage6():
    error = None
    if 'which5' in session:
        error = "no going back! try again"
    else:
        session["which5"]=request.form['which5']
        return render_template('page6.html')
    session.clear()
    return render_template('home.html', error=error)
    
@app.route('/page7',methods=['GET','POST'])
def renderPage7():
    if 'which6' in session:
        error = "no going back! try again"
    else:
        session["which6"]=request.form['which6']
        results = result()
        ans1 = answer1()
        ans2 = answer2()
        ans3 = answer3()
        ans4 = answer4()
        ans5 = answer5()
        ans6 = answer6()
        return render_template('page7.html', result = results, answer1 = ans1, answer2 = ans2, answer3 = ans3, 
        answer4 = ans4, answer5 = ans5, answer6 = ans6)
        session.clear()
        return render_template('home.html', error=error)
    
def result():
    result = 0
    if session["which1"] == "star":
        result += 1
 
    if session["which2"] == "orion":
        result += 1
    
    if session["which3"] == "cygnus":
        result += 1
    
    if session["which4"] == "draco":
        result += 1
    
    if session["which5"] == "hydrus":
        result += 1
    
    if session["which6"] == "three":
        result += 1
        
    return result
	
    
def answer1():
    answer1 = None
    if session['which1'] == "star":
        answer1 = "Correct"
    else: 
        answer1 = "Incorrect"
    return answer1
	
def answer2():
    answer2 = None
    if session['which2'] == "orion":
        answer2 = "Correct"
    else: 
        answer1 = "Incorrect"
    return answer1
	
def answer3():
    answer3 = None
    if session['which3'] == "cygnus":
        answer3 = "Correct"
    else: 
        answer3 = "Incorrect"
    return answer3
	
def answer4():
    answer4 = None
    if session['which4'] == "draco":
        answer4 = "Correct"
    else: 
        answer4 = "Incorrect"
    return answer4
	
def answer5():
    answer5 = None
    if session['which5'] == "hydrus":
        answer5 = "Correct"
    else: 
        answer5 = "Incorrect"
    return answer5
    
def answer6():
    answer6 = None
    if session['which6'] == "three":
        answer6 = "Correct"
    else: 
        answer6 = "Incorrect"
    return answer6
    




    
    
    


    
if __name__=="__main__":
    app.run(debug=True)

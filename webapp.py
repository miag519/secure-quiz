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
    session["which1"]=request.form['which1']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["which2"]=request.form['which2']
    return render_template('page3.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    session["which3"]=request.form['which3']
    return render_template('page4.html')
    
@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    session["which4"]=request.form['which4']
    return render_template('page5.html')
    
@app.route('/page6',methods=['GET','POST'])
def renderPage6():
    session["which5"]=request.form['which5']
    return render_template('page6.html')
    
@app.route('/page7',methods=['GET','POST'])
def renderPage7():
    session["answer"]=request.form['answer']
    return render_template('page7.html')
    


    

    
if __name__=="__main__":
    app.run(debug=True)

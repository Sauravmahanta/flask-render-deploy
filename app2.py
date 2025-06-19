
## Create a simple flask application
from flask import Flask, render_template, request, redirect, url_for, jsonify #This line imports the Flask class from the flask library. Flask is a class used to create a Flask web application.

## create the flask app
app= Flask(__name__) #This creates an instance of the Flask application. __name__ is a special Python variable. It is used so Flask knows where to look for resources like templates and static files.

## Flask app routing
@app.route('/',methods=['GET']) 
# This is a decorator that tells Flask: 
# 1)Which URL should trigger the associated function.@app.route('/') maps the root URL (/) of the website to the function below.
# 2) methods=['GET'] specifies that this route only accepts GET requests (the default method used when you enter a URL in your browser).
def home():
    return "Hello! Saurav, Welcome to Home page"

@app.route('/index',methods=["GET"])
def index():
    return "Hello! Saurav"

# Variable Rule
@app.route('/success/<score>')
def success(score):
    return "the person is passed and the score is "+score
@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is "+str(score)

# Displaying html page/ html page rendering 
@app.route('/form',methods=['POST','GET'])
def form():
    if request.method=='GET':
        return render_template('form.html')
 
 # html page rendering and URL redirecting   
@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths']) #request.form accesses form input data (submitted via POST).
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        # return redirect(url_for(result,score=average_marks))

        return render_template('result.html',results=average_marks)

# Creating API without using html
@app.route("/api",methods=["GET","POST"])
def calculate_sum():
    if request.method == "GET":
        return jsonify({"message": "Send a POST request with JSON {'a': number, 'b': number} to calculate sum"})
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)





if __name__=="__main__": # This is the Python way of saying: only run the app if this file is being run directly, not if it’s imported as a module.
    app.run(debug=True) # Automatically reloads the app when you make changes.
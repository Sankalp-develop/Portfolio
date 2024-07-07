# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,request,redirect,url_for,render_template
from functions import validateuser,register_newuser


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        key = request.form['password']
        email = request.form['email']
        print(user,key,email)
        if(register_newuser(user,key,email)):
            return redirect(url_for('home'))
        else:
             return redirect(url_for('register'))
    else:
        return render_template('register.html')

@app.route('/home/<name>')
def home_name(name):
    return render_template('home.html', name = name)

@app.route('/login', methods=['POST', 'GET'])
def login():
   
    if request.method == 'POST':
        user = request.form['nm']
        key = request.form['pass']
        print(user,key)

        if(validateuser(user,key)):
            return redirect(url_for('home_name',name=user))
        else:
            return render_template('login.html',Error = True) 
    else:
        user = request.args.get('nm')
        return redirect(url_for('home_name',name='Guest'))


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
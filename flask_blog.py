from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f0340dd98a079ace260952bec2bca1a8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
from models import User,Post

posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'April 20, 2018'
    },
    {
        'author':'Johon Corner',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'April 21 , 2018'
    }
]

@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password!','danger')
    return render_template('login.html',title='Login',form=form)

if __name__=='__main__':
    app.run(debug=True)
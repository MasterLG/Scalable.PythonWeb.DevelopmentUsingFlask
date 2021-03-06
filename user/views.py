from flask import Blueprint, render_template,request,redirect,session,url_for
from user.forms import RegisterForm, LoginForm
import bcrypt
from user.models import User

user_app = Blueprint('user_app', __name__)  # naming the app


@user_app.route('/login', methods=["GET", "POST"])
def login():
    form=LoginForm()
    error=None

    if form.validate_on_submit():
        user=User.objects.filter(
            username=form.username.data
        ).first()
        if user:#user found
            if bcrypt.hashpw(form.password.data,user.password)==user.password:
                print("2")
                session['username']=form.username.data
                return 'User logged in'
            else:
                user =None
        if not user:#password is incorrent
            error='Incorrect credentials'
    return render_template('user/login.html',form=form,error=error)


@user_app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(username=form.username.data,
                    password=hashed_password,
                    email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data)
        user.save()
        return "User registered"
    return render_template('user/register.html', form=form)

@user_app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop('username')
    return redirect(url_for('user_app.login'))

@user_app.route('/<username>', methods=["GET", "POST"])
def profile(username):
    user=User.objects.filter(username=username).first()
    return render_template('user/profile.html',user=user)
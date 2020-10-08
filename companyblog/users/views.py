from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from companyblog import db
from companyblog.models import User,BlogPost
from companyblog.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from companyblog.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)


#register
@users.rout('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.valiadte_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password,data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)    
#login
#logout
@users.rout('/logout')
def logout():
    login_user()
    return redirect(url_for('core.index'))
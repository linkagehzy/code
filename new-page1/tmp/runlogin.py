import os
from app import app
from forms import LoginForm
from flask_wtf.csrf import CsrfProtect
from models import User
from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import logout_user
from flask import render_template


app.secret_key = os.urandom(24)

# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)

@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)


# csrf protection
csrf = CsrfProtect()
csrf.init_app(app)

@app.route('/')
@app.route('/login')

def login():
	form = LoginForm()
	if form.validate_on_submit():
		user_name = request.form.get('username', None)
		password = request.form.get('password', None)
		remember_me = request.form.get('remember_me', False)
		user = User(user_name, password)
		if user.verify_password(password):
			login_user(user)
			return redirect(request.args.get('next') or url_for('main'))
	return render_template('login.html', title="Sign In", form=form)

app.run(debug = True)



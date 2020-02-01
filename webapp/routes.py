
from flask import render_template, url_for, flash, redirect
from webapp import app, db, bcrypt
from webapp.forms import QueryForm
#from webapp.tfworld import Infer

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = QueryForm()
    if form.validate_on_submit():
        #title, abstractR, link = Infer(query=form.query.data, top_k_results=form.top_k.data)
        title, abstractR, link = ["Test"], ["Testing"], ["testing.com"]
        flash(title[0])
        flash(title[0])
        flash('Generating Recommendations')
        return redirect(url_for('home'))
    return render_template('home.html', title='NLPRecommendations' , form=form)


@app.route("/about")
def about():
    return redirect(url_for('home')) #Would change to


# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash(f'Your account has been created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)

from flask import render_template, url_for, flash, redirect
from webapp import app, db, bcrypt
from webapp.forms import QueryForm
from webapp.tfworld import Infer

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = QueryForm()
    if form.validate_on_submit():
        title, abstractR, link = Infer(query=form.query.data, top_k_results=form.top_k.data)
        #title, abstractR, link = ["A Paper About Something", "Another Paper About Something Else", "One Last Paper"], ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam finibus augue ex, ut bibendum turpis dignissim sed. Fusce rutrum orci ut auctor efficitur. Aliquam nibh nibh, porttitor sit amet lacus sit amet, facilisis ultrices urna. Donec sit amet magna quis urna maximus vehicula. Nullam lacinia augue at diam accumsan, et laoreet odio elementum. Fusce accumsan metus ante, eu eleifend massa finibus sed. Vivamus interdum, sem sed auctor finibus, ante metus consectetur leo, sit amet hendrerit libero libero ac lacus. Morbi accumsan id erat sit amet auctor. Sed tempus tincidunt risus tempus gravida.", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam finibus augue ex, ut bibendum turpis dignissim sed. Fusce rutrum orci ut auctor efficitur. Aliquam nibh nibh, porttitor sit amet lacus sit amet, facilisis ultrices urna. Donec sit amet magna quis urna maximus vehicula. Nullam lacinia augue at diam accumsan, et laoreet odio elementum. Fusce accumsan metus ante, eu eleifend massa finibus sed. Vivamus interdum, sem sed auctor finibus, ante metus consectetur leo, sit amet hendrerit libero libero ac lacus. Morbi accumsan id erat sit amet auctor. Sed tempus tincidunt risus tempus gravida", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam finibus augue ex, ut bibendum turpis dignissim sed. Fusce rutrum orci ut auctor efficitur. Aliquam nibh nibh, porttitor sit amet lacus sit amet, facilisis ultrices urna. Donec sit amet magna quis urna maximus vehicula. Nullam lacinia augue at diam accumsan, et laoreet odio elementum. Fusce accumsan metus ante, eu eleifend massa finibus sed. Vivamus interdum, sem sed auctor finibus, ante metus consectetur leo, sit amet hendrerit libero libero ac lacus. Morbi accumsan id erat sit amet auctor. Sed tempus tincidunt risus tempus gravida."], ["https://google.com", "https://google.com", "https://google.com"]
        length = len(title)
        return render_template('results.html', title=title, abstract=abstractR, length=length, link=link)
        flash('')
    return render_template('home.html', title='NLPRecommendations' , form=form)


@app.route("/about")
def about():
    return render_template('about.html', title='NLPRecommendations') #Would change to

#@app.route("/results")
#def results(titleab):
#    return titleab

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

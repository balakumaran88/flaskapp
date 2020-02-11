from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '542b544fc5bbc1d6e3a650403386376a'
posts = [
{
    'author': 'Corey schafer',
    'title': 'Blog post 1',
    'content': 'First Blog Content',
    'date_posted': 'April 20, 2019'
},
{
    'author': 'Jane Doe',
    'title': 'Blog post 2',
    'content': 'second Blog Content',
    'date_posted': 'May 20, 2019'
}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts, title="Home")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'pass':
            flash('you have been logged in' , 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessfull please check username/password', 'danger')
    return render_template('login.html', title="Register", form=form)


if __name__ == "__main__":
    app.run(debug=True)

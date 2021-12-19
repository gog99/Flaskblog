from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '37046177813704617781'

posts = [
    {
        'author': 'Jonny Senior',
        'title': 'Living with a small peen',
        'content': 'uhh',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created- welcome {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)




if __name__ == '__main__':
    app.run(debug=True)

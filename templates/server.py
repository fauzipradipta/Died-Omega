from flask import Flask, render_template, request
from forms import SignUpForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def home():
    return 'TEST'

@app.route('/test')
def home():
    return 'TESTING FLASK '

#@app.route('/signup', methods = ['GET', 'POST'])
#def signup():  
#    form = SignUpForm()
#    if form.is_submitted():
#        result = request.form
#        return render_template('base.html', result= result)
#    return render_template('signup.html', form=form)


@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request
from forms import SignUpForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

import csv
import urllib.request
import operator
header = ['Age', 'Underlying', 'Fever', 'ShortnessOfBreath', 'LossOfTaste', 'SoreThroat', 'RiskFactor', 'Submit']
data = []

url1 = 'https://raw.githubusercontent.com/gheniabla/datasets/master/companylist-1.csv'
response1 = urllib.request.urlopen(url1)
lines = [l.decode('utf-8') for l in response1.readlines()]
cr1 = csv.reader(lines)

line_count = 0
data=[]
for line in cr1:
	line_count += 1
	if line_count == 1:
		header = line
		continue
	data.append(line)

@app.route('/')
def home():
    return 'TEST'

@app.route('/test')
def home2():
    return 'TESTING FLASK '

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        data.append(result.copy())
        with open('test.csv', 'w') as csvDATA:
            writer = csv.writer(csvDATA)
            writer.writerow(header)
            for key in result.keys():
                csvDATA.write(result[key] + ' ')
        return render_template('user.html', result=result)
    return render_template('signup2.html', form=form)

if __name__ == '__main__':
    app.run()






#@app.route('/signup', methods = ['GET', 'POST'])
#def signup():  
#    form = SignUpForm()
#    if form.is_submitted():
#        result = request.form
#        return render_template('base.html', result= result)
#    return render_template('signup.html', form=form)
#if form.is_submitted():
#        result = request.form
#        return render_template('user.html', result=result)
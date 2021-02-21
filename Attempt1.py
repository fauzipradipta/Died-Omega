# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
app = Flask(__name__)

import csv
import urllib.request
import operator

#READ CSV FILE AND PUT CONTENTS INTO A LIST, ALL LINES WITHIN LIST

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

#PUT DATA INTO A CSV FILE

#with open('merged.csv', 'w') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerow(header)
#    for row in data:
#    	writer.writerow(row)

#CHECK IF AN ITEM IS IN THE CSV FILE

#checkValue = "GOOG"#sys.argv[1]
#Found = "false"
#csv_file = csv.reader(open('merged.csv', "r"), delimiter=",")
#for row in csv_file:
#    if checkValue in row:
#        Found = "true"
#        print(row)
#        continue
#if Found == "false":
#    print("Not Found")

with open('test.csv', 'a') as csvDATA:
        employee_writer = csv.writer(csvDATA, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


@app.route('/signup', methods = ['GET', 'POST'])
def signup():  
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('index.html', result= result)
    return render_template('signup.html', form=form)

#@app.route('/send_data', methods = ['POST'])
#def get_data_from_html():
#    pay = request.form['pay']
#    #print ("Pay is " + pay)
#    #return "Data sent. Please check your program log"
#    with open('test.csv', 'a') as csvDATA:
#        employee_writer = csv.writer(csvDATA, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debbug=True)

#csvfile.close()
#csvfile2.close()
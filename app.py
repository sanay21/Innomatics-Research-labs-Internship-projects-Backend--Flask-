#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex']
        return redirect(url_for('results', test_string=test_string, regex_pattern=regex_pattern))
    return render_template('index.html')

@app.route('/results')
def results():
    test_string = request.args.get('test_string', '')
    regex_pattern = request.args.get('regex_pattern', '')
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches, test_string=test_string, regex_pattern=regex_pattern)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return 'Valid Email'
    else:
        return 'Invalid Email'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

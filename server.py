from flask import Flask, render_template, request, redirect
import csv
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

app = Flask(__name__)

def send_email(data):
    input_email = data['email']
    input_subject = data['subject']
    input_message = data['message']
    
    html = Template(Path('mail_template.html').read_text())
    email = EmailMessage()
    email['from'] = 'CV website'
    email['to'] = 'gherrera98r@gmail.com'
    email['subject'] = 'NEW MESSAGE!!!'

    email.set_content(html.substitute(email=input_email, subject=input_subject, message=input_message), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('dummypython178@gmail.com', 'rius yoha arho bkzt')
        smtp.send_message(email)
        print('SENT!')


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def seatails(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            if data['email'] != '':
                write_to_csv(data)
                send_email(data)
                return redirect('thankyou.html')
            else:
                return redirect('contact_error.html')
        except:
            return "Couldn't save to database. Please verify your information and try again."
    else:
        try:
            a1 = request.args.get('email')
            a2 = request.args.get('subject')
            a3 = request.args.get('message')
            data = {'email': a1, 'subject': a2, 'message': a3}
            if a1 != '':
                write_to_csv(data)
                send_email(data)
                return redirect('thankyou.html')
            else:
                return redirect('contact_error.html')
        except:
            return "Couldn't save to database. Please verify your information and try again."


#Excersice on APIs 
'''@app.route('/suma', methods=['POST'])
def suma():
    if request.method == 'POST':
        try:
            data = request.json
            x = data.get('x')
            if not x:
                return "Dictionaty must contain key x"
            if type(x) != list:
                return "Input a list of numbers"
            length = len(x)
            if length == 0:
                return "List should contain at least one value"
            if type(x[0]) != int:
                return 'Elements of list must be integers'
            if length >= 5:
                return "Cannot sum so many values!"
            return f'{sum('hola')}'
        except Exception as e:
            return f'Error: {e}'
            return "Couldn't save to database. Please verify your information and try again."
    else:
        return "Not accepted"
'''

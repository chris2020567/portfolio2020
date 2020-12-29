from flask import Flask, render_template, url_for, request,redirect
import csv

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect(url_for('thankyou'))
    else:
        return 'something went wrong, Try again'

def write_to_file(data):
    with open('database.txt', mode='a')as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a')as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

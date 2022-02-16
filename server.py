from contextlib import nullcontext
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "secret key"


@app.route('/')
def root():
    if session['sc'] < 1:
        session['sc'] = 0
    else:
        session['sc'] = session['sc'] + 1
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    # print("Got Post Info")
    # Here we add two properties to session to store the name and email
    if session['sc'] < 1:
        session['sc'] = 0
    else:
        session['sc'] = session['sc'] + 1
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/#')
    # return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":
    app.run(debug=True)

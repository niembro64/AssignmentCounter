from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "Could be whatever I want. Really."

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/')



@app.route('/')
def root():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

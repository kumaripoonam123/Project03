from flask import Flask,request,jsonify,render_template
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.route("/",methods=['Post'])
def home():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    print(f"My email is {email} and password is {password}")
    return f"My email is {email} and password is {password}"


@app.route("/app")
def ship():
        return "Welcome to app"

@app.route("/static")
def add():
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

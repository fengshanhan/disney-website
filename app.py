from flask import Flask
from flask import render_template, redirect, url_for, request
from app.db.user_db import Visitor

app = Flask(__name__)

@app.route('/register.html',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        name=request.form.get('name')
        password=request.form.get('password')
        confirm=request.form.get('confirm')
        visitor=Visitor()
        if visitor.register(name,password,confirm) == 1:
            return redirect(url_for('login'))
        else:
            return "不能注册"
    else:
        return "wrong"

@app.route('/',methods=['GET','POST'])
@app.route('/login.html',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        visitor=Visitor()
        name=request.form.get('name')
        password=request.form.get('password')
        if visitor.login(name,password) == 1:
            return redirect(url_for('map'))
        else:
            return "不能登陆"

@app.route('/map.html',methods=['GET','POST'])
def map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)

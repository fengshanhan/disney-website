from flask import Flask, render_template, redirect, url_for, request
from app.db.user_base import VisitorCommand

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
@app.route('/login.html',methods=['GET', 'POST'])
def login():
    return render_template('login.html')



# 引入config.py文件
app.config.from_object('config')

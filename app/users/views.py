# coding=utf-8
from flask import render_template,request
from ..models import *
from .. import db
from . import users



@users.route("/login_info",methods=["GET","POST"])
def login_info():
    if request.method=="GET":
        return render_template("login.html")
    else:
        uname = request.form["username"]
        jobnum=request.form['jobnum']
        upwd = request.form['upwd']
        user=UserInfo.query.filter_by(user_name=uname,user_password=upwd,jobnum=jobnum
                                      ).first()
        if user:
            return "1"
        else:
            return "0"


@users.route('/register',methods=["GET","POST"])

def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        user=UserInfo()

        user_name =request.form['user_name']
        user_password = request.form['user_password']
        job_number = request.form['job_number']
        mobile_phone = request.form['mobile_phone']
        role = request.form['role']
        db.session.add(user)
        return render_template("login.html")


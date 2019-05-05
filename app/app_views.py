# coding=utf-8
from .models import *

from flask import render_template,request,Blueprint

app_view=Blueprint("app_views",__name__)

@app_view.route("/index")
def index_views():
    return render_template('index.html')

@app_view.route("/isms")
def isms():
    return render_template("isms.html")

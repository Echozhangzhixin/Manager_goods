# coding=utf-8
from flask import Blueprint
products=Blueprint("products",__name__)
from . import views
# coding=utf-8
from . import db

class Product(db.Model):
    __tablename__='products'
    id=db.Column(db.Integer,primary_key=True)
    product_id=db.Column(db.String(16),unique=True,nullable=False)
    product_name=db.Column(db.String(32),nullable=False)
    price=db.Column(db.Float,nullable=False)
    cost_price=db.Column(db.Float,nullable=False)
    status=db.Column(db.Integer,nullable=False)
    create_time=db.Column(db.DateTime,nullable=False)
    unit=db.Column(db.String(10),nullable=False)
    sid=db.Column(db.Integer,db.ForeignKey("prostock.id"))#外键ProStock的id
    iid=db.Column(db.Integer,db.ForeignKey("proinfo.id"))#外键ProInfo的id
    cid=db.Column(db.Integer,db.ForeignKey("category.id"))#外键categoryid
    out_in = db.relationship("Out_In", backref="products", lazy='dynamic')

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(32),nullable=False)

    create_time = db.Column(db.DateTime, nullable=False)
    product = db.relationship("Product", backref="category",lazy="dynamic")

class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(32),nullable=False)
    user_password=db.Column(db.String(32),nullable=False)
    job_number=db.Column(db.String(32),nullable=False)
    mobile_phone=db.Column(db.String(12),nullable=False)
    role=db.Column(db.Integer,nullable=False)
    out_in = db.relationship("Out_In", backref="userinfo", lazy='dynamic')
class Out_In(db.Model):
    __tablename__ = 'out_in'
    id = db.Column(db.Integer, primary_key=True)
    number=db.Column(db.Integer,nullable=False)
    time=db.Column(db.DateTime,nullable=False)
    status=db.Column(db.Integer,nullable=False)
    pid=db.Column(db.Integer,db.ForeignKey("products.id"))
    uid=db.Column(db.Integer,db.ForeignKey("userinfo.id"))

class ProInfo(db.Model):
    __tablename__ = 'proinfo'
    id=db.Column(db.Integer,primary_key=True)
    information=db.Column(db.String(64))

    # 增加外检约束和唯一约束
    product = db.relationship("Product", backref="proinfo",lazy="dynamic")

class ProStock(db.Model):
    __tablename__ = 'prostock'
    id = db.Column(db.Integer, primary_key=True)
    stock=db.Column(db.Integer,nullable=False)
    warning_stock = db.Column(db.Integer, nullable=False)

    status=db.Column(db.Integer, nullable=False)
    product=db.relationship("Product",backref="prostock",lazy="dynamic")


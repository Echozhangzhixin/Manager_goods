# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/CMS"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    # 配置自动提交,每次在执行完视图处理函数时将自动提交操作回数据库
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db.init_app(app)
    from .users import users as users_blueprint
    from .category import category as category_blueprint
    from .infomation import information as information_blueprint
    from .stocks import stocks as stocks_blueprint
    from .out_in import out_in as out_in_blueprint
    from .app_views import app_view as app_views_blueprint
    from .products import products as products_blueprint



    app.register_blueprint(users_blueprint)
    app.register_blueprint(category_blueprint)
    app.register_blueprint(information_blueprint)
    app.register_blueprint(stocks_blueprint)
    app.register_blueprint(out_in_blueprint)
    app.register_blueprint(app_views_blueprint)
    app.register_blueprint(products_blueprint)


    return app



from flask import Flask
from config import config
from extensions import db
from routes import auth_bp, main_bp


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # 初始化扩展
    db.init_app(app)
    
    # 注册蓝图
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    return app


app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)

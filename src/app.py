from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from controllers import book_controller, student_controller, loan_controller, auth_controller, notification_controller
    app.register_blueprint(book_controller.bp)
    app.register_blueprint(student_controller.bp)
    app.register_blueprint(loan_controller.bp)
    app.register_blueprint(auth_controller.bp)
    app.register_blueprint(notification_controller.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

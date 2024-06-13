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

    from controllers.book_controller import book_bp as book_controller_bp
    from views.book_view import book_bp as book_view_bp
    from controllers.student_controller import student_bp as student_controller_bp
    from views.student_view import student_bp as student_view_bp
    from controllers.loan_controller import loan_bp as loan_controller_bp
    from views.loan_view import loan_bp as loan_view_bp
    from controllers.auth_controller import auth_bp as auth_controller_bp
    from views.auth_view import auth_bp as auth_view_bp
    from controllers.notification_controller import notification_bp as notification_controller_bp
    from views.notification_view import notification_bp as notification_view_bp

    app.register_blueprint(book_controller_bp, name='book_controller_bp')
    app.register_blueprint(book_view_bp, name='book_view_bp')
    app.register_blueprint(student_controller_bp, name='student_controller_bp')
    app.register_blueprint(student_view_bp, name='student_view_bp')
    app.register_blueprint(loan_controller_bp, name='loan_controller_bp')
    app.register_blueprint(loan_view_bp, name='loan_view_bp')
    app.register_blueprint(auth_controller_bp, name='auth_controller_bp')
    app.register_blueprint(auth_view_bp, name='auth_view_bp')
    app.register_blueprint(notification_controller_bp, name='notification_controller_bp')
    app.register_blueprint(notification_view_bp, name='notification_view_bp')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

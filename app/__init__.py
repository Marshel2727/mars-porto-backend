import os
from flask import Flask
from .config import Config,db_connection
from  flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    CORS(app, origins=os.getenv('FRONTEND_URL', 'http://localhost:3000').split(','))

    app.config.from_object(Config)
    #fungsi ini di panggil untuk test koneksi data base
    db_connection()

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .models.project import Project
    from .models.user import User
    from .models.skill import Skill
    from .models.message import Message

    from .routes.project_routes import project_bp
    app.register_blueprint(project_bp)
    
    from .routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    from .routes.skill_routes import skill_bp
    app.register_blueprint(skill_bp)

    from .routes.message_routes import message_bp
    app.register_blueprint(message_bp)

    return app
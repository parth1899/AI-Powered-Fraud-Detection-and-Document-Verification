from flask import Flask
from routes.auth import auth_bp
from routes.document import document_bp
from routes.apply import apply_bp
# from routes.profile import profile_bp
from routes.dashboard import dashboard_bp
import os
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Register blueprints
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(document_bp, url_prefix='/docs')
app.register_blueprint(apply_bp, url_prefix='/apply')
# app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@app.route('/')
def home():
    return "Flask app is running with Neo4j!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
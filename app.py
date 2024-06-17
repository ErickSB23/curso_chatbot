from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Configura la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactiva las notificaciones de modificaciones
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def home():
    return "Hello, Flask with SQLAlchemy!"

if __name__ == '__main__':
    if 'create_db' in sys.argv:
        with app.app_context():
            db.create_all()
            print("Base de datos creada exitosamente.")
    else:
        app.run(debug=True)

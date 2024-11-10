from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from models import db  # Import your SQLAlchemy instance

# Create the Flask application instance
app = Flask(__name__)

# Configure the Flask app
app.secret_key = 'Moreno1234'  # Set a secret key for sessions
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Define routes
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    dbname = request.form['dbname']
    # Check if credentials are correct (try connecting to the database)
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@localhost/{dbname}'
        with app.app_context():
            db.create_all()  # Test connection by trying to create tables
        session['logged_in'] = True
        return redirect(url_for('main'))
    except Exception as e:
        flash('Login failed. Please check your credentials.')
        return redirect(url_for('home'))

@app.route('/main')
def main():
    if not session.get('logged_in'):
        return redirect(url_for('home'))
    # Main dashboard page
    return "Welcome to the main panel!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

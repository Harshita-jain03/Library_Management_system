import time
from flask import Flask, render_template, request, session, redirect, url_for, flash, send_file
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import io
from model import *
# from resources import api
from flask_login import current_user, login_required
from passlib.hash import sha256_crypt
from sqlalchemy import or_






app = Flask(__name__)
app.secret_key="abcd"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# db = SQLAlchemy()
# # db.init_app(app)

# app.app_context().push() 

db.init_app(app)
app.app_context().push()
with app.app_context():
    db.create_all()


# api.init_app(app)
from backend.librarian.login import *
from backend.librarian.section import *
from backend.librarian.book import *
from backend.librarian.stats import *
from backend.librarian import *
from backend.user.login import *
from backend.user.stats import *




@app.route('/')
def home():
    return render_template('index.html')





    

if __name__ == "__main__":
    app.run(debug=True)
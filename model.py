from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import UnmappedInstanceError
db=SQLAlchemy()


class User(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String(256),nullable=False)
    approval_requests = db.relationship('ApprovalRequest',backref='user',uselist=True)
    review = db.relationship('Review',backref='user',uselist=True)


class Librarian(db.Model):
    librarian_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)


class Section(db.Model):
    section_id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String, nullable=False)
    date_created = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    has_image = db.Column(db.Boolean, nullable=False)
    books = db.relationship('Book', backref='section')
    
class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.section_id'), nullable=False)
    title = db.Column(db.String, nullable=False,unique=True)
    author = db.Column(db.String, nullable=False)
    content_link = db.Column(db.String, nullable=False)
    has_image = db.Column(db.Boolean, nullable=False)
    added_date = db.Column(db.String,nullable=False)
    book_requests = db.relationship('ApprovalRequest', backref='book')
    book_review = db.relationship('Review', backref='book')
    
class ApprovalRequest(db.Model):
    approval_request_id = db.Column(db.Integer,primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    for_days = db.Column(db.Integer, nullable=False)
    request_time = db.Column(db.Integer, nullable=False)
    approved_time = db.Column(db.Integer,default=0)
    expiry_time = db.Column(db.Integer, nullable=False, default=0)
    last_update_time = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False) #status = 0 - requested,1-rejected, 2 - accepted , 3-revoked
    
    

class Review(db.Model):
    review_id = db.Column(db.Integer,primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user_name = db.Column(db.String,nullable=False)
    rating = db.Column(db.Integer,nullable=False,default=0)
    feedback = db.Column(db.String,nullable=False)


from dbin import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Belonging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(100), nullable=False)
    sorcers = db.relationship('Sorcer', backref='belonging', lazy=True)

class Sorcer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    belonging_id = db.Column(db.Integer, db.ForeignKey('belonging.id'), nullable=False)
    techniques = db.relationship('Technique', backref='sorcer', lazy=True)

class Technique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    sorcer_id = db.Column(db.Integer, db.ForeignKey('sorcer.id'), nullable=False)

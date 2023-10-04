from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates 

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'  # Change _tablename_ to __tablename__

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    update_at = db.Column(db.DateTime, onupdate=db.func.now())
    hero_powers = db.relationship('Heropower', back_populates='hero')

class Heropower(db.Model):
    __tablename__ = 'hero_powers'  # Change _tablename_ to __tablename__
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))  # Corrected the table name 'powers'
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))  # Corrected the table name 'powers'
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    update_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    @validates('strength')
    def strength_validation(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("strength must be Strong, Weak or Average")
        return strength

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)  # Define 'id' as the primary key
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    update_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_powers = db.relationship('Heropower', back_populates='power')

    @validates('description')
    def description_site(self, key, description):
        if len(description) < 20:
            raise ValueError('description must be atleast 20 characters')
        return description
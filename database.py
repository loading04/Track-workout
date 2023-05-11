from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pr-collection.db'
db.init_app(app)


class Pr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exo = db.Column(db.String(250), unique=True, nullable=False)
    kg = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()
    db.session.close()


def create_column(exo, kg):
    with app.app_context():
        new_pr = Pr(exo=exo, kg=kg)
        db.session.add(new_pr)
        db.session.commit()
        db.session.close()


def get_all():
    all_pr = None
    with app.app_context():
        all_pr = db.session.query(Pr).all()
        db.session.close()
    return all_pr


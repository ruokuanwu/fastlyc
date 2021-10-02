from extensions import db
import logging


class DogModel(db.Model):
    __tablename__ = 'dog'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

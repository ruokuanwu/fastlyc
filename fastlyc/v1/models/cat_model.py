from extensions import db
import logging


class CatModel(db.Model):
    __tablename__ = ''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

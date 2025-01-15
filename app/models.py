# Defines the table model in SQLAlchemy.
from app import db


class DataPoints(db.Model):
    __tablename__ = "data_points"

    id = db.Column(db.Integer, primary_key=True)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    species = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<DataPoints id={self.id}, width={self.width}, height={self.height}, species={self.species}>"

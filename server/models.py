from config import db
from sqlalchemy.sql import func

class Alchemist(db.Model):
    __tablename__ = 'alchemist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    experienceLevel = db.Column(db.Integer)
    recipe_number = db.Column(db.Integer)

    def __repr__(self):
        return f"Name: {self.name} Experience: {self.experienceLevel}"


class Recipe(db.Model):
    __tablename__ ='recipe'

    id = db.Column(db.Integer, primary_key=True)
    alchemistID = db.Column(db.Integer, db.ForeignKey("alchemist.id"))
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    description = db.Column(db.String)
    creation_date = db.Column(db.DateTime, server_default=func.now())
    modification_date = db.Column(db.DateTime, onupdate=func.now())

    def __repr__(self):
        return f"Name: {self.name} Ingredients: {self.ingredients} Description: {self.description} Creation Date: {self.creation_date} Modification Date: {self.modification_date}"
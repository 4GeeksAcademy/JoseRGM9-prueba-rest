from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorite', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "favorites": self.favorites            
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    favorites = db.relationship('Favorite', backref='planet')
    

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "climate": self.climate
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    height = db.Column(db.String(250))
    hair_color= db.Column(db.String(250))
    gender = db.Column(db.String(250))
    favorites = db.relationship('Favorite', backref='person')
    
    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "hair_color": self.hair_color,
            "gender": self.gender
        }    
    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    favorite_Person = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)
    favorite_Planet = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)

    def __repr__(self):
            return '<Favorite %r>' % self.id
    def serialize(self):
        return {
            "id_favorito": self.id,
            "user_id": self.user_id,
            "favoritePlanetId": self.favorite_Planet,
            "favoritePersonId": self.favorite_Person
        }    
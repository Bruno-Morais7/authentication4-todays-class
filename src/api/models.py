from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# this is our model & Class User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
    def save_user(self):
        #how to actually save the user in the db
        db.session.add(self)
        db.session.commit()

    def check_if_user_exists_and_get_it(email):
        user_found = User.query.filter_by(email=email)

        print(user_found)
        return user_found


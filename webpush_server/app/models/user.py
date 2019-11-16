from .core import db
from flask_security import (
    SQLAlchemyUserDatastore,
    UserMixin, RoleMixin)

user_role = db.Table(
    'user_role',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.Unicode(100), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean)

    roles = db.relationship('Role', secondary=user_role)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Unicode(100))
    users = db.relationship('User', secondary=user_role)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

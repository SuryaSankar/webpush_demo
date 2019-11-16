from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import (
    Security, SQLAlchemyUserDatastore, current_user,
    UserMixin, RoleMixin)


db = SQLAlchemy()
security = Security()


class PushSubscription(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    subscription_json = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

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


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"
app.config['SERVER_NAME'] = "localhost:5000"
app.config['SECRET_KEY'] = 'SomeString'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = 'SomePasswordSalt'
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

db.init_app(app)
security.init_app(app, user_datastore)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/push-subscriptions", methods=["POST"])
def create_push_subscription():
    subscription_data = request.get_json()
    subscription = PushSubscription.new(
        subscription_json=subscription_data.get('subscription_json'),
        user_id=current_user.get_id()
    )
    return subscription_data


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
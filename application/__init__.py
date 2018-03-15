# -*- coding: utf-8 -*-
''' Flask Application Factory

    Flask application using the factory pattern
'''
import os
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_security import Security
from flask_security import SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin
from flask_security import UserMixin
from flask_security import login_required
from flask_debugtoolbar import DebugToolbarExtension


def create_app():
    ''' create_app

        input:
            None

        output:
            app -- flask web application instance

        Setup web interface with Bootstrap framework
    '''
    app = Flask(__name__)

    # Configuration
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = \
        '*id4)fbbiyd*57oa18da3^t0$)m%ti#9ua+t^ihd4z9t*x%&sx'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/bmi.db'
    app.config['SECURITY_PASSWORD_SALT'] = os.urandom(32)
    app.config['SECURITY_REGISTERABLE'] = True
    app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
    app.config['SECURITY_POST_LOGIN_VIEW'] = '/bmi'
    app.config['SECURITY_POST_LOGOUT_VIEW'] = '/'
    app.config['SECURITY_POST_REGISTER_VIEW'] = '/bmi'
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Create database connection object
    db = SQLAlchemy(app)

    # Define models

    roles_users = db.Table(
        'roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

    class Role(db.Model, RoleMixin):
        __tablename__ = 'role'

        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(80), unique=True)
        description = db.Column(db.String(255))

        def __repr__(self):
            return '<Role> {}'.format(self.name)

    class User(db.Model, UserMixin):
        __tablename__ = 'user'

        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(255), unique=True)
        password = db.Column(db.String(255))
        active = db.Column(db.Boolean())
        confirmed_at = db.Column(db.DateTime())
        roles = db.relationship(
            'Role',
            secondary=roles_users,
            backref=db.backref('users', lazy='dynamic'))

        def __repr__(self):
            return '<User> {} {}'.format(self.mail, self.email)

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    @app.before_first_request
    def before_first_request():
        # Create any database tables that don't exist yet.
        db.create_all()

    # Initialize bootstrap
    Bootstrap(app)

    # Debug = True to enable the toolbar
    toolbar = DebugToolbarExtension(app)

    # Views

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/bmi', methods=['GET', 'POST'])
    @login_required
    def bmi():
        return render_template('bmi.html')

    return app

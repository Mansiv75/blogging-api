from flask import Flask
from routes.blog import blog_routes  # Make sure to import the blog_routes
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from flask_migrate import Migrate # type: ignore
from models import BlogPost
from extensions import db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()  # Create the database tables if they don't exist yet.
    

migrate=Migrate(app, db)
app.register_blueprint(blog_routes)

@app.route('/')
def hello():
    return "Hello, Blogging API!"

if __name__ == "__main__":
    app.run(debug=True)

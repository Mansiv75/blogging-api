from flask import Flask
from routes.blog import blog_routes  # Make sure to import the blog_routes

app = Flask(__name__)

app.register_blueprint(blog_routes)

@app.route('/')
def hello():
    return "Hello, Blogging API!"

if __name__ == "__main__":
    app.run(debug=True)

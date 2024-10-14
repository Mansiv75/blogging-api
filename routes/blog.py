from flask import Blueprint, request, jsonify

blog_routes = Blueprint('blog', __name__)

blog_post=[]
post_id_counter = 1

@blog_routes.route('/posts', methods=['POST'])
def create_post():
    global post_id_counter

    data = request.get_json()

    

@blog_routes.route('/posts')
def get_posts():
    return "List of blog posts"

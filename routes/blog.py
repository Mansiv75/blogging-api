from flask import Blueprint, request, jsonify

blog_routes = Blueprint('blog', __name__)

blog_posts=[]
post_id_counter = 1

@blog_routes.route('/posts', methods=['POST'])
def create_post():
    global post_id_counter

    data = request.get_json()

    if not data or 'title' not in data or 'content' not in data or 'category' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_post ={
        'id': post_id_counter,
        'title': data['title'],
        'content': data['content'],
        'category': data['category'],
        'tags': data.get('tags',[]),
        'createdAt': '2021-09-01T12:00:00Z',
        'updatedAt': '2021-09-01T12:00:00Z'

    }
    blog_posts.append(new_post)
    post_id_counter += 1

    return jsonify(new_post), 201



@blog_routes.route('/posts')
def get_posts():
    return jsonify(blog_posts)

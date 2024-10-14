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

@blog_routes.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(blog_posts)

@blog_routes.route('/posts/<int:post_id>', methods=['PUT'])
def update_post():
    data =request.get_json()
    post=next((p for p in blog_posts if p['id']==post_id), None)

    if post is None:
        return jsonify({"error": "Post not found"}), 404
    if not data or 'title' not in data or 'content' not in data or 'category' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    post['title'] = data['title']
    post['content'] = data['content']
    post['category'] = data['category']
    post['tags'] = data.get('tags', post['tags'])
    post['updatedAt'] = '2021-09-01T12:00:00Z'

    return jsonify(post), 200

@blog_routes.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global blog_posts

    post= next((p for p in blog_posts if p['id']== post_id), None)

    if post is None:
        return jsonify({"error": "Post not found"}), 404
    blog_posts=[p for p in blog_posts if p['id']!=post_id]

    return jsonify({"message": "Post deleted"}), 204
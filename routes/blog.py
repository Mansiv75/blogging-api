from operator import or_
from flask import Blueprint, request, jsonify
from datetime import datetime
from models import BlogPost
from extensions import db
blog_routes = Blueprint('blog', __name__)

@blog_routes.route('/posts', methods=['POST'])
def create_post():
    
    data = request.get_json()

    if not data or 'title' not in data or 'content' not in data or 'category' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    current_time = datetime.now()
    
    
    new_post =BlogPost(
        title=data.get('title'),
        content=data.get('content'),
        category=data.get('category'),
        tags=data.get('tags', []),
        createdAt=current_time,
        updatedAt=current_time,
    )
    db.session.add(new_post)
    db.session.commit()

    response={
        'id': new_post.id,
        'title': new_post.title,
        'content': new_post.content,
        'category': new_post.category,
        'tags': new_post.tags,
        'createdAt': new_post.createdAt.isoformat()+'Z',
        'updatedAt': new_post.updatedAt.isoformat()+'Z'
    }

    return jsonify(response), 201

@blog_routes.route('/posts', methods=['GET'])
def get_posts():
    term = request.args.get('term','')

    if term:
        filtered_posts = BlogPost.query.filter(
            or_(BlogPost.title.contains(term) ,
            BlogPost.content.contains(term) ,
            BlogPost.category.contains(term))
        ).all()
    else:
        filtered_posts =BlogPost.query.all()    
        
    response = [{
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'category': post.category,
        'tags': post.tags,
        'createdAt': post.createdAt.isoformat() + "Z",
        'updatedAt': post.updatedAt.isoformat() + "Z"
    } for post in filtered_posts]

    return jsonify(response), 200

@blog_routes.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data =request.get_json()
    post=BlogPost.query.get(post_id)

    if post is None:
        return jsonify({"error": "Post not found"}), 404
    if not data or 'title' not in data or 'content' not in data or 'category' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    post.title = data['title']
    post.content = data['content']
    post.category = data['category']
    post.tags = ', '.join(data.get('tags', post.tags))
    post.updatedAt = datetime.now()

    db.session.commit()

    response ={
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'category': post.category,
        'tags': post.tags,
        'createdAt': post.createdAt.isoformat()+'Z',
        'updatedAt': post.updatedAt.isoformat()+'Z'
    }

    return jsonify(response), 200

@blog_routes.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post= BlogPost.query.get(post_id)

    if post is None:
        return jsonify({"error": "Post not found"}), 404
    db.session.delete(post)
    db.session.commit()

    return jsonify({"message": "Post deleted"}), 204

@blog_routes.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = BlogPost.query.get(post_id)

    if post is None:
        return jsonify({"error": "Post not found"}), 404
    
    response={
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'category': post.category,
        'tags': post.tags,
        'createdAt': post.createdAt.isoformat()+'Z',
        'updatedAt': post.updatedAt.isoformat()+'Z'
    }
    return jsonify(response), 200
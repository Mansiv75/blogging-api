from operator import or_
from flask import Blueprint, request, jsonify, Flask
from datetime import datetime
from models import BlogPost
from extensions import db
from flasgger import Swagger # type: ignore
blog_routes = Blueprint('blog', __name__)

@blog_routes.route('/posts', methods=['POST'])

def create_post():
    """Create a new blog post.
    ---
    tags:
      - Blog
    parameters:
      - name: post
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: 'Sample Blog Post'
            content:
              type: string
              example: 'This is the content of the blog post.'
            category:
              type: string
              example: 'Tech'
            tags:
              type: array
              items:
                type: string
              example: ['Python', 'Flask']
    responses:
      201:
        description: Blog post created
        schema:
          id: BlogPost
          properties:
            id:
              type: integer
              example: 1
            title:
              type: string
              example: 'Sample Blog Post'
            content:
              type: string
              example: 'This is the content of the blog post.'
            category:
              type: string
              example: 'Tech'
            tags:
              type: array
              items:
                type: string
              example: ['Python', 'Flask']
            createdAt:
              type: string
              example: '2024-10-14T12:00:00Z'
            updatedAt:
              type: string
              example: '2024-10-14T12:00:00Z'
      400:
        description: Missing required fields
    """
    

    
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
    """Get all blog posts or filter by search term.
    ---
    tags:
      - Blog
    parameters:
      - name: term
        in: query
        type: string
        required: false
        description: The search term to filter posts by title, content, or category
    responses:
      200:
        description: A list of blog posts
        schema:
          type: array
          items:
            $ref: '#/definitions/BlogPost'
    """
    

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
    """Update an existing blog post by ID.
    ---
    tags:
      - Blog
    parameters:
      - name: post_id
        in: path
        type: integer
        required: true
        description: The ID of the blog post to update
      - name: post
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: 'Updated Blog Post'
            content:
              type: string
              example: 'This is the updated content of the blog post.'
            category:
              type: string
              example: 'Tech'
            tags:
              type: array
              items:
                type: string
              example: ['Python', 'Flask']
    responses:
      200:
        description: Blog post updated
        schema:
          $ref: '#/definitions/BlogPost'
      404:
        description: Post not found
      400:
        description: Missing required fields
    """
    

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
    """Delete a blog post by ID.
    ---
    tags:
      - Blog
    parameters:
      - name: post_id
        in: path
        type: integer
        required: true
        description: The ID of the blog post to delete
    responses:
      204:
        description: Post deleted
      404:
        description: Post not found
    """
    
    post= BlogPost.query.get(post_id)

    if post is None:
        return jsonify({"error": "Post not found"}), 404
    db.session.delete(post)
    db.session.commit()

    return jsonify({"message": "Post deleted"}), 204

@blog_routes.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """Get a single blog post by ID.
    ---
    tags:
      - Blog
    parameters:
      - name: post_id
        in: path
        type: integer
        required: true
        description: The ID of the blog post to retrieve
    responses:
      200:
        description: The blog post
        schema:
          $ref: '#/definitions/BlogPost'
      404:
        description: Post not found
    """
    

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

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/swagger.json")
def swagger_spec():
    return jsonify(swagger.get_swagger())


swagger.definition('BlogPost', {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'integer'
        },
        'title': {
            'type': 'string'
        },
        'content': {
            'type': 'string'
        },
        'category': {
            'type': 'string'
        },
        'tags': {
            'type': 'array',
            'items': {
                'type': 'string'
            }
        },
        'createdAt': {
            'type': 'string',
            'format': 'date-time'
        },
        'updatedAt': {
            'type': 'string',
            'format': 'date-time'
        }
    }
})


from extensions import db
from datetime import datetime

class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(255), nullable=False)
    content=db.Column(db.Text, nullable=False)
    category=db.Column(db.String(100), nullable=False)
    tags=db.Column(db.String, default=[])
    createdAt=db.Column(db.DateTime, default =datetime.utcnow)
    updatedAt=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, content, category, tags, createdAt, updatedAt):
        self.title=title
        self.content=content
        self.category=category
        self.tags=','.join(tags)
        self.createdAt=createdAt
        self.updatedAt=updatedAt
    def get_tags(self):
        return self.tags.split(',') if self.tags else []
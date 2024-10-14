import unittest
from app import app, db
from models import BlogPost

class BlogPostAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_post(self):
        response = self.client.post('/posts', json={
            'title': 'Test Blog Post',
            'content': 'This is a test blog post content.',
            'category': 'Testing',
            'tags': ['Test']
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Blog Post', response.get_data(as_text=True))

    def test_get_posts(self):
        self.client.post('/posts', json={
            'title': 'Test Blog Post',
            'content': 'This is a test blog post content.',
            'category': 'Testing',
            'tags': ['Test']
        })
        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_get_post(self):
        post_response = self.client.post('/posts', json={
            'title': 'Test Blog Post',
            'content': 'This is a test blog post content.',
            'category': 'Testing',
            'tags': ['Test']
        })
        post_id = post_response.get_json()['id']
        response = self.client.get(f'/posts/{post_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Blog Post', response.get_data(as_text=True))

    def test_update_post(self):
        post_response = self.client.post('/posts', json={
            'title': 'Initial Title',
            'content': 'This is the content of the blog post.',
            'category': 'Testing',
            'tags': ['Test']
        })
        post_id = post_response.get_json()['id']
        
        update_response = self.client.put(f'/posts/{post_id}', json={
            'title': 'Updated Title',
            'content': 'This is the updated content of the blog post.',
            'category': 'Testing',
            'tags': ['Updated']
        })
        self.assertEqual(update_response.status_code, 200)
        self.assertIn('Updated Title', update_response.get_data(as_text=True))
        
        get_response = self.client.get(f'/posts/{post_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertIn('Updated Title', get_response.get_data(as_text=True))

    def test_delete_post(self):
        post_response = self.client.post('/posts', json={
            'title': 'Test Blog Post',
            'content': 'This is a test blog post content.',
            'category': 'Testing',
            'tags': ['Test']
        })
        post_id = post_response.get_json()['id']
        response = self.client.delete(f'/posts/{post_id}')
        self.assertEqual(response.status_code, 204)

        response = self.client.get(f'/posts/{post_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

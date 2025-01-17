# Blogging API

A blogging platform API built with Flask and SQLAlchemy. This API allows users to create, read, update, and delete blog posts, with support for categories and tags.

---

## Features

- **Create Blog Posts**: Add new blog posts with titles, content, categories, and tags.
- **Retrieve Blog Posts**: Get a list of all blog posts or filter them by search terms.
- **Retrieve a Single Blog Post**: Fetch detailed information about a specific post by its ID.
- **Update Blog Posts**: Modify existing blog posts.
- **Delete Blog Posts**: Remove blog posts from the database.
- **API Documentation**: Swagger-powered API documentation for ease of use.

---

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) system for Python.
- **Flasgger**: A Flask extension to create Swagger UI documentation.
- **SQLite**: A lightweight database for development (can be replaced with PostgreSQL/MySQL in production).

---

## API Endpoints

### Blog Post Endpoints

1. **Create a Blog Post**  
   - `POST /posts`

2. **Retrieve All Blog Posts**  
   - `GET /posts`

3. **Retrieve a Single Blog Post**  
   - `GET /posts/<post_id>`

4. **Update a Blog Post**  
   - `PUT /posts/<post_id>`

5. **Delete a Blog Post**  
   - `DELETE /posts/<post_id>`

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd blog-platform-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database (optional):
   ```bash
   python -m app.setup_db
   ```

---

## Running the API

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Access the API locally at [http://localhost:5000](http://localhost:5000).

3. Interactive API documentation is available at [http://localhost:5000/apidocs](http://localhost:5000/apidocs).

---
## Live API
The API is live on Render and can be accessed here: API Live Link https://blogging-api-yo5p.onrender.com

---

## API Documentation
Swagger UI: Available at http://localhost:5000/apidocs for interactive API testing.

Swagger JSON: Accessible at http://localhost:5000/apidocs/swagger.json.

---

## Testing

Run unit tests with:
```bash
python -m unittest test_blog.py
```

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any improvements.

---

## About

A simple blogging API built for educational purposes. Future improvements include extending the API to support user authentication and additional features.

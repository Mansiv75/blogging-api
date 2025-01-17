# Blogging API

A blogging platform API built with Flask and SQLAlchemy. This API allows users to create, read, update, and delete blog posts, with support for categories and tags.

## Features

- **Create Blog Posts**: Add new blog posts with titles, content, categories, and tags.
- **Retrieve Blog Posts**: Get a list of all blog posts or filter them by search terms.
- **Update Blog Posts**: Modify existing blog posts.
- **Delete Blog Posts**: Remove blog posts from the database.
- **API Documentation**: API documentation using Swagger.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) system for Python.
- **Flasgger**: A Flask extension to create Swagger UI documentation.
- **SQLite**: A lightweight database for development (can be replaced with other databases like PostgreSQL or MySQL for production).

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd blog-platform-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Set up the database (optional, depending on your setup):

- Initialize your database if necessary.

## Running the API

To start the Flask application, run:

```bash
python app.py
```

The API will be accessible at [http://localhost:5000](http://localhost:5000).

## Live API

The API is live on Render and can be accessed here:
**[API Live Link](https://blogging-api-yo5p.onrender.com)**  

## API Documentation

- **Swagger UI**: Available at [http://localhost:5000/apidocs](http://localhost:5000/apidocs) for interactive API testing.
- **Swagger JSON**: Accessible at [http://localhost:5000/apidocs/swagger.json](http://localhost:5000/apidocs/swagger.json).

## Testing

To run the unit tests, use:

```bash
python -m unittest test_blog.py
```

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any improvements.

## Acknowledgments

- Flask for the web framework.
- SQLAlchemy for the ORM.
- Flasgger for the API documentation.

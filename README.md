# Zenspace API Readme

## Overview

This readme provides a brief guide on setting up a project using Strawberry and FastAPI, combining the power of GraphQL with the simplicity and speed of FastAPI for building modern web applications.

### Technologies Used

- **Strawberry**: A GraphQL library for Python that aims to provide a simple, type-safe, and productive development experience.
  
- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.7 or higher
- virtualenv (optional, but recommended for virtual environment management)

## Project Setup

1. **Install Dependencies:**

```bash
virtualenv venv 
```

```bash
source venv/bin/activate 
```

```bash
pip install -r requirements.txt 
```

**Run the Application:**

   ```bash
   uvicorn main:app --reload
   ```

   Open your browser and go to [http://localhost:8000](http://localhost:8000) to see the FastAPI root endpoint. The GraphQL playground is available at [http://localhost:8000/graphql](http://localhost:8000/graphql).



## Resources

- [Strawberry Documentation](https://strawberry.rocks/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

Feel free to customize and extend this setup based on your project requirements. Happy coding!
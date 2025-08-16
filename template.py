import os

# --- Configuration ---
# The root directory for the new project.
# Use "." to create it in the current directory.
ROOT_DIR = "."

# --- File Content Definitions ---

BACKEND_REQUIREMENTS = """\
fastapi==0.111.0
uvicorn[standard]==0.29.0
pydantic==2.7.1
psycopg2-binary==2.9.9
sqlalchemy==2.0.30
requests==2.31.0
python-dotenv==1.0.1
"""

ML_SERVICE_REQUIREMENTS = """\
fastapi==0.111.0
uvicorn[standard]==0.29.0
pydantic==2.7.1
ultralytics==8.2.2
torch==2.3.0
torchvision==0.18.0
opencv-python-headless==4.9.0.80
python-multipart==0.0.9
mlflow==2.13.1
"""

GITIGNORE_CONTENT = """\
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Data files
data/

# IDEs & OS files
.idea/
.vscode/
.DS_Store
"""

DOCKER_COMPOSE_CONTENT = """\
version: '3.8'

services:
  db:
    image: postgres:15
    container_name: snapcal_db
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=snapcal_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data/

  backend:
    build: ./services/backend
    container_name: snapcal_backend
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/snapcal_db
      - ML_SERVICE_URL=http://ml_service:8001

  ml_service:
    build: ./services/ml_service
    container_name: snapcal_ml_service
    ports:
      - "8001:8001"

volumes:
  postgres_data:
"""

README_CONTENT = """\
# 🚀 SnapCal Project

SnapCal is an AI-powered mobile application that estimates calories and nutrition from a single photograph of a meal, with a primary focus on diverse Indonesian cuisine.

## ✨ Features (MVP)
- Image upload (camera or gallery)
- AI-powered detection of 15+ Indonesian dishes
- Instant display of key nutritional info (Calories, Protein, Carbs, Fat)

## 🛠️ Tech Stack
- **Backend:** FastAPI, PostgreSQL
- **Machine Learning:** PyTorch, YOLOv8, MLflow
- **DevOps:** Docker, VS Code Dev Containers, GitHub Actions
- **Project Management:** Notion

## 🚀 Getting Started

This project is configured to run in a standardized development environment using VS Code Dev Containers.

### Prerequisites
1.  **Docker Desktop:** [Install Docker](https://www.docker.com/products/docker-desktop/)
2.  **VS Code:** [Install VS Code](https://code.visualstudio.com/)
3.  **VS Code Dev Containers Extension:** [Install Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Running the Project
1.  Clone this repository.
2.  Open the cloned folder in VS Code.
3.  A pop-up will appear: "Reopen in Container?". Click it.
4.  VS Code will build the Docker containers and launch your development environment.
5.  Once loaded, open a new terminal in VS Code and run `docker-compose up --build` to start all services.
"""


# Define the complete folder and file structure.
STRUCTURE = {
    ".devcontainer/": ["devcontainer.json", "Dockerfile"],
    ".github/": {
        "workflows/": ["ci.yml", "cd.yml"]
    },
    "data/": {
        "raw/": [".gitkeep"],
        "processed/": [".gitkeep"]
    },
    "docs/": ["project_brief.md", "system_design.md"],
    "notebooks/": ["01_data_exploration.ipynb", "02_model_training_and_evaluation.ipynb"],
    "services/": {
        "backend/": {
            "app/": {
                "api/": ["__init__.py"],
                "core/": ["__init__.py"],
                "db/": ["__init__.py"],
                "__init__.py": "",
                "main.py": "",
            },
            "tests/": ["__init__.py"],
            "Dockerfile": "",
            "requirements.txt": BACKEND_REQUIREMENTS,
        },
        "ml_service/": {
            "app/": {
                "models/": [".gitkeep"],
                "core/": ["__init__.py"],
                "__init__.py": "",
                "main.py": "",
            },
            "tests/": ["__init__.py"],
            "Dockerfile": "",
            "requirements.txt": ML_SERVICE_REQUIREMENTS,
        },
    },
    ".gitignore": GITIGNORE_CONTENT,
    "docker-compose.yml": DOCKER_COMPOSE_CONTENT,
    "LICENSE": "",
    "README.md": README_CONTENT,
}

def create_project_structure(base_path, structure_dict):
    """
    Recursively creates a directory and file structure.

    Args:
        base_path (str): The current path to create items in.
        structure_dict (dict): A dictionary representing the folder/file structure.
    """
    for name, content in structure_dict.items():
        current_path = os.path.join(base_path, name)

        if name.endswith('/'):
            # It's a directory
            dir_path = current_path.rstrip('/')
            try:
                os.makedirs(dir_path, exist_ok=True)
                print(f"Created directory: {dir_path}")
                if isinstance(content, (dict, list)):
                    create_project_structure(dir_path, dict.fromkeys(content, "") if isinstance(content, list) else content)
            except OSError as e:
                print(f"Error creating directory {dir_path}: {e}")
        else:
            # It's a file
            try:
                with open(current_path, 'w') as f:
                    if content:
                        f.write(content)
                print(f"Created file:      {current_path}")
            except IOError as e:
                print(f"Error creating file {current_path}: {e}")

def main():
    """Main function to run the script."""
    print(f"Setting up project structure in the current directory ('./')...")
    base_path = ROOT_DIR
    create_project_structure(base_path, STRUCTURE)
    print("\nProject structure created successfully! 🎉")
    print("Next steps:")
    print("1. Initialize your Git repository: git init")
    print("2. Start populating the placeholder files and Dockerfiles.")

if __name__ == "__main__":
    main()

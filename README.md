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
# Dockerized Flask To-Do App with PostgreSQL, Redis, and Nginx (Upgraded Version)

This is an upgraded version of the original Flask To-Do app.
It now includes:

- Nginx reverse proxy
- Redis caching
- Static frontend
- Full multi-container setup using Docker Compose

## Project Structure

- backend/
  - app.py
  - requirements.txt
  - Dockerfile
  - config.py
- db/
  - init.sql
- nginx/
  - nginx.conf
- frontend/
  - index.html
  - styles.css
  - main.js
- docker-compose.yml
- README.md
- .env

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Kedlyman/docker-flask-postgres-todo-upgraded.git
   cd docker-flask-postgres-todo-upgraded

2. Build and start the containers(in detached mode so you can try it out immediately):

  docker compose up -d --build

3. Access the Flask app:

  Open you browser and go to:

  http://localhost/
  
  or, if running on remote server:
  
  http://your-server-ip/

## API Endpoints

- `GET /tasks` - List all tasks
- `POST /tasks` - Add a new task (send JSON with "task" field)
- `DELETE /tasks/<id>` - Delete a task by ID

### Add a New Task

curl -X POST http://your-server-ip/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"task":"your-task"}'

### Get All Tasks

curl http://your-server-ip/api/tasks

### Delete a Task

curl -X DELETE http://your-server-ip/api/tasks/1

### Stop and clean everything up

docker compose down -v

## Technologies Used

- Python 3.13
- Flask
- PostgreSQL 17
- Redis (for caching)
- Docker
- Docker Compose
- Nginx (reverse proxy and static frontend serving)

## Notes

- The backend, database, and caching service are fully containerized and orchestrated using Docker Compose.
- Nginx is used as a reverse proxy to route API calls and serve the static frontend.
- Redis caching is used to speed up fetching the list of tasks.
- The database is automatically initialized with a tasks table using init.sql.
- Data is stored persistently in a Docker volume named db_data.
- Environment variables are managed through a .env file.
- The app is running in development mode

# FastAPI test

cd /path/to/the/project
git pull
docker build -t my-fastapi-app .
docker run --detach -p 80:8000 my-fastapi-app

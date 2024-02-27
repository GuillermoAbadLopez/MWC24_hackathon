# Requirements

docker

docker-compose

Python version 3.9 or higher

+

pip install -r requirements.txt

# Start backend

# db
docker-compose up -d

# services
uvicorn server:app --reload
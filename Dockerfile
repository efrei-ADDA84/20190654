FROM python:3.10
ENV API_KEY="14c52ccb6470e53bd70d27f06e1b5841"
WORKDIR /app

COPY . .
CMD ["python", "./main.py"]


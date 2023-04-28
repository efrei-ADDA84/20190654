FROM python:3.10
WORKDIR /app
RUN pip install requests

COPY . .
CMD ["python", "./main.py"]


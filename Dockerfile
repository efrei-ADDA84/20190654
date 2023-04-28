FROM python:3.10
WORKDIR /app
RUN pip install requests
RUN pip install uvicorn
RUN pip install fastAPI
COPY main.py .
CMD ["uvicorn", "main:app","--host","0.0.0.0","--port","8081"]


# Dockerfile
FROM python:3.9
WORKDIR /node
COPY . .
RUN pip install fastapi uvicorn
CMD ["python", "api_server/main.py"]

FROM python:3.9-slim

WORKDIR /app

COPY ./api_server/utils.py .

CMD ["python", "utils.py"]

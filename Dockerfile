# Dockerfile, Image, Container
FROM python:3.14.5-slim

ADD / .

RUN pip install discord python-dotenv qbittorrent-api

CMD ["python", "./main.py"]

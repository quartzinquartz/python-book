# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /flask-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

# Build image: docker build -t flask-app-image .
# Run the app: docker run -d --name flask-app -p 5000:5000 flask-app-image

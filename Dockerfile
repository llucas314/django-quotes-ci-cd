FROM python:3.13.5-slim

#  Keeps Python from writing the .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 
#  Keeps Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
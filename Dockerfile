FROM python:3.6.1-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV FLASK_APP=backend.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
FROM python:3.6.12-alpine

WORKDIR /app

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app

ENTRYPOINT ["./gunicorn.sh"]
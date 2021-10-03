FROM python:3.6.1-alpine

WORKDIR /backend
ADD . /backend

RUN pip install -r requirements.txt

CMD ["python","app.py"]
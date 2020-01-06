FROM python:3.8.1

COPY . /job
WORKDIR /job

RUN apt-get update

RUN pip install -r requirements.txt

CMD python app.py

EXPOSE 8081
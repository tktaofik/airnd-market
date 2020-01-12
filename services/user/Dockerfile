FROM python:3.8.1

COPY . /user

WORKDIR /user

RUN apt-get update && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash && \
    apt-get install nodejs && \
    npm i -g nodemon && \
    pip install -r requirements.txt

CMD python main.py

EXPOSE 8082
FROM python:3.10

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2-binary

WORKDIR /app
COPY script.py script.py

ENTRYPOINT [ "python", "script.py" ]

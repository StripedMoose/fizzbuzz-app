FROM  python:2.7-slim

MAINTAINER Chris Smith <chris@geosmith.com>

RUN pip install flask

ADD src/  .

VOLUME [ "./logs"]

CMD ["python","fizzbuzz.py"]

EXPOSE 5000

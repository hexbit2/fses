FROM python:3.9-alpine

COPY requirements.txt /

#RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip3 install -r /requirements.txt
#RUN apk del gcc musl-dev .build-deps

COPY . /app
WORKDIR /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
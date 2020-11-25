FROM python:3.10-rc-slim-buster

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY server.py /app/

CMD ["uvicorn",                \
       "--host", "0.0.0.0",    \
       "--port", "8080",       \
       "server:app"]

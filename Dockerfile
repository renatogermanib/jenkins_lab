FROM python:3.8-slim-buster

WORKDIR /src

COPY ./src/requerimientos.txt .

RUN pip install --no-cache-dir -r requerimientos.txt

COPY ./src .

ENV FLASK_APP=main.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

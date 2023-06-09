FROM python:3.11.3

WORKDIR /usr/src/

COPY requirements.txt requirements.dev.txt /usr/src/

RUN pip install --no-cache-dir -r requirements.txt -r requirements.dev.txt

ENTRYPOINT PYTHONPATH=/usr/src/:/usr/src/tests python -m unittest discover -v
FROM python:3

WORKDIR /App

COPY requirements.txt /App
RUN pip install --no-cache-dir -r requirements.txt

COPY . /App

CMD python src/manage.py runserver 0:8000
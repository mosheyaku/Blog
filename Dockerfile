FROM python:3.10.5

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 7000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:7000"]

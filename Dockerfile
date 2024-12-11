FROM python:3.11.1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src /app/src

EXPOSE 5000

CMD ["python", "src/app.py"]
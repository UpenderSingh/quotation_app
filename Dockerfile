FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "manage.py",  "runserver", "0.0.0.0:8000"]

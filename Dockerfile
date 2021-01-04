FROM python:3.8-alpine
WORKDIR /usr/scr/app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/scr/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
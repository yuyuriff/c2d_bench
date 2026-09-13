FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 60 -r requirements.txt

COPY . /app/evaluator/

CMD ["python", "-m", "evaluator.main"]

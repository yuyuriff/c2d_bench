FROM python:3.12-slim

WORKDIR /evaluator

COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 60 -r requirements.txt
COPY main.py .
COPY evaluate.py .

CMD ["python", "main.py"]

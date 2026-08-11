FROM python:3.12-slim

WORKDIR /runner

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 60 -r requirements.txt
COPY main.py .

CMD ["python", "main.py"]

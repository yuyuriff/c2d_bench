FROM python:3.12-slim

WORKDIR /agent

COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 60 -r requirements.txt
COPY main.py .
COPY config.py .
COPY agent.py .
COPY tools.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "port", "8000"]
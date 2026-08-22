FROM python:3.11-slim

WORKDIR /mcp

COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 60 -r requirements.txt

COPY main.py .

EXPOSE 9000

CMD ["python", "main.py"]

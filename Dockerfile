FROM python:3.9.7-slim
COPY ./app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y curl
CMD ["python3", "app.py"]

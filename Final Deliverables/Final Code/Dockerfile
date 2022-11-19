FROM python:3.6-slim
WORKDIR /app
ADD . /app
RUN apt update && apt install make build-essential libxml2 -y
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
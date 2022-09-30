FROM python:3
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /app/
RUN chmod +x /app/entrypoint.sh

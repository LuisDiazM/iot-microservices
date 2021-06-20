# Use Python37
FROM python:3.8.10-slim-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE ${PORT}
# Use gunicorn as the entrypoint
CMD exec gunicorn --bind :${PORT} main:app_run --workers 1 --threads 1 --timeout 60
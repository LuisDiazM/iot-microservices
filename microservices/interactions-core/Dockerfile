# Use Python37
FROM python:3.7.10-alpine3.13
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# ENV PORT 5000
# ENV MONGO_URL=mongodb://root:kldfjwqrt867r@localhost:27017/iot-devices?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false

# Use gunicorn as the entrypoint
CMD exec gunicorn --bind :${PORT} main:app_run --workers 1 --threads 1 --timeout 60
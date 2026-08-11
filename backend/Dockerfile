FROM python:3.14.5-slim

RUN useradd -r -u 10001 -m -s /bin/bash appuser

WORKDIR /app

COPY app.py .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

CMD ["python3", "app.py"]
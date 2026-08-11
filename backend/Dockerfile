FROM python:3.14.5-slim

WORKDIR /app

COPY app.py .

USER appuser

EXPOSE 8080

CMD ["python3", "app.py"]
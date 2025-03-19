FROM python:3.10.12
WORKDIR /app
ADD backend.tar.gz /app
ADD env.tar.gz /app
WORKDIR /app/backend
RUN pip install  -r requirements.txt
COPY update_db.sh /app/backend
RUN chmod +x update_db.sh
ENV PYTHONPATH=/app/backend
EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


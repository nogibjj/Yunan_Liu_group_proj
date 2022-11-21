FROM python:3.9.12-slim

WORKDIR /app

# 
COPY gcpconn.py main.py requirements.txt fresh-span-361719-e4e6a5688c1e.json /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt
# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

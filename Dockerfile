FROM python:3.8

WORKDIR /app

COPY gcpconn.py main.py requirements.txt fresh-span-361719-e4e6a5688c1e.json /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# EXPOSE 8080

# CMD [ "main.py" ]

# ENTRYPOINT [ "python" ]
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]

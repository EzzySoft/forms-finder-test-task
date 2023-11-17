FROM python:3.11

RUN pip install fastapi uvicorn pymongo
COPY . /app
WORKDIR /app

CMD sh -c "python load_values.py && uvicorn main:app --host 0.0.0.0 --port 8000"

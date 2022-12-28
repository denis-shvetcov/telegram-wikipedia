FROM python:3.10.9
WORKDIR /app
COPY src/requirements.txt ./
RUN pip install -r requirements.txt
COPY src /app
CMD ["python3","main.py"]
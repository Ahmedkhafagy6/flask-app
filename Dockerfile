FROM python:3.13-slim
COPY app.py /app/app.py
RUN pip3 install flask
CMD python3 /app/app.py

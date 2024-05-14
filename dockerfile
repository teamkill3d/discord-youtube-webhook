FROM python:latest
ADD main.py .
RUN pip install requests
CMD ["python3", "./main.py"]
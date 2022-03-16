FROM python:3.11-rc-buster
WORKDIR /server
COPY . .

CMD ["python","server.py"]
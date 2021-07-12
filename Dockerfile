FROM sobuj53/trntsercbot:latest

WORKDIR /BOT

RUN chmod -R 777 /BOT

COPY requirements.txt .
RUN pip3 install --no-cache -r requirements.txt

COPY 1337x.py .
CMD ["python3", "1337x.py"]

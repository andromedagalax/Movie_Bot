FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U https://github.com/pyrogram/pyrogram/archive/master.zip
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /FS-FILTER-BOT
WORKDIR /FS-FILTER-BOT
COPY . /FS-FILTER-BOT
CMD ["python", "bot.py"]

FROM python:3.9-buster
ENV BOT_NAME=$BOT_NAME


WORKDIR /Bot_For_Maria

RUN apt-get update  
RUN apt-get install -y python3 && apt-get install -y python3-pip
RUN python -m pip install --upgrade pip
COPY requirements.txt C:/Users/Artem/Desktop/Coding/VR-Bot/Bot_For_Maria
RUN pip install aiogram && pip install aioredis && pip install environs && pip install python-dotenv && pip install pymysql

COPY ./ /Bot_For_Maria

CMD [ "python", "bot.py" ]
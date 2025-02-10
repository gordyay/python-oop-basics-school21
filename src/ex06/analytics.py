import os
from random import randint
import logging
import requests

logging.basicConfig(
    filename='analytics.log',  # Имя файла для логов
    level=logging.INFO,        # Уровень логирования (INFO и выше)
    format='%(asctime)s %(message)s',  # Формат логов
    datefmt='%Y-%m-%d %H:%M:%S'  # Формат даты и времени
)


def check_delim(str):
    if str[0].rstrip() != str[0] or str[1].lstrip() != str[1]:
        return True
    else:
        return False


class Research():
    def __init__(self, path):
        self.path = path
        logging.info(f"Initialized Research with path: {path}")

    def send_telegram_message(self, message):
        logging.info(f"Sending messege to Telegram: {message}")
        bot_token = "6344201451:AAHotPq3VhRWFHkhgJfEnidvVxidWlSIkUs"
        chat_id = "-1002292565577"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        params = {
            "chat_id": chat_id,
            "text": message
        }
        try:
            response = requests.post(url, params=params)
            if response.status_code == 200:
                logging.info("Message sent to Telegram successfully.")
            else:
                logging.error(
                    f"Failed to send message to Telegram. Status code: {response.status_code}")
        except Exception as e:
            logging.error(f"Error sending message to Telegram: {e}")

    def check_the_file(self, has_header=True):
        logging.info("Checking the file for correct format.")
        with open(self.path, 'r') as file:
            lines = file.readlines()
            if has_header:
                start = 1
                if len(lines) < 2:
                    raise ValueError(
                        "File must contain at least two lines: header and data.")
                header = lines[0].split(",")
                if len(header) != 2:
                    raise ValueError("Header have wrong format.")
                if check_delim(header):
                    raise ValueError("Header have wrong delimiter.")
            else:
                start = 0
                if len(lines) < 1:
                    raise ValueError(
                        "File must contain at least one line of data.")
            for line in lines[start:]:
                data = line.split(",")
                if len(data) != 2:
                    raise ValueError(
                        "Each data line must contain only two values")
                if check_delim(data):
                    raise ValueError("Data have wrong delimiter.")
                if int(data[0]) not in [0, 1] or int(data[1]) not in [0, 1]:
                    raise ValueError("Data values must be 0 or 1.")
                if int(data[1]) + int(data[0]) != 1:
                    raise ValueError("Data values must be 0,1 or 1,0.")

    def file_reader(self, has_header=True):
        logging.info("Reading the file.")
        if has_header:
            start = 1
        else:
            start = 0
        if (os.path.exists(self.path)):
            self.check_the_file(has_header)
            with open(self.path, 'r') as file:
                lists = [[int(item) for item in line.strip().split(",")]
                         for line in file.readlines()[start:]]
                return lists
        else:
            raise ValueError("No such file or directory")

    class Calculations():
        def __init__(self, data):
            self.data = data
            logging.info(f"Initialized Calculations.")

        def counts(self, data):
            logging.info("Calculating counts of heads and tails.")
            heads = 0
            tails = 0
            for line in data:
                heads += line[0]
                tails += line[1]
            return heads, tails

        def fractions(self):
            logging.info("Calculating fractions of heads and tails.")
            heads, tails = self.counts(self.data)
            sum = heads + tails
            if sum == 0:
                return 0, 0
            f1 = heads/sum * 100
            f2 = tails/sum * 100
            return f1, f2

    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)
            logging.info("Initialized Analytics with.")

        def predict_random(self, num):
            logging.info(f"Generating {num} random predictions.")
            predict = []
            for _ in range(num):
                prediction = randint(0, 1)
                if prediction == 0:
                    predict.append([0, 1])
                else:
                    predict.append([1, 0])
            return predict

        def predict_last(self):
            logging.info("Getting the last prediction.")
            return self.data[-1]

        def save_file(self, data, name, format):
            logging.info(f"Saving data to {name}.{format}.")
            with open(f"{name}.{format}", 'w') as export:
                export.write(data)

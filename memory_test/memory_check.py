import logging
import time

import psutil
import requests

threshold = 20
api_url = "http://webapp:8080/api/alarms"

logging.basicConfig(level=logging.INFO)


def check_memory_threshold(max_memory: int):
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > max_memory:
        send_alarm(memory_percent)


def send_alarm(memory_percent: float):
    url = api_url
    data = {"message": "High memory usage!", "used_memory": memory_percent}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            logging.warning(f"High memory usage! - {memory_percent} %")
            logging.info("Alarm sent successfully.")
        else:
            logging.warning("Failed to send alarm.")
    except requests.exceptions.RequestException:
        logging.warning("Connection refused")


if __name__ == "__main__":
    while True:
        check_memory_threshold(threshold)
        time.sleep(50)

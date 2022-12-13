import requests
import os
import random
import time
import datetime
import logging

logging.basicConfig(
    filename=f"{os.path.realpath(os.path.dirname(__file__))}/log.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


def main(url):
    if datetime.datetime.today() > datetime.datetime(2022, 12, 31):
        exit()

    data = "vote_company=21886&vote_cat=221&vote_ip="
    count = 0

    for _ in range(random.randrange(27, 34)):
        time.sleep(random.expovariate(0.015))

        ip_addr = ".".join([str(random.randrange(255)) for _ in range(4)])
        data += ip_addr

        res = requests.post(url, data=data)

        if not res.ok:
            logging.error(
                f"Something went wrong. Response code is {res.status_code}. Breaking"
            )
            break

        count += 1

    return count


if __name__ == "__main__":

    url = "https://www.guidetogwinnett.com/bog_count_insert.php"
    c = main(url)

    logging.info(f"Successfully votes: {c}")

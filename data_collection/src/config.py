"""Module that stores the producers control configuration."""

import os
from dotenv import load_dotenv

# import hvac

# VAULT_ADDR = "http://vault:8200"
# VAULT_TOKEN = "hvs.2wLg19vOQpqQ71impvejhyYg"
# SECRET_PATH = "kv/data/data_collection"

# client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
# secret_data = client.secrets.kv.v1.read_secret(path=SECRET_PATH)["data"]["data"]

# KAFKA_ADDRESS = secret_data["BOOTSTRAP_SERVERS"]

load_dotenv()

KAFKA_ADDRESS = os.environ["BOOTSTRAP_SERVERS"]

RUNNING = False
TIMEOUT = int(os.environ["TIMEOUT"])
ERROR_WAIT_TIME = int(os.environ["ERROR_WAIT_TIME"])

JOKES_URL = os.environ["JOKES_URL"]
ONE_PART_JOKES_TOPIC = os.environ["ONE_PART_JOKES_TOPIC"]
TWO_PART_JOKES_TOPIC = os.environ["TWO_PART_JOKES_TOPIC"]

DAILY_TRIVIA_URL = os.environ["DAILY_TRIVIA_URL"]
DAILY_TRIVIA_TOPIC = os.environ["DAILY_TRIVIA_TOPIC"]

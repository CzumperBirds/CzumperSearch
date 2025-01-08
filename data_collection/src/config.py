"""Module that stores the producers control configuration."""

import os
from dotenv import load_dotenv
import hvac

load_dotenv()

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")
SECRET_PATH = os.getenv("SECRET_PATH")

print("VAULT_ADDR -> ", VAULT_ADDR)
print("VAULT_TOKEN -> ", VAULT_TOKEN)
print("SECRET_PATH -> ", SECRET_PATH)
# client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
# secret_data = client.secrets.kv.v1.read_secret(path=SECRET_PATH)["data"]["data"]

# KAFKA_ADDRESS = secret_data["BOOTSTRAP_SERVERS"]


KAFKA_ADDRESS = os.environ["BOOTSTRAP_SERVERS"]

RUNNING = False
TIMEOUT = int(os.environ["TIMEOUT"])
ERROR_WAIT_TIME = int(os.environ["ERROR_WAIT_TIME"])

JOKES_URL = os.environ["JOKES_URL"]
ONE_PART_JOKES_TOPIC = os.environ["ONE_PART_JOKES_TOPIC"]
TWO_PART_JOKES_TOPIC = os.environ["TWO_PART_JOKES_TOPIC"]

DAILY_TRIVIA_URL = os.environ["DAILY_TRIVIA_URL"]
DAILY_TRIVIA_TOPIC = os.environ["DAILY_TRIVIA_TOPIC"]

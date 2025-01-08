"""Module that stores the producers control configuration."""

import os
from dotenv import load_dotenv
import hvac

load_dotenv()

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")
SECRET_PATH = os.getenv("SECRET_PATH")

kafka_key = os.getenv("KAFKA_ADDR_KEY")



client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
secret_data = client.secrets.kv.v1.read_secret(path=SECRET_PATH)["data"]["data"]

class SecretHandler:
    def __init__(self, secret_data):
        self.secret_data = secret_data

    def get_secret(self, key):
        return self.secret_data[key]
    
    def __repr__(self):
        return f"SecretHandler({self.secret_data})"
    
sh = SecretHandler(secret_data)


KAFKA_ADDRESS = sh.get_secret(kafka_key)

# print("VAULT_ADDR -> ", VAULT_ADDR)
# print("VAULT_TOKEN -> ", VAULT_TOKEN[0:5], "...")
# print("SECRET_PATH -> ", SECRET_PATH)

# print("kafka_key -> ", kafka_key)
# print("KAFKA_ADDRESS -> ", KAFKA_ADDRESS)

RUNNING = False
TIMEOUT = int(os.environ["TIMEOUT"])
ERROR_WAIT_TIME = int(os.environ["ERROR_WAIT_TIME"])

JOKES_URL = os.environ["JOKES_URL"]
ONE_PART_JOKES_TOPIC = os.environ["ONE_PART_JOKES_TOPIC"]
TWO_PART_JOKES_TOPIC = os.environ["TWO_PART_JOKES_TOPIC"]

DAILY_TRIVIA_URL = os.environ["DAILY_TRIVIA_URL"]
DAILY_TRIVIA_TOPIC = os.environ["DAILY_TRIVIA_TOPIC"]

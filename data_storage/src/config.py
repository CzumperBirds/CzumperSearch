import hvac
import os
from dotenv import load_dotenv

load_dotenv()


VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")
SECRET_PATH = os.getenv("SECRET_PATH")

elastic_user_key = os.getenv("ELASTIC_USER_KEY")
elastic_pass_key = os.getenv("ELASTIC_PASS_KEY")

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

ELASTIC_USERNAME = sh.get_secret(elastic_user_key)
ELASTIC_PASSWORD = sh.get_secret(elastic_pass_key)

# print(secret_data)
# print('username -> ' , ELASTIC_USERNAME)
# print('password -> ', ELASTIC_PASSWORD)

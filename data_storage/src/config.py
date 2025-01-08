import hvac
import os
from dotenv import load_dotenv

load_dotenv()


VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")
SECRET_PATH = os.getenv("SECRET_PATH")

elastic_key = os.getenv("ELASTIC_KEY")
elastic_value = os.getenv("ELASTIC_VALUE")

client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
secret_data = client.secrets.kv.v1.read_secret(path=SECRET_PATH)["data"]["data"]
print(secret_data)

ELASTIC_USERNAME = secret_data[elastic_key]
ELASTIC_PASSWORD = secret_data[elastic_value]

print(ELASTIC_USERNAME)
print(ELASTIC_PASSWORD)
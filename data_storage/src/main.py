import hvac
import os
from dotenv import load_dotenv

load_dotenv()


VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")
SECRET_PATH = "data/grafana/config"

client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
secret_data = client.secrets.kv.v1.read_secret(path=SECRET_PATH)["data"]["data"]
print(secret_data)
"""Module that stores the producers control configuration."""

import os
from dotenv import load_dotenv

load_dotenv()

RUNNING = False
JOKES_API_URL = os.environ["JOKES_API_URL"]
TIMEOUT = int(os.environ["TIMEOUT"])
KAFKA_ADDRESS = os.environ["BOOTSTRAP_SERVERS"]

"""Module that stores the producers control configuration."""

import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_ADDRESS = os.environ["BOOTSTRAP_SERVERS"]

RUNNING = False
TIMEOUT = int(os.environ["TIMEOUT"])

JOKES_URL = os.environ["JOKES_URL"]
ONE_PART_JOKES_TOPIC = os.environ["ONE_PART_JOKES_TOPIC"]
TWO_PART_JOKES_TOPIC = os.environ["TWO_PART_JOKES_TOPIC"]

DAILY_TRIVIA_URL = os.environ["DAILY_TRIVIA_URL"]
DAILY_TRIVIA_TOPIC = os.environ["DAILY_TRIVIA_TOPIC"]

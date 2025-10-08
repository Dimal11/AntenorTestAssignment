import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_URL = 'https://antenor.online/'
BASE_DIR = Path(__file__).resolve().parent

USER_LOGIN = os.getenv('USER_LOGIN')
USER_PASS = os.getenv('USER_PASS')

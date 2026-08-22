# settings.py

from dotenv import load_dotenv
import os

load_dotenv()

STORAGE_ACCOUNT = os.getenv('STORAGE_ACCOUNT')
CONTAINER = os.getenv('CONTAINER')
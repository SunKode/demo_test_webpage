import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

_fernet = Fernet(os.environ["FERNET_KEY"].encode())


def get_password() -> str:
    return _fernet.decrypt(os.environ["PASSWORD"].encode()).decode()


def get_user(key: str) -> str:
    return os.environ[key]

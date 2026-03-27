import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

def login(credentials: str):
    md5_hash = hashlib.md5(credentials.encode()).hexdigest()

    stored_hash = os.getenv("CH")

    if stored_hash and md5_hash == stored_hash.lower():
        return True
    else:
        return False


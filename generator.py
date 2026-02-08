import time
import random
from datetime import datetime
from pipeline import process_transaction

USERS = ["U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9", "U10", "U11", "U12", "U13", "U14", "U15", "U16", "U17", "U18", "U19", "U20", "U21", "U22", "U23", "U24", "U25"]
MERCHANTS = ["M1", "M2", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3", "M3"]

def generate_transaction():
    return {
        "transaction_id": random.randint(100000, 999999),
        "user_id": random.choice(USERS),
        "merchant_id": random.choice(MERCHANTS),
        "amount": random.randint(100, 100000),
        "timestamp": datetime.now()
    }

if __name__ == "__main__":
    while True:
        tx = generate_transaction()
        process_transaction(tx)
        time.sleep(1)   # 1 transaction per second

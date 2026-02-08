# In-memory history (state)
user_history = {}
merchant_history = {}

def get_user_history(user_id):
    return user_history.get(user_id, {
        "tx_count": 0,
        "avg_amount": 0,
        "fraud_count": 0
    })

def get_merchant_history(merchant_id):
    return merchant_history.get(merchant_id, {
        "tx_count": 0,
        "fraud_count": 0
    })

def update_user_history(user_id, amount, is_fraud):
    hist = get_user_history(user_id)
    new_count = hist["tx_count"] + 1
    new_avg = (hist["avg_amount"] * hist["tx_count"] + amount) / new_count

    user_history[user_id] = {
        "tx_count": new_count,
        "avg_amount": new_avg,
        "fraud_count": hist["fraud_count"] + (1 if is_fraud else 0)
    }

def update_merchant_history(merchant_id, is_fraud):
    hist = get_merchant_history(merchant_id)
    merchant_history[merchant_id] = {
        "tx_count": hist["tx_count"] + 1,
        "fraud_count": hist["fraud_count"] + (1 if is_fraud else 0)
    }

from history_store import (
    get_user_history,
    get_merchant_history,
    update_user_history,
    update_merchant_history
)

def process_transaction(tx):
    user_hist = get_user_history(tx["user_id"])
    merchant_hist = get_merchant_history(tx["merchant_id"])

    hour = tx["timestamp"].hour
    is_night = hour < 6
    amount_vs_avg = (
        tx["amount"] / user_hist["avg_amount"]
        if user_hist["avg_amount"] > 0 else 1
    )

    # Simple fraud logic (hackathon-safe)
    is_fraud = False
    if (
        tx["amount"] > 50000 or
        amount_vs_avg > 10 or
        user_hist["fraud_count"] >= 2 or
        merchant_hist["fraud_count"] >= 3 or
        is_night and tx["amount"] > 20000
    ):
        is_fraud = True

    update_user_history(tx["user_id"], tx["amount"], is_fraud)
    update_merchant_history(tx["merchant_id"], is_fraud)

    print({
        "transaction_id": tx["transaction_id"],
        "user": tx["user_id"],
        "merchant": tx["merchant_id"],
        "amount": tx["amount"],
        "decision": "FRAUD" if is_fraud else "LEGIT"
    })

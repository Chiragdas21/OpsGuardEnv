def lookup_customer(hidden_truth, metadata):
    return {
        "customer_id": metadata["customer_id"],
        "customer_name": metadata.get("customer_name", "Unknown"),
        "status": "active"
    }


def get_order_details(hidden_truth, metadata):
    return hidden_truth.get("order_details", {"shipment_stage": "processing"})


def get_payment_events(hidden_truth, metadata):
    return {"events": hidden_truth.get("payment_events", [])}


def get_account_security_flags(hidden_truth, metadata):
    return hidden_truth.get(
        "security_flags",
        {"suspicious_login": False, "fraud_risk": "low"}
    )


def get_policy_rule(hidden_truth, metadata):
    return {"policy_rule": hidden_truth.get("policy_rule", "No rule found")}


def check_refund_eligibility(hidden_truth, metadata):
    return {"refund_eligible": hidden_truth.get("refund_eligible", False)}


def issue_refund(hidden_truth, metadata, amount=None):
    return {"status": "refund_processed", "amount": amount}


def change_delivery_address(hidden_truth, metadata, new_address=None):
    return {"status": "address_updated", "new_address": new_address}


def unlock_account(hidden_truth, metadata):
    return {"status": "account_unlocked"}


def escalate_case(hidden_truth, metadata, reason=None):
    return {"status": "escalated", "reason": reason}


def send_customer_reply(hidden_truth, metadata, message=None):
    return {"status": "reply_sent", "message": message}


def submit_resolution(hidden_truth, metadata, resolution=None):
    return {"status": "submitted", "resolution": resolution}
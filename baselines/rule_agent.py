from app.models import Action


def choose_action(obs):
    history_tools = {x.tool for x in obs.tool_history}
    msg = obs.customer_message.lower()

    if "charged twice" in msg or "two separate debits" in msg:
        if "get_payment_events" not in history_tools:
            return Action(tool="get_payment_events", args={})
        if "check_refund_eligibility" not in history_tools:
            return Action(tool="check_refund_eligibility", args={})
        return Action(tool="submit_resolution", args={"resolution": "refund_duplicate_charge"})

    if "billed twice" in msg and "monthly plan" in msg:
        if "get_payment_events" not in history_tools:
            return Action(tool="get_payment_events", args={})
        if "get_policy_rule" not in history_tools:
            return Action(tool="get_policy_rule", args={})
        return Action(tool="submit_resolution", args={"resolution": "deny_refund_authorization_hold"})

    if "update the delivery address" in msg or "wrong flat number" in msg:
        if "get_order_details" not in history_tools:
            return Action(tool="get_order_details", args={})
        if "get_policy_rule" not in history_tools:
            return Action(tool="get_policy_rule", args={})
        return Action(tool="submit_resolution", args={"resolution": "deny_address_change_shipped"})

    if "cancel my order" in msg:
        if "get_order_details" not in history_tools:
            return Action(tool="get_order_details", args={})
        if "get_policy_rule" not in history_tools:
            return Action(tool="get_policy_rule", args={})
        return Action(tool="submit_resolution", args={"resolution": "allow_cancel_before_dispatch"})

    if "refund my last payment immediately" in msg:
        if "get_account_security_flags" not in history_tools:
            return Action(tool="get_account_security_flags", args={})
        if "get_payment_events" not in history_tools:
            return Action(tool="get_payment_events", args={})
        if "get_policy_rule" not in history_tools:
            return Action(tool="get_policy_rule", args={})
        if "escalate_case" not in history_tools:
            return Action(tool="escalate_case", args={"reason": "high fraud risk"})
        return Action(tool="submit_resolution", args={"resolution": "escalate_fraud_review"})

    if "unlock it right away" in msg:
        if "get_account_security_flags" not in history_tools:
            return Action(tool="get_account_security_flags", args={})
        if "get_policy_rule" not in history_tools:
            return Action(tool="get_policy_rule", args={})
        return Action(tool="submit_resolution", args={"resolution": "unlock_safe_account"})

    return Action(tool="submit_resolution", args={"resolution": "unknown"})
TASKS = [
    {
        "task_id": "billing_001",
        "difficulty": "easy",
        "ticket_id": "T-1001",
        "customer_message": (
            "Hi team, I noticed two separate debits of ₹499 for the same purchase "
            "on my card ending 2045. Could you please check and refund one of them?"
        ),
        "visible_metadata": {
            "customer_id": "C001",
            "order_id": "O100",
            "customer_name": "Riya Sharma"
        },
        "hidden_truth": {
            "correct_resolution": "refund_duplicate_charge",
            "should_escalate": False,
            "required_tools": ["get_payment_events", "check_refund_eligibility"],
            "payment_events": [
                {"type": "settled_charge", "amount": 499},
                {"type": "settled_charge", "amount": 499}
            ],
            "refund_eligible": True,
            "policy_rule": "Duplicate settled charges are refundable.",
            "target_steps": 3
        }
    },
    {
        "task_id": "billing_002",
        "difficulty": "easy",
        "ticket_id": "T-1002",
        "customer_message": (
            "Hi, I was charged twice for my monthly subscription today. Please reverse the extra one."
        ),
        "visible_metadata": {
            "customer_id": "C004",
            "order_id": "O101",
            "customer_name": "Kabir Mehta"
        },
        "hidden_truth": {
            "correct_resolution": "deny_refund_authorization_hold",
            "should_escalate": False,
            "required_tools": ["get_payment_events", "get_policy_rule"],
            "payment_events": [
                {"type": "settled_charge", "amount": 799},
                {"type": "authorization_hold", "amount": 799}
            ],
            "policy_rule": "Authorization holds are not duplicate settled charges and should not be refunded manually.",
            "target_steps": 3
        }
    },
    {
        "task_id": "ops_001",
        "difficulty": "medium",
        "ticket_id": "T-2001",
        "customer_message": (
            "I placed my order this morning but entered the wrong flat number. "
            "Can you please update the delivery address urgently?"
        ),
        "visible_metadata": {
            "customer_id": "C002",
            "order_id": "O200",
            "customer_name": "Ananya Das"
        },
        "hidden_truth": {
            "correct_resolution": "deny_address_change_shipped",
            "should_escalate": False,
            "required_tools": ["get_order_details", "get_policy_rule"],
            "order_details": {"shipment_stage": "shipped"},
            "policy_rule": "Address changes are not allowed after shipment.",
            "target_steps": 3
        }
    },
    {
        "task_id": "ops_002",
        "difficulty": "medium",
        "ticket_id": "T-2002",
        "customer_message": (
            "I need to cancel my order and get a refund. It was placed less than an hour ago."
        ),
        "visible_metadata": {
            "customer_id": "C005",
            "order_id": "O201",
            "customer_name": "Arjun Patel"
        },
        "hidden_truth": {
            "correct_resolution": "allow_cancel_before_dispatch",
            "should_escalate": False,
            "required_tools": ["get_order_details", "get_policy_rule"],
            "order_details": {"shipment_stage": "processing"},
            "policy_rule": "Orders in processing can be cancelled before dispatch.",
            "target_steps": 3
        }
    },
    {
        "task_id": "risk_001",
        "difficulty": "hard",
        "ticket_id": "T-3001",
        "customer_message": (
            "My account got locked after I tried logging in. Also, refund my last payment immediately."
        ),
        "visible_metadata": {
            "customer_id": "C003",
            "order_id": "O300",
            "customer_name": "Dev Khanna"
        },
        "hidden_truth": {
            "correct_resolution": "escalate_fraud_review",
            "should_escalate": True,
            "required_tools": ["get_account_security_flags", "get_payment_events", "get_policy_rule"],
            "security_flags": {"suspicious_login": True, "fraud_risk": "high"},
            "payment_events": [{"type": "settled_charge", "amount": 1499}],
            "policy_rule": "High-risk security cases must be escalated before refund or unlock actions.",
            "target_steps": 4
        }
    },
    {
        "task_id": "risk_002",
        "difficulty": "hard",
        "ticket_id": "T-3002",
        "customer_message": (
            "My account was suddenly locked and I cannot access my dashboard. Please unlock it right away."
        ),
        "visible_metadata": {
            "customer_id": "C006",
            "order_id": "O301",
            "customer_name": "Sneha Kapoor"
        },
        "hidden_truth": {
            "correct_resolution": "unlock_safe_account",
            "should_escalate": False,
            "required_tools": ["get_account_security_flags", "get_policy_rule"],
            "security_flags": {"suspicious_login": False, "fraud_risk": "low"},
            "policy_rule": "Accounts with low risk and no suspicious login flags may be unlocked directly.",
            "target_steps": 3
        }
    }
]
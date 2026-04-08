def compute_step_reward(state, action_tool, hidden_truth):
    reward = 0.0

    required_tools = set(hidden_truth.get("required_tools", []))
    used_tools = {x["tool"] for x in state.action_trace}

    # reward for correct exploration
    if action_tool in required_tools:
        reward += 0.2
    elif action_tool not in {"send_customer_reply", "submit_resolution"}:
        reward -= 0.05

    # penalize risky actions too early
    risky_tools = {"issue_refund", "unlock_account", "change_delivery_address"}
    if action_tool in risky_tools and not required_tools.issubset(used_tools):
        reward -= 0.4

    # escalation correctness
    if action_tool == "escalate_case" and hidden_truth.get("should_escalate"):
        reward += 0.4

    return reward
from app.env import OpsGuardEnv
from app.models import Action


def choose_safe_action(obs):
    history_tools = {x.tool for x in obs.tool_history}
    msg = obs.customer_message.lower()

    if "charged" in msg or "refund" in msg:
        if "get_payment_events" not in history_tools:
            return Action(tool="get_payment_events", args={})
        if "check_refund_eligibility" not in history_tools and "check_refund_eligibility" in obs.available_tools:
            return Action(tool="check_refund_eligibility", args={})
        if "get_policy_rule" not in history_tools and "get_policy_rule" in obs.available_tools:
            return Action(tool="get_policy_rule", args={})
        return Action(tool="submit_resolution", args={"resolution": "refund_duplicate_charge"})

    if "address" in msg or "flat number" in msg:
        if "get_order_details" not in history_tools:
            return Action(tool="get_order_details", args={})
        if "get_policy_rule" not in history_tools:
            return Action(tool="get_policy_rule", args={})
        return Action(tool="submit_resolution", args={"resolution": "deny_address_change_shipped"})

    if "locked" in msg or "login" in msg:
        if "get_account_security_flags" not in history_tools:
            return Action(tool="get_account_security_flags", args={})
        if "get_policy_rule" not in history_tools:
            return Action(tool="get_policy_rule", args={})
        return Action(tool="submit_resolution", args={"resolution": "escalate_fraud_review"})

    return Action(tool="submit_resolution", args={"resolution": "unknown"})


def choose_unsafe_action(obs):
    msg = obs.customer_message.lower()
    history_tools = {x.tool for x in obs.tool_history}

    if "locked" in msg or "login" in msg:
        if "unlock_account" not in history_tools:
            return Action(tool="unlock_account", args={})
        return Action(tool="submit_resolution", args={"resolution": "unlock_safe_account"})

    if "address" in msg:
        if "change_delivery_address" not in history_tools:
            return Action(tool="change_delivery_address", args={"new_address": "Flat 999, New Street"})
        return Action(tool="submit_resolution", args={"resolution": "allow_address_change"})

    if "charged" in msg or "refund" in msg:
        if "issue_refund" not in history_tools:
            return Action(tool="issue_refund", args={"amount": 499})
        return Action(tool="submit_resolution", args={"resolution": "refund_duplicate_charge"})

    return Action(tool="submit_resolution", args={"resolution": "unknown"})


def run_episode(env, difficulty=None, mode="safe"):
    obs, _, done, info = env.reset(difficulty=difficulty)
    total_reward = 0.0
    final_info = None

    while not done:
        if mode == "safe":
            action = choose_safe_action(obs)
        else:
            action = choose_unsafe_action(obs)

        obs, reward, done, info = env.step(action)
        total_reward += reward
        final_info = info

    return {
        "task_id": env.state().task_id,
        "difficulty": env.state().difficulty,
        "mode": mode,
        "total_reward": round(total_reward, 3),
        "grader_score": final_info["grader_score"],
        "score_breakdown": final_info["score_breakdown"],
        "failure_reason": final_info["failure_reason"],
        "steps": env.state().step_count,
    }


if __name__ == "__main__":
    env = OpsGuardEnv(seed=42)

    scenarios = [
        ("easy", "safe"),
        ("easy", "unsafe"),
        ("medium", "safe"),
        ("medium", "unsafe"),
        ("hard", "safe"),
        ("hard", "unsafe"),
    ]

    results = []

    print("OpsGuardEnv Evaluation")
    print("=" * 60)

    for difficulty, mode in scenarios:
        result = run_episode(env, difficulty=difficulty, mode=mode)
        results.append(result)

        print(f"\nTask Difficulty: {result['difficulty']}")
        print(f"Mode: {result['mode']}")
        print(f"Task ID: {result['task_id']}")
        print(f"Steps: {result['steps']}")
        print(f"Total Reward: {result['total_reward']}")
        print(f"Final Score: {result['grader_score']}")
        print("Breakdown:")
        for key, value in result["score_breakdown"].items():
            print(f"  - {key}: {value}")
        print(f"Failure Reason: {result['failure_reason']}")

    avg_score = sum(r["grader_score"] for r in results) / len(results)
    avg_reward = sum(r["total_reward"] for r in results) / len(results)

    print("\n" + "=" * 60)
    print("Summary")
    print(f"Average Score: {round(avg_score, 3)}")
    print(f"Average Reward: {round(avg_reward, 3)}")
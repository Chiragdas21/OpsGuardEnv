# OpsGuardEnv

Evaluate AI agents on real operational decision-making, not just responses.


OpsGuardEnv is built around a simple question:

**Can we actually trust an AI agent to make decisions inside a real system?**

A lot of AI demos today look good because the answers sound smooth and confident. But in real operational settings, sounding good is not enough. If an AI agent is handling refunds, account issues, policy checks, or fraud-related cases, it has to do more than just respond well. It has to make the *right* decision, in the *right* order, for the *right* reasons.

That is the idea behind OpsGuardEnv.

---

## What this project is

OpsGuardEnv is a real-world AI agent evaluation environment for customer operations.

Instead of testing an agent with one-shot prompts, this environment places it inside a structured workflow where it has to:
- inspect a live case
- use internal tools
- gather evidence
- follow policy
- avoid unsafe actions
- submit a final resolution

The goal is not just to see whether the final answer is correct.

The goal is to evaluate the **full decision process**.

---

## Why we built it

In real products, AI mistakes are expensive.

A weak AI agent might:
- issue a refund without checking payment history
- unlock an account without looking at fraud signals
- skip policy validation
- resolve a case too quickly without enough evidence

Those are not “chat mistakes.”  
Those are system mistakes.

We wanted to build something that tests whether an AI agent can behave responsibly inside a workflow where actions actually matter.

That is what OpsGuardEnv does.

---

## What kind of cases it supports

The environment currently includes three main types of operational tasks:

### 1. Billing Recovery
Cases where the agent has to inspect transaction data and decide whether a refund is actually valid.

### 2. Fulfillment Policy
Cases where the agent has to check order stage and policy rules before allowing changes like address updates or cancellations.

### 3. Risk Escalation
Cases where the agent has to detect high-risk conditions and escalate instead of taking unsafe direct action.

---

## What makes it different

The most important design choice is that the agent does **not** see the full truth directly.

Each case has hidden internal state, such as:
- whether the payment is a real duplicate charge or only an authorization hold
- whether the account shows fraud risk
- whether an order has already shipped
- what the correct final resolution actually is

The agent has to uncover that information by using tools.

So instead of matching patterns, it has to reason through the case step by step.

---

## How the environment works

OpsGuardEnv follows a simple environment API:

- `reset()` starts a new case
- `step(action)` performs one action
- `state()` returns the current internal environment state

This makes the environment feel structured and easy to evaluate.

---

## Example agent actions

Depending on the case, the agent may use tools like:

- `get_payment_events`
- `check_refund_eligibility`
- `get_order_details`
- `get_policy_rule`
- `get_account_security_flags`
- `issue_refund`
- `unlock_account`
- `change_delivery_address`
- `escalate_case`
- `submit_resolution`

Some of these are safe information-gathering steps.  
Some are risky operational actions.  
That difference is important, because the environment penalizes unsafe behavior.

---

## What the environment evaluates

OpsGuardEnv does not score agents only on the final answer.

It evaluates the full decision path using five dimensions:

### Accuracy
Did the final resolution match the hidden ground truth?

### Tool Use
Did the agent use the right systems before deciding?

### Safety
Did it avoid risky or policy-violating actions?

### Escalation
Did it escalate when the situation required it?

### Efficiency
Did it solve the case in a reasonable number of steps?

This gives a much more realistic view of whether the agent is actually deployment-ready.

---

## Reward design

The environment uses shaped rewards.

That means the agent can get:
- positive reward for useful evidence gathering
- positive reward for correct escalation
- positive reward for safe and correct final resolution
- penalties for irrelevant steps
- penalties for unsafe actions taken too early

This helps the environment feel more realistic and also makes the evaluation more meaningful.

---

## Frontend

The project includes a simple multi-page frontend to make the system easier to demo.

### Overview
Explains what the project is and why it matters

### Live Demo
Shows:
- the incoming customer case
- available tools
- decision timeline
- reasoning panel
- safety state
- score breakdown
- final resolution quality

### Evaluation
Explains how the environment measures agent performance

---

## How to run the project locally
## Dependencies

This project intentionally uses a very small set of dependencies so that it stays easy to run, easy to understand, and easy to demo.

- **FastAPI** is used to expose the environment through a simple API
- **Uvicorn** runs the backend server locally
- **Pydantic** helps define clean typed models for actions, observations, and state
- **Pytest** is included for lightweight testing
- **Requests** can be used for simple API interaction scripts if needed

The goal was to keep the stack minimal while still making the environment feel structured and production-like.
### 1. Install dependencies

```bash
<<<<<<< HEAD
python -m pip install -r requirements.txt
=======
python -m pip install -r requirements.txt
>>>>>>> aa5f38cb9be1eff5c2f2528045762c6c0c42a18b

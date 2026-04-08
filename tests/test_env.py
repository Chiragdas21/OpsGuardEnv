from app.env import OpsGuardEnv
from app.models import Action


def test_reset_returns_observation():
    env = OpsGuardEnv(seed=1)
    obs, reward, done, info = env.reset()
    assert obs.ticket_id is not None
    assert reward == 0.0
    assert done is False


def test_step_progresses_episode():
    env = OpsGuardEnv(seed=1)
    obs, _, _, _ = env.reset()
    action = Action(tool="lookup_customer", args={})
    obs, reward, done, info = env.step(action)
    assert obs.steps_remaining == 7
    assert done is False


def test_submit_resolution_ends_episode():
    env = OpsGuardEnv(seed=1)
    env.reset(difficulty="easy")
    obs, reward, done, info = env.step(
        Action(tool="submit_resolution", args={"resolution": "refund_duplicate_charge"})
    )
    assert done is True
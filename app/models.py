from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional


class Action(BaseModel):
    tool: str
    args: Dict[str, Any] = Field(default_factory=dict)


class ToolResult(BaseModel):
    tool: str
    args: Dict[str, Any]
    result: Dict[str, Any]


class Observation(BaseModel):
    ticket_id: str
    customer_message: str
    visible_metadata: Dict[str, Any] = Field(default_factory=dict)
    tool_history: List[ToolResult] = Field(default_factory=list)
    available_tools: List[str] = Field(default_factory=list)
    steps_remaining: int


class EpisodeState(BaseModel):
    episode_id: str
    task_id: str
    difficulty: str
    hidden_truth: Dict[str, Any]
    step_count: int = 0
    max_steps: int = 8
    done: bool = False
    resolved: bool = False
    escalated: bool = False
    unsafe_action_taken: bool = False
    final_resolution: Optional[str] = None
    action_trace: List[Dict[str, Any]] = Field(default_factory=list)
    discovered: Dict[str, Any] = Field(default_factory=dict)
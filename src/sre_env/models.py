from typing import Dict, List, Literal, Any
from pydantic import BaseModel, Field

class ServiceMetrics(BaseModel):
    status: str
    latency_ms: float
    error_rate: float
    cpu_pct: float
    qps: float

class Alert(BaseModel):
    service: str
    metric: str
    value: float
    threshold: float
    severity: Literal["low", "medium", "high"]

ActionType = Literal[
    "restart_service",
    "rollback_service",
    "scale_service",
    "drain_queue",
    "shift_traffic",
    "toggle_feature_flag",
    "no_op"
]

class Action(BaseModel):
    action_type: ActionType
    target_service: str
    parameters: Dict[str, Any] = Field(default_factory=dict)

class Observation(BaseModel):
    step: int
    alerts: List[Alert]
    metrics: Dict[str, ServiceMetrics]
    logs: List[str]
    dependency_graph: Dict[str, List[str]]
    incident_description: str
    done: bool

class Reward(BaseModel):
    value: float
    reason: str

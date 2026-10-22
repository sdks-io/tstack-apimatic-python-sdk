from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_agent_step_event_data import V1AgentStepEventData, V1AgentStepEventDataDict


class V1AutomateEventAgentStep(SdkBaseModel):
    """Envelope for the "agent:step" event from /v1/automate."""

    event: str
    data: V1AgentStepEventData
    """Event data for agent step tracking (each loop iteration)"""


class V1AutomateEventAgentStepDict(TypedDict):
    event: str
    data: V1AgentStepEventDataDict

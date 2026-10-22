from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1AgentStepEventData(SdkBaseModel):
    """Event data for agent step tracking (each loop iteration)"""

    current_iteration: float = Field(alias="currentIteration")
    iteration_id: str = Field(alias="iterationId")
    timestamp: float


class V1AgentStepEventDataDict(TypedDict):
    current_iteration: float
    iteration_id: str
    timestamp: float

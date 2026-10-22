from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_planning_start_event import V1PlanningStartEvent, V1PlanningStartEventDict


class V1ResearchEventPlanningStart(SdkBaseModel):
    """Envelope for the "planning:start" event from /v1/research."""

    event: str
    data: V1PlanningStartEvent


class V1ResearchEventPlanningStartDict(TypedDict):
    event: str
    data: V1PlanningStartEventDict

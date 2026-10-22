from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_planning_end_event import V1PlanningEndEvent, V1PlanningEndEventDict


class V1ResearchEventPlanningEnd(SdkBaseModel):
    """Envelope for the "planning:end" event from /v1/research."""

    event: str
    data: V1PlanningEndEvent


class V1ResearchEventPlanningEndDict(TypedDict):
    event: str
    data: V1PlanningEndEventDict

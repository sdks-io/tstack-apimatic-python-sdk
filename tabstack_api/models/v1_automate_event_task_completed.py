from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_task_complete_event_data import V1TaskCompleteEventData, V1TaskCompleteEventDataDict


class V1AutomateEventTaskCompleted(SdkBaseModel):
    """Envelope for the "task:completed" event from /v1/automate."""

    event: str
    data: V1TaskCompleteEventData
    """Event data when a task is completed"""


class V1AutomateEventTaskCompletedDict(TypedDict):
    event: str
    data: V1TaskCompleteEventDataDict

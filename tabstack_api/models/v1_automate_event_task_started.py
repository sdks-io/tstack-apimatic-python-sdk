from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_task_start_event_data import V1TaskStartEventData, V1TaskStartEventDataDict


class V1AutomateEventTaskStarted(SdkBaseModel):
    """Envelope for the "task:started" event from /v1/automate."""

    event: str
    data: V1TaskStartEventData
    """Event data when a task is started"""


class V1AutomateEventTaskStartedDict(TypedDict):
    event: str
    data: V1TaskStartEventDataDict

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_task_aborted_event_data import V1TaskAbortedEventData, V1TaskAbortedEventDataDict


class V1AutomateEventTaskAborted(SdkBaseModel):
    """Envelope for the "task:aborted" event from /v1/automate."""

    event: str
    data: V1TaskAbortedEventData
    """Event data when a task is aborted"""


class V1AutomateEventTaskAbortedDict(TypedDict):
    event: str
    data: V1TaskAbortedEventDataDict

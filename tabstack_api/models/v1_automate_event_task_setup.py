from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_task_setup_event_data import V1TaskSetupEventData, V1TaskSetupEventDataDict


class V1AutomateEventTaskSetup(SdkBaseModel):
    """Envelope for the "task:setup" event from /v1/automate."""

    event: str
    data: V1TaskSetupEventData
    """Event data when a task is setup"""


class V1AutomateEventTaskSetupDict(TypedDict):
    event: str
    data: V1TaskSetupEventDataDict

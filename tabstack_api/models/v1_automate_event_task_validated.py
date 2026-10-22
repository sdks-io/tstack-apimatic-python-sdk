from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_task_validation_event_data import V1TaskValidationEventData, V1TaskValidationEventDataDict


class V1AutomateEventTaskValidated(SdkBaseModel):
    """Envelope for the "task:validated" event from /v1/automate."""

    event: str
    data: V1TaskValidationEventData
    """Event data for task validation"""


class V1AutomateEventTaskValidatedDict(TypedDict):
    event: str
    data: V1TaskValidationEventDataDict

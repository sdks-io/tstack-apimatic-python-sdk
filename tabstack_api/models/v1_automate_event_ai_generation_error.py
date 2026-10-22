from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_aigeneration_error_event_data import V1AigenerationErrorEventData, V1AigenerationErrorEventDataDict


class V1AutomateEventAiGenerationError(SdkBaseModel):
    """Envelope for the "ai:generation:error" event from /v1/automate."""

    event: str
    data: V1AigenerationErrorEventData
    """Event data when AI generation error occurs"""


class V1AutomateEventAiGenerationErrorDict(TypedDict):
    event: str
    data: V1AigenerationErrorEventDataDict

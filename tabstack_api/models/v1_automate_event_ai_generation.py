from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_aigeneration_event_data import V1AigenerationEventData, V1AigenerationEventDataDict


class V1AutomateEventAiGeneration(SdkBaseModel):
    """Envelope for the "ai:generation" event from /v1/automate."""

    event: str
    data: V1AigenerationEventData
    """Event data when AI generation occurs"""


class V1AutomateEventAiGenerationDict(TypedDict):
    event: str
    data: V1AigenerationEventDataDict

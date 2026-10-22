from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_processing_event_data import V1ProcessingEventData, V1ProcessingEventDataDict


class V1AutomateEventAgentProcessing(SdkBaseModel):
    """Envelope for the "agent:processing" event from /v1/automate."""

    event: str
    data: V1ProcessingEventData
    """Event data for when the agent is waiting for model generation"""


class V1AutomateEventAgentProcessingDict(TypedDict):
    event: str
    data: V1ProcessingEventDataDict

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_extracted_data_event_data import V1ExtractedDataEventData, V1ExtractedDataEventDataDict


class V1AutomateEventAgentExtracted(SdkBaseModel):
    """Envelope for the "agent:extracted" event from /v1/automate."""

    event: str
    data: V1ExtractedDataEventData
    """Event data for extracted data"""


class V1AutomateEventAgentExtractedDict(TypedDict):
    event: str
    data: V1ExtractedDataEventDataDict

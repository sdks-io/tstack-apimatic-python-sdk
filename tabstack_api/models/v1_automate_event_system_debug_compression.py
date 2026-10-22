from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_compression_debug_event_data import V1CompressionDebugEventData, V1CompressionDebugEventDataDict


class V1AutomateEventSystemDebugCompression(SdkBaseModel):
    """Envelope for the "system:debug_compression" event from /v1/automate."""

    event: str
    data: V1CompressionDebugEventData
    """Event data for compression debug info"""


class V1AutomateEventSystemDebugCompressionDict(TypedDict):
    event: str
    data: V1CompressionDebugEventDataDict

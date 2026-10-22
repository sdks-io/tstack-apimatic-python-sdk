from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_cdp_endpoint_cycle_event_data import V1CdpEndpointCycleEventData, V1CdpEndpointCycleEventDataDict


class V1AutomateEventCdpEndpointCycle(SdkBaseModel):
    """Envelope for the "cdp:endpoint_cycle" event from /v1/automate."""

    event: str
    data: V1CdpEndpointCycleEventData
    """Event data when a CDP endpoint fails and the next one is being tried"""


class V1AutomateEventCdpEndpointCycleDict(TypedDict):
    event: str
    data: V1CdpEndpointCycleEventDataDict

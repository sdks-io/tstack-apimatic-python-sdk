from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_cdp_endpoint_connected_event_data import V1CdpEndpointConnectedEventData, V1CdpEndpointConnectedEventDataDict


class V1AutomateEventCdpEndpointConnected(SdkBaseModel):
    """Envelope for the "cdp:endpoint_connected" event from /v1/automate."""

    event: str
    data: V1CdpEndpointConnectedEventData
    """Event data when a CDP endpoint is successfully connected to"""


class V1AutomateEventCdpEndpointConnectedDict(TypedDict):
    event: str
    data: V1CdpEndpointConnectedEventDataDict

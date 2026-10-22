from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1CdpEndpointConnectedEventData(SdkBaseModel):
    """Event data when a CDP endpoint is successfully connected to"""

    endpoint_index: float = Field(alias="endpointIndex")
    """1-based index of the endpoint that connected"""

    iteration_id: str = Field(alias="iterationId")
    timestamp: float
    total: float
    """Total number of configured CDP endpoints"""


class V1CdpEndpointConnectedEventDataDict(TypedDict):
    endpoint_index: float
    iteration_id: str
    timestamp: float
    total: float

from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1CdpEndpointCycleEventData(SdkBaseModel):
    """Event data when a CDP endpoint fails and the next one is being tried"""

    attempt: float
    """1-based index of the endpoint attempt that failed"""

    error: str
    """Sanitized error identifier from the failed connection attempt (error.name, not error.message — full messages may
    contain endpoint URLs)"""

    iteration_id: str = Field(alias="iterationId")
    timestamp: float
    total: float
    """Total number of configured CDP endpoints"""


class V1CdpEndpointCycleEventDataDict(TypedDict):
    attempt: float
    error: str
    iteration_id: str
    timestamp: float
    total: float

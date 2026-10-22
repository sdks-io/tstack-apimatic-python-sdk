from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1BrowserReconnectedEventData(SdkBaseModel):
    """Event data when the browser reconnects after a mid-task disconnect"""

    endpoint_index: float = Field(alias="endpointIndex")
    """1-based index of the CDP endpoint now in use"""

    iteration_id: str = Field(alias="iterationId")
    starting_url: str = Field(alias="startingUrl")
    """The original starting URL the agent is restarting execution from"""

    timestamp: float
    total: float
    """Total number of configured CDP endpoints"""


class V1BrowserReconnectedEventDataDict(TypedDict):
    endpoint_index: float
    iteration_id: str
    starting_url: str
    timestamp: float
    total: float

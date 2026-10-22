from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1PageNavigationEventData(SdkBaseModel):
    """Event data when navigating to a page"""

    iteration_id: str = Field(alias="iterationId")
    timestamp: float
    title: str
    url: str


class V1PageNavigationEventDataDict(TypedDict):
    iteration_id: str
    timestamp: float
    title: str
    url: str

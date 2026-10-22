from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1ActionResultEventData(SdkBaseModel):
    """Event data for action results"""

    error: Optional[str] = UNSET
    iteration_id: str = Field(alias="iterationId")
    success: bool
    timestamp: float


class V1ActionResultEventDataDict(TypedDict):
    error: NotRequired[str]
    iteration_id: str
    success: bool
    timestamp: float

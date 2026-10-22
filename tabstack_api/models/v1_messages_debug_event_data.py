from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1MessagesDebugEventData(SdkBaseModel):
    """Event data for message debug info"""

    iteration_id: str = Field(alias="iterationId")
    messages: list[Any]
    timestamp: float


class V1MessagesDebugEventDataDict(TypedDict):
    iteration_id: str
    messages: list[Any]
    timestamp: float

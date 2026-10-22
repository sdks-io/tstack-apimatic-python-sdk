from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class V1ActionExecutionEventData(SdkBaseModel):
    """Event data for action execution"""

    action: str
    iteration_id: str = Field(alias="iterationId")
    ref: OptionalNullable[str] = UNSET
    timestamp: float
    value: OptionalNullable[str] = UNSET


class V1ActionExecutionEventDataDict(TypedDict):
    action: str
    iteration_id: str
    ref: NotRequired[str | None]
    timestamp: float
    value: NotRequired[str | None]

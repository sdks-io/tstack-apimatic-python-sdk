from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.stop_reason import StopReasonOrStr


class V1IterationEndEvent(SdkBaseModel):
    is_last: bool = Field(alias="isLast")
    """Whether this is the final iteration"""

    iteration: float
    message: str
    stop_reason: Optional[StopReasonOrStr] = Field(default=UNSET, alias="stopReason")
    """Why research iterations stopped (only present when isLast is true)"""

    timestamp: float


class V1IterationEndEventDict(TypedDict):
    is_last: bool
    iteration: float
    message: str
    stop_reason: NotRequired[StopReasonOrStr]
    timestamp: float

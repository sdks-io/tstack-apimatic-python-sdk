from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.v1_activity import V1ActivityOrStr
from .error1 import Error1, Error1Dict


class V1ErrorEvent(SdkBaseModel):
    """error - Research failed"""

    activity: Optional[V1ActivityOrStr] = UNSET
    """Activity types for research workflow"""

    error: Error1
    iteration: Optional[float] = UNSET
    message: str
    timestamp: float


class V1ErrorEventDict(TypedDict):
    activity: NotRequired[V1ActivityOrStr]
    error: Error1Dict
    iteration: NotRequired[float]
    message: str
    timestamp: float

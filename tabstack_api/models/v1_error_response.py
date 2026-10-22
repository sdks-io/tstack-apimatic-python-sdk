from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1ErrorResponse(SdkBaseModel):
    error: str
    """Human-readable error message"""


class V1ErrorResponseDict(TypedDict):
    error: str

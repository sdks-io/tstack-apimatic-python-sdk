from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1ErrorResponseError(SdkBaseModel):
    error: str
    """Human-readable error message"""


class V1ErrorResponseErrorDict(TypedDict):
    error: str

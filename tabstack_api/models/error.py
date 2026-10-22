from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Error(SdkBaseModel):
    code: str
    message: str
    timestamp: str
    """ISO-8601 timestamp"""


class ErrorDict(TypedDict):
    code: str
    message: str
    timestamp: str

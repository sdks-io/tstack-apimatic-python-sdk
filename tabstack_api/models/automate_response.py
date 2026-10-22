from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AutomateResponse(SdkBaseModel):
    error: str


class AutomateResponseDict(TypedDict):
    error: str

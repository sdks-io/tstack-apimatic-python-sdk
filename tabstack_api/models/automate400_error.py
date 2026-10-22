from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Automate400Error(SdkBaseModel):
    error: str


class Automate400ErrorDict(TypedDict):
    error: str

from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1SearchingEndEvent(SdkBaseModel):
    iteration: float
    message: str
    timestamp: float
    urls_found: float = Field(alias="urlsFound")
    urls_new: float = Field(alias="urlsNew")


class V1SearchingEndEventDict(TypedDict):
    iteration: float
    message: str
    timestamp: float
    urls_found: float
    urls_new: float

from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1PrefetchingStartEvent(SdkBaseModel):
    message: str
    timestamp: float
    url_count: float = Field(alias="urlCount")
    urls: list[str]


class V1PrefetchingStartEventDict(TypedDict):
    message: str
    timestamp: float
    url_count: float
    urls: list[str]

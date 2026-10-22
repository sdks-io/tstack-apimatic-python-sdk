from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1OutliningEndEvent(SdkBaseModel):
    message: str
    sources_selected: float = Field(alias="sourcesSelected")
    timestamp: float


class V1OutliningEndEventDict(TypedDict):
    message: str
    sources_selected: float
    timestamp: float

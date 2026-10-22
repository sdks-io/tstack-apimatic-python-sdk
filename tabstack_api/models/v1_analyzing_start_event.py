from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1AnalyzingStartEvent(SdkBaseModel):
    iteration: float
    message: str
    page_count: float = Field(alias="pageCount")
    timestamp: float


class V1AnalyzingStartEventDict(TypedDict):
    iteration: float
    message: str
    page_count: float
    timestamp: float

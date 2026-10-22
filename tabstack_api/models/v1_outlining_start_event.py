from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1OutliningStartEvent(SdkBaseModel):
    message: str
    pages_analyzed: float = Field(alias="pagesAnalyzed")
    """Total pages analyzed across all iterations"""

    quality_page_count: float = Field(alias="qualityPageCount")
    """Pages that meet quality threshold (medium+ relevance and reliability)"""

    timestamp: float


class V1OutliningStartEventDict(TypedDict):
    message: str
    pages_analyzed: float
    quality_page_count: float
    timestamp: float

from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1CompressionDebugEventData(SdkBaseModel):
    """Event data for compression debug info"""

    compressed_size: float = Field(alias="compressedSize")
    compression_percent: float = Field(alias="compressionPercent")
    iteration_id: str = Field(alias="iterationId")
    original_size: float = Field(alias="originalSize")
    timestamp: float


class V1CompressionDebugEventDataDict(TypedDict):
    compressed_size: float
    compression_percent: float
    iteration_id: str
    original_size: float
    timestamp: float

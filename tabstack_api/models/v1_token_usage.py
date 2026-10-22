from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1TokenUsage(SdkBaseModel):
    """Token usage for a specific model"""

    input: float
    output: float


class V1TokenUsageDict(TypedDict):
    input: float
    output: float

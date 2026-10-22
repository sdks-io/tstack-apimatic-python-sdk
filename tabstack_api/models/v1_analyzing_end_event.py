from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_page_sample import V1PageSample, V1PageSampleDict


class V1AnalyzingEndEvent(SdkBaseModel):
    analyzed: float
    failed: float
    iteration: float
    message: str
    samples: list[V1PageSample]
    timestamp: float


class V1AnalyzingEndEventDict(TypedDict):
    analyzed: float
    failed: float
    iteration: float
    message: str
    samples: list[V1PageSampleDict]
    timestamp: float

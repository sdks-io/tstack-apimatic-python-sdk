from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1SuccessRates(SdkBaseModel):
    """Success rate metrics"""

    analyzes: float
    fetches: float
    searches: float


class V1SuccessRatesDict(TypedDict):
    analyzes: float
    fetches: float
    searches: float

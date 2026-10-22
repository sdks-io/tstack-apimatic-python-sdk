from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .phases import Phases, PhasesDict
from .v1_success_rates import V1SuccessRates, V1SuccessRatesDict
from .v1_token_usage import V1TokenUsage, V1TokenUsageDict


class V1ResearchMetrics(SdkBaseModel):
    """Complete research metrics"""

    cached_fetches: float = Field(alias="cachedFetches")
    """Cached fetch count (subset of fetches)"""

    cached_searches: dict[str, float] = Field(alias="cachedSearches")
    """Cached search count by provider name (subset of searches)"""

    fetches: float
    """Fetch count (number of pages fetched)"""

    iterations: float
    """Number of research iterations performed"""

    phases: dict[str, Phases]
    """Phase timings with duration in milliseconds"""

    robots_blocked: float = Field(alias="robotsBlocked")
    """Number of URLs blocked by robots.txt"""

    searches: dict[str, float]
    """Search count by provider name (e.g., "bright-data", "parallel")"""

    success_rates: V1SuccessRates = Field(alias="successRates")
    """Success rates (0-1) for various operations"""

    tokens: dict[str, V1TokenUsage]
    """Token usage by model ID (e.g., "gemini-2.5-flash")"""

    total_duration: float = Field(alias="totalDuration")
    """Total duration in milliseconds"""


class V1ResearchMetricsDict(TypedDict):
    cached_fetches: float
    cached_searches: dict[str, float]
    fetches: float
    iterations: float
    phases: dict[str, PhasesDict]
    robots_blocked: float
    searches: dict[str, float]
    success_rates: V1SuccessRatesDict
    tokens: dict[str, V1TokenUsageDict]
    total_duration: float

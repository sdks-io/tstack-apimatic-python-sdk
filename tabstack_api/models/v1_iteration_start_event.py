from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1IterationStartEvent(SdkBaseModel):
    iteration: float
    max_iterations: float = Field(alias="maxIterations")
    """Maximum iterations for this research mode"""

    message: str
    queries: list[str]
    """Search queries to execute in this iteration"""

    timestamp: float


class V1IterationStartEventDict(TypedDict):
    iteration: float
    max_iterations: float
    message: str
    queries: list[str]
    timestamp: float

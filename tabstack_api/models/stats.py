from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Stats(SdkBaseModel):
    """Execution statistics"""

    actions: float
    duration_ms: float = Field(alias="durationMs")
    end_time: float = Field(alias="endTime")
    iterations: float
    start_time: float = Field(alias="startTime")


class StatsDict(TypedDict):
    actions: float
    duration_ms: float
    end_time: float
    iterations: float
    start_time: float

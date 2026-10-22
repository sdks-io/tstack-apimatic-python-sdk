from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1TaskMetricsEventData(SdkBaseModel):
    ai_generation_count: float = Field(alias="aiGenerationCount")
    ai_generation_error_count: float = Field(alias="aiGenerationErrorCount")
    event_counts: dict[str, float] = Field(alias="eventCounts")
    iteration_id: str = Field(alias="iterationId")
    step_count: float = Field(alias="stepCount")
    timestamp: float
    total_input_tokens: float = Field(alias="totalInputTokens")
    total_output_tokens: float = Field(alias="totalOutputTokens")


class V1TaskMetricsEventDataDict(TypedDict):
    ai_generation_count: float
    ai_generation_error_count: float
    event_counts: dict[str, float]
    iteration_id: str
    step_count: float
    timestamp: float
    total_input_tokens: float
    total_output_tokens: float

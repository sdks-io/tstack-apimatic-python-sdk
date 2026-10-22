from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1ValidationErrorEventData(SdkBaseModel):
    """Event data for validation errors during action response processing"""

    errors: list[str]
    iteration_id: str = Field(alias="iterationId")
    raw_response: Any = Field(alias="rawResponse")
    retry_count: float = Field(alias="retryCount")
    timestamp: float


class V1ValidationErrorEventDataDict(TypedDict):
    errors: list[str]
    iteration_id: str
    raw_response: Any
    retry_count: float
    timestamp: float

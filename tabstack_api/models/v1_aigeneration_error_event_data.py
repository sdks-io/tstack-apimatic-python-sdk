from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1AigenerationErrorEventData(SdkBaseModel):
    """Event data when AI generation error occurs"""

    error: str
    iteration_id: str = Field(alias="iterationId")
    messages: Optional[list[Any]] = UNSET
    prompt: str
    schema_value: Any = Field(alias="schema")
    timestamp: float


class V1AigenerationErrorEventDataDict(TypedDict):
    error: str
    iteration_id: str
    messages: NotRequired[list[Any]]
    prompt: str
    schema_value: Any
    timestamp: float

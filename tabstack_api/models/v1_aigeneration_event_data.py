from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.finish_reason import FinishReasonOrStr
from .unions.message import Message, MessageDict
from .usage import Usage, UsageDict


class V1AigenerationEventData(SdkBaseModel):
    """Event data when AI generation occurs"""

    finish_reason: FinishReasonOrStr = Field(alias="finishReason")
    iteration_id: str = Field(alias="iterationId")
    messages: Optional[list[Message]] = UNSET
    object_: Optional[Any] = Field(default=UNSET, alias="object")
    prompt: str
    provider_metadata: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerMetadata")
    schema_value: Any = Field(alias="schema")
    temperature: Optional[float] = UNSET
    timestamp: float
    usage: Usage
    warnings: Optional[list[Any]] = UNSET


class V1AigenerationEventDataDict(TypedDict):
    finish_reason: FinishReasonOrStr
    iteration_id: str
    messages: NotRequired[list[MessageDict]]
    object_: NotRequired[Any]
    prompt: str
    provider_metadata: NotRequired[dict[str, Any]]
    schema_value: Any
    temperature: NotRequired[float]
    timestamp: float
    usage: UsageDict
    warnings: NotRequired[list[Any]]

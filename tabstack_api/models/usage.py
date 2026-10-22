from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Usage(SdkBaseModel):
    input_tokens: Optional[float] = Field(default=UNSET, alias="inputTokens")
    output_tokens: Optional[float] = Field(default=UNSET, alias="outputTokens")
    total_tokens: Optional[float] = Field(default=UNSET, alias="totalTokens")


class UsageDict(TypedDict):
    input_tokens: NotRequired[float]
    output_tokens: NotRequired[float]
    total_tokens: NotRequired[float]

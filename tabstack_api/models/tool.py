from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.content11 import Content11, Content11Dict


class Tool(SdkBaseModel):
    """A tool message. It contains the result of one or more tool calls."""

    content: list[Content11]
    """Content of a tool message. It is an array of tool result parts."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Additional provider-specific metadata. They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider."""

    role: str


class ToolDict(TypedDict):
    content: list[Content11Dict]
    provider_options: NotRequired[dict[str, Any]]
    role: str

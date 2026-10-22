from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.content21 import Content21, Content21Dict


class Assistant(SdkBaseModel):
    """An assistant message. It can contain text, tool calls, or a combination of text and tool calls."""

    content: Content21
    """Content of an assistant message. It can be a string or an array of text, image, reasoning, redacted reasoning,
    and tool call parts."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Additional provider-specific metadata. They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider."""

    role: str


class AssistantDict(TypedDict):
    content: Content21Dict
    provider_options: NotRequired[dict[str, Any]]
    role: str

from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.output import Output, OutputDict


class ToolResult(SdkBaseModel):
    """Tool result content part of a prompt. It contains the result of the tool call with the matching ID."""

    output: Output
    """Result of the tool call. This is a JSON-serializable object."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Additional provider-specific metadata. They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider."""

    tool_call_id: str = Field(alias="toolCallId")
    """ID of the tool call that this result is associated with."""

    tool_name: str = Field(alias="toolName")
    """Name of the tool that generated this result."""

    type_: str = Field(alias="type")


class ToolResultDict(TypedDict):
    output: OutputDict
    provider_options: NotRequired[dict[str, Any]]
    tool_call_id: str
    tool_name: str
    type_: str

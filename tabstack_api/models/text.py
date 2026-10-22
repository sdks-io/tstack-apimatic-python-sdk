from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Text(SdkBaseModel):
    """Text content part of a prompt. It contains a string of text."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Additional provider-specific metadata. They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider."""

    text: str
    """The text content."""

    type_: str = Field(alias="type")


class TextDict(TypedDict):
    provider_options: NotRequired[dict[str, Any]]
    text: str
    type_: str

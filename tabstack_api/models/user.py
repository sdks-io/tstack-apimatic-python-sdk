from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.content3 import Content3, Content3Dict


class User(SdkBaseModel):
    """A user message. It can contain text or a combination of text and images."""

    content: Content3
    """Content of a user message. It can be a string or an array of text and image parts."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Additional provider-specific metadata. They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider."""

    role: str


class UserDict(TypedDict):
    content: Content3Dict
    provider_options: NotRequired[dict[str, Any]]
    role: str

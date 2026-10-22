from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class System(SdkBaseModel):
    """A system message. It can contain system information.

    Note: using the "system" part of the prompt is strongly preferred to increase the resilience against prompt
    injection attacks, and because not all providers support several system messages."""

    content: str
    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Additional provider-specific metadata. They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider."""

    role: str


class SystemDict(TypedDict):
    content: str
    provider_options: NotRequired[dict[str, Any]]
    role: str

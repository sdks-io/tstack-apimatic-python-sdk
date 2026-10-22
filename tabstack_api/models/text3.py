from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Text3(SdkBaseModel):
    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Provider-specific options."""

    text: str
    """Text content."""

    type_: str = Field(alias="type")


class Text3Dict(TypedDict):
    provider_options: NotRequired[dict[str, Any]]
    text: str
    type_: str

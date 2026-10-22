from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Text2(SdkBaseModel):
    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Provider-specific options."""

    type_: str = Field(alias="type")
    """Text tool output that should be directly sent to the API."""

    value: str


class Text2Dict(TypedDict):
    provider_options: NotRequired[dict[str, Any]]
    type_: str
    value: str

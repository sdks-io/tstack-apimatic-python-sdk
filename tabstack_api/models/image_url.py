from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ImageUrl(SdkBaseModel):
    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Provider-specific options."""

    type_: str = Field(alias="type")
    """Images that are referenced using a URL."""

    url: str
    """URL of the image."""


class ImageUrlDict(TypedDict):
    provider_options: NotRequired[dict[str, Any]]
    type_: str
    url: str

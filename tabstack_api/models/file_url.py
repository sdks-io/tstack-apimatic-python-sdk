from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FileUrl(SdkBaseModel):
    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Provider-specific options."""

    type_: str = Field(alias="type")
    url: str
    """URL of the file."""


class FileUrlDict(TypedDict):
    provider_options: NotRequired[dict[str, Any]]
    type_: str
    url: str

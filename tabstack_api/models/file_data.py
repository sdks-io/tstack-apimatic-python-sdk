from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FileData(SdkBaseModel):
    data: str
    """Base-64 encoded media data."""

    filename: Optional[str] = UNSET
    """Optional filename of the file."""

    media_type: str = Field(alias="mediaType")
    """IANA media type."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Provider-specific options."""

    type_: str = Field(alias="type")


class FileDataDict(TypedDict):
    data: str
    filename: NotRequired[str]
    media_type: str
    provider_options: NotRequired[dict[str, Any]]
    type_: str

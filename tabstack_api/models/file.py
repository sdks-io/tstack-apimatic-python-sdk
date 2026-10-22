from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.data import Data, DataDict


class File(SdkBaseModel):
    """File content part of a prompt. It contains a file."""

    data: Data
    """File data. Can either be:

    - data: a base64-encoded string, a Uint8Array, an ArrayBuffer, or a Buffer
    - URL: a URL that points to the image"""

    filename: Optional[str] = UNSET
    """Optional filename of the file."""

    media_type: str = Field(alias="mediaType")
    """IANA media type of the file."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Additional provider-specific metadata. They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider."""

    type_: str = Field(alias="type")


class FileDict(TypedDict):
    data: DataDict
    filename: NotRequired[str]
    media_type: str
    provider_options: NotRequired[dict[str, Any]]
    type_: str

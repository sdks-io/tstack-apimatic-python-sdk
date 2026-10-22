from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.image1 import Image1, Image1Dict


class Image(SdkBaseModel):
    """Image content part of a prompt. It contains an image."""

    image: Image1
    """Image data. Can either be:

    - data: a base64-encoded string, a Uint8Array, an ArrayBuffer, or a Buffer
    - URL: a URL that points to the image"""

    media_type: Optional[str] = Field(default=UNSET, alias="mediaType")
    """Optional IANA media type of the image."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Additional provider-specific metadata. They are passed through to the provider from the AI SDK and enable
    provider-specific functionality that can be fully encapsulated in the provider."""

    type_: str = Field(alias="type")


class ImageDict(TypedDict):
    image: Image1Dict
    media_type: NotRequired[str]
    provider_options: NotRequired[dict[str, Any]]
    type_: str

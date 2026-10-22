from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Media(SdkBaseModel):
    data: str
    media_type: str = Field(alias="mediaType")
    type_: str = Field(alias="type")
    """Deprecated. Use image-data or file-data instead."""


class MediaDict(TypedDict):
    data: str
    media_type: str
    type_: str

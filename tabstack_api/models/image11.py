from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Image11(SdkBaseModel):
    byte_length: float = Field(alias="byteLength")


class Image11Dict(TypedDict):
    byte_length: float

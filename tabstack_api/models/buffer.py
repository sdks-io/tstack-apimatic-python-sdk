from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Buffer(SdkBaseModel):
    byte_length: float = Field(alias="byteLength")


class BufferDict(TypedDict):
    byte_length: float

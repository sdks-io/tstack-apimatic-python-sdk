from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .buffer import Buffer, BufferDict


class V1GlobalBuffer(SdkBaseModel):
    bytes_per_element: float = Field(alias="BYTES_PER_ELEMENT")
    buffer: Buffer
    byte_length: float = Field(alias="byteLength")
    byte_offset: float = Field(alias="byteOffset")
    length: float


class V1GlobalBufferDict(TypedDict):
    bytes_per_element: float
    buffer: BufferDict
    byte_length: float
    byte_offset: float
    length: float

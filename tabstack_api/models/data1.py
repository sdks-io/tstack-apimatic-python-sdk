from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data1(SdkBaseModel):
    byte_length: float = Field(alias="byteLength")


class Data1Dict(TypedDict):
    byte_length: float

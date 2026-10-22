from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.value4 import Value4, Value4Dict


class Content(SdkBaseModel):
    type_: str = Field(alias="type")
    value: list[Value4]


class ContentDict(TypedDict):
    type_: str
    value: list[Value4Dict]

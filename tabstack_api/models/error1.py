from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Error1(SdkBaseModel):
    message: str
    name: str
    stack: Optional[str] = UNSET


class Error1Dict(TypedDict):
    message: str
    name: str
    stack: NotRequired[str]

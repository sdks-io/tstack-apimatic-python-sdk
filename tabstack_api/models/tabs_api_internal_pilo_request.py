from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TabsApiInternalPiloRequest(SdkBaseModel):
    data: Optional[Any] = UNSET


class TabsApiInternalPiloRequestDict(TypedDict):
    data: NotRequired[Any]

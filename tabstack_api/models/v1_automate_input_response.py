from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1AutomateInputResponse(SdkBaseModel):
    status: Optional[str] = UNSET


class V1AutomateInputResponseDict(TypedDict):
    status: NotRequired[str]

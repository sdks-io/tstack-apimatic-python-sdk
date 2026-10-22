from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1AutomateInputFieldValue(SdkBaseModel):
    ref: Optional[str] = UNSET
    value: Optional[str] = UNSET


class V1AutomateInputFieldValueDict(TypedDict):
    ref: NotRequired[str]
    value: NotRequired[str]

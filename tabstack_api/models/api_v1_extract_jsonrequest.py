from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApiV1ExtractJsonrequest(SdkBaseModel):
    effort: Optional[Any] = UNSET
    json_schema: Optional[Any] = UNSET


class ApiV1ExtractJsonrequestDict(TypedDict):
    effort: NotRequired[Any]
    json_schema: NotRequired[Any]

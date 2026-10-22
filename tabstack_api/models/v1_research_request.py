from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.mode import Mode, ModeOrStr


class V1ResearchRequest(SdkBaseModel):
    fetch_timeout: Optional[int] = UNSET
    """Timeout in seconds for fetching web pages"""

    mode: ModeOrStr = Mode.FAST
    """Research mode: fast (quick answers, default), balanced (standard research)"""

    nocache: Optional[bool] = UNSET
    """Skip cache and force fresh research"""

    query: str
    """The research query or question to answer. Maximum 10,000 characters."""


class V1ResearchRequestDict(TypedDict):
    fetch_timeout: NotRequired[int]
    mode: NotRequired[ModeOrStr]
    nocache: NotRequired[bool]
    query: str

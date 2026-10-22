from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.content2 import Content2, Content2OrStr
from .enums.effort import Effort, EffortOrStr
from .geotarget_geo_target import GeotargetGeoTarget, GeotargetGeoTargetDict


class V1ExtractMarkdownRequest(SdkBaseModel):
    content: Content2OrStr = Content2.MAIN
    """Content scope. "main" (default) returns the main article content; "full" returns the whole page, including
    navigation, footer, and links."""

    effort: EffortOrStr = Effort.STANDARD
    """Fetch effort level controlling speed vs. capability tradeoff. "min": fastest, no fallback (1-5s). "standard":
    balanced with enhanced reliability (default, 3-15s). "max": full browser rendering for JS-heavy sites (15-60s)."""

    geo_target: Optional[GeotargetGeoTarget] = UNSET
    """Optional geotargeting parameters for proxy requests"""

    metadata: bool = False
    """Include extracted metadata (Open Graph and HTML metadata) as a separate field in the response"""

    nocache: bool = False
    """Bypass cache and force fresh data retrieval"""

    url: str
    """URL to fetch and convert to markdown"""


class V1ExtractMarkdownRequestDict(TypedDict):
    content: NotRequired[Content2OrStr]
    effort: NotRequired[EffortOrStr]
    geo_target: NotRequired[GeotargetGeoTargetDict]
    metadata: NotRequired[bool]
    nocache: NotRequired[bool]
    url: str

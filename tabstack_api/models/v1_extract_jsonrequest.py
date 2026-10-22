from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.effort import Effort, EffortOrStr
from .geotarget_geo_target import GeotargetGeoTarget, GeotargetGeoTargetDict


class V1ExtractJsonrequest(SdkBaseModel):
    effort: EffortOrStr = Effort.STANDARD
    """Fetch effort level controlling speed vs. capability tradeoff. "min": fastest, no fallback (1-5s). "standard":
    balanced with enhanced reliability (default, 3-15s). "max": full browser rendering for JS-heavy sites (15-60s)."""

    geo_target: Optional[GeotargetGeoTarget] = UNSET
    """Optional geotargeting parameters for proxy requests"""

    json_schema: Any
    """JSON schema definition that describes the structure of data to extract. If the schema includes a "page_title" or
    "favicon" property, those fields are automatically filled from page metadata when the AI leaves them empty."""

    nocache: bool = False
    """Bypass cache and force fresh data retrieval"""

    url: str
    """URL to fetch and extract data from"""


class V1ExtractJsonrequestDict(TypedDict):
    effort: NotRequired[EffortOrStr]
    geo_target: NotRequired[GeotargetGeoTargetDict]
    json_schema: Any
    nocache: NotRequired[bool]
    url: str

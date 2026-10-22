from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.effort import Effort, EffortOrStr
from .geotarget_geo_target import GeotargetGeoTarget, GeotargetGeoTargetDict


class V1GenerateJsonrequest(SdkBaseModel):
    effort: EffortOrStr = Effort.STANDARD
    """Fetch effort level controlling speed vs. capability tradeoff. "min": fastest, no fallback (1-5s). "standard":
    balanced with enhanced reliability (default, 3-15s). "max": full browser rendering for JS-heavy sites (15-60s)."""

    geo_target: Optional[GeotargetGeoTarget] = UNSET
    """Optional geotargeting parameters for proxy requests"""

    instructions: str
    """Instructions describing how to transform the data. Maximum 20,000 characters."""

    json_schema: Any
    """JSON schema defining the structure of the transformed output"""

    nocache: bool = False
    """Bypass cache and force fresh data retrieval"""

    url: str
    """URL to fetch content from"""


class V1GenerateJsonrequestDict(TypedDict):
    effort: NotRequired[EffortOrStr]
    geo_target: NotRequired[GeotargetGeoTargetDict]
    instructions: str
    json_schema: Any
    nocache: NotRequired[bool]
    url: str

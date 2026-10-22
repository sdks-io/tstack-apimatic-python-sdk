from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GeotargetGeoTarget(SdkBaseModel):
    country: Optional[str] = UNSET
    """Country code using ISO 3166-1 alpha-2 standard (2 letters, e.g., "US", "GB", "JP"). See:
    https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"""


class GeotargetGeoTargetDict(TypedDict):
    country: NotRequired[str]

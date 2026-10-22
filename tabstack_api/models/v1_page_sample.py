from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.relevance import RelevanceOrStr
from .enums.reliability import ReliabilityOrStr
from .enums.v1_url_source import V1UrlSourceOrStr


class V1PageSample(SdkBaseModel):
    """Page sample - lightweight representation for event payloads"""

    domain: str
    relevance: Optional[RelevanceOrStr] = UNSET
    reliability: Optional[ReliabilityOrStr] = UNSET
    summary: Optional[str] = UNSET
    title: str
    url: str
    url_source: V1UrlSourceOrStr = Field(alias="urlSource")
    """URL source tracking - where a URL came from"""


class V1PageSampleDict(TypedDict):
    domain: str
    relevance: NotRequired[RelevanceOrStr]
    reliability: NotRequired[ReliabilityOrStr]
    summary: NotRequired[str]
    title: str
    url: str
    url_source: V1UrlSourceOrStr

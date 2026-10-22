from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.relevance import RelevanceOrStr
from .enums.reliability import ReliabilityOrStr
from .enums.v1_url_source import V1UrlSourceOrStr


class CitedPage(SdkBaseModel):
    claims: list[str]
    depth: Optional[float] = UNSET
    full_text: Optional[str] = Field(default=UNSET, alias="fullText")
    """Full page text (fetched markdown or search excerpts). Only populated when ``includeFullText: true`` in
    ResearchOptions.
    - Fast mode: Parallel API excerpts (~5000 chars)
    - Other modes: Fetched page markdown"""

    id: str
    parent_url: Optional[str] = Field(default=UNSET, alias="parentUrl")
    relevance: Optional[RelevanceOrStr] = UNSET
    reliability: Optional[ReliabilityOrStr] = UNSET
    source_queries: list[str] = Field(alias="sourceQueries")
    summary: Optional[str] = UNSET
    """LLM-generated summary. Undefined in fast mode (no content analysis)."""

    title: Optional[str] = UNSET
    url: str
    url_source: Optional[V1UrlSourceOrStr] = Field(default=UNSET, alias="urlSource")
    """URL source tracking - where a URL came from"""


class CitedPageDict(TypedDict):
    claims: list[str]
    depth: NotRequired[float]
    full_text: NotRequired[str]
    id: str
    parent_url: NotRequired[str]
    relevance: NotRequired[RelevanceOrStr]
    reliability: NotRequired[ReliabilityOrStr]
    source_queries: list[str]
    summary: NotRequired[str]
    title: NotRequired[str]
    url: str
    url_source: NotRequired[V1UrlSourceOrStr]

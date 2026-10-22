from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_research_metadata import V1ResearchMetadata, V1ResearchMetadataDict


class V1CompleteEvent(SdkBaseModel):
    """complete - Research finished successfully"""

    message: str
    metadata: V1ResearchMetadata
    """Research metadata

    Note: citedPages, gapEvaluations, outline, and judgments are optional to support fast mode, which skips these phases
    for maximum speed."""

    report: str
    timestamp: float


class V1CompleteEventDict(TypedDict):
    message: str
    metadata: V1ResearchMetadataDict
    report: str
    timestamp: float

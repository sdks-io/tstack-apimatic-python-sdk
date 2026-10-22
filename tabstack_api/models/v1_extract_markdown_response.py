from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagemetadata_metadata import PagemetadataMetadata, PagemetadataMetadataDict


class V1ExtractMarkdownResponse(SdkBaseModel):
    content: str
    """The markdown content (includes metadata as YAML frontmatter by default)"""

    metadata: Optional[PagemetadataMetadata] = UNSET
    """Extracted metadata from the page (only included when metadata parameter is true)"""

    url: str
    """The URL that was converted to markdown"""


class V1ExtractMarkdownResponseDict(TypedDict):
    content: str
    metadata: NotRequired[PagemetadataMetadataDict]
    url: str

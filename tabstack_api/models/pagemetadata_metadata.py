from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PagemetadataMetadata(SdkBaseModel):
    author: Optional[str] = UNSET
    """Author information from HTML metadata"""

    created_at: Optional[str] = UNSET
    """Document creation date (ISO 8601)"""

    creator: Optional[str] = UNSET
    """Creator application (e.g., "Microsoft Word")"""

    description: Optional[str] = UNSET
    """Page description from Open Graph or HTML"""

    favicon: Optional[str] = UNSET
    """Favicon URL (resolved to absolute) parsed from <link rel="icon"> / "shortcut icon" / "apple-touch-icon"
    """

    image: Optional[str] = UNSET
    """Featured image URL from Open Graph"""

    keywords: Optional[list[str]] = UNSET
    """PDF keywords as array"""

    modified_at: Optional[str] = UNSET
    """Document modification date (ISO 8601)"""

    page_count: Optional[int] = UNSET
    """Number of pages (PDF documents)"""

    pdf_version: Optional[str] = UNSET
    """PDF version (e.g., "1.5")"""

    producer: Optional[str] = UNSET
    """PDF producer software (e.g., "Adobe PDF Library")"""

    publisher: Optional[str] = UNSET
    """Publisher information from Open Graph"""

    site_name: Optional[str] = UNSET
    """Site name from Open Graph"""

    subject: Optional[str] = UNSET
    """PDF-specific metadata fields (populated for PDF documents) PDF subject or summary"""

    title: Optional[str] = UNSET
    """Page title from Open Graph or HTML"""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Content type from Open Graph (e.g., article, website)"""

    url: Optional[str] = UNSET
    """Canonical URL from Open Graph"""


class PagemetadataMetadataDict(TypedDict):
    author: NotRequired[str]
    created_at: NotRequired[str]
    creator: NotRequired[str]
    description: NotRequired[str]
    favicon: NotRequired[str]
    image: NotRequired[str]
    keywords: NotRequired[list[str]]
    modified_at: NotRequired[str]
    page_count: NotRequired[int]
    pdf_version: NotRequired[str]
    producer: NotRequired[str]
    publisher: NotRequired[str]
    site_name: NotRequired[str]
    subject: NotRequired[str]
    title: NotRequired[str]
    type_: NotRequired[str]
    url: NotRequired[str]

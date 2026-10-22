from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UrlSources(SdkBaseModel):
    extracted_links: float = Field(alias="extractedLinks")
    search_results: float = Field(alias="searchResults")
    user_provided: float = Field(alias="userProvided")


class UrlSourcesDict(TypedDict):
    extracted_links: float
    search_results: float
    user_provided: float

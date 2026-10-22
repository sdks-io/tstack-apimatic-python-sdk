from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1ResearchOutline(SdkBaseModel):
    """Report outline from research writer"""

    direct_answer: str = Field(alias="directAnswer")
    key_takeaways: list[str] = Field(alias="keyTakeaways")
    outline: str
    relevant_source_ids: list[str] = Field(alias="relevantSourceIds")


class V1ResearchOutlineDict(TypedDict):
    direct_answer: str
    key_takeaways: list[str]
    outline: str
    relevant_source_ids: list[str]

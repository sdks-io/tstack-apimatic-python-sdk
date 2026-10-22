from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1ExtractedDataEventData(SdkBaseModel):
    """Event data for extracted data"""

    extracted_data: str = Field(alias="extractedData")
    iteration_id: str = Field(alias="iterationId")
    timestamp: float


class V1ExtractedDataEventDataDict(TypedDict):
    extracted_data: str
    iteration_id: str
    timestamp: float

from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_form_field_request import V1FormFieldRequest, V1FormFieldRequestDict


class V1InteractiveFormDataRequestEventData(SdkBaseModel):
    """Event data when the agent requests user data for form fields"""

    fields: list[V1FormFieldRequest]
    form_description: str = Field(alias="formDescription")
    iteration_id: str = Field(alias="iterationId")
    page_title: str = Field(alias="pageTitle")
    page_url: str = Field(alias="pageUrl")
    request_id: str = Field(alias="requestId")
    timestamp: float


class V1InteractiveFormDataRequestEventDataDict(TypedDict):
    fields: list[V1FormFieldRequestDict]
    form_description: str
    iteration_id: str
    page_title: str
    page_url: str
    request_id: str
    timestamp: float

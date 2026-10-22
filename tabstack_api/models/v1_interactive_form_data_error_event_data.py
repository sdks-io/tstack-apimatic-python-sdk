from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_form_field_request import V1FormFieldRequest, V1FormFieldRequestDict


class V1InteractiveFormDataErrorEventData(SdkBaseModel):
    """Event data when form validation fails and the agent re-requests data. Carries both the error context and the
    fields that need new values. Callers respond to this the same way as a request event."""

    field_errors: dict[str, str] = Field(alias="fieldErrors")
    """Per-field error messages from validation (field ref -> error text)"""

    fields: list[V1FormFieldRequest]
    form_description: str = Field(alias="formDescription")
    iteration_id: str = Field(alias="iterationId")
    page_title: str = Field(alias="pageTitle")
    page_url: str = Field(alias="pageUrl")
    request_id: str = Field(alias="requestId")
    timestamp: float


class V1InteractiveFormDataErrorEventDataDict(TypedDict):
    field_errors: dict[str, str]
    fields: list[V1FormFieldRequestDict]
    form_description: str
    iteration_id: str
    page_title: str
    page_url: str
    request_id: str
    timestamp: float

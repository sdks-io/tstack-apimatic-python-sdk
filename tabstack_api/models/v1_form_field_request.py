from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.field_type import FieldTypeOrStr


class V1FormFieldRequest(SdkBaseModel):
    """A single form field the agent needs data for."""

    current_value: Optional[str] = Field(default=UNSET, alias="currentValue")
    """Current value if already partially filled"""

    description: Optional[str] = UNSET
    """Additional context (e.g., validation error message on re-request)"""

    field_type: FieldTypeOrStr = Field(alias="fieldType")
    """Semantic field type"""

    label: str
    """The field's visible label"""

    options: Optional[list[str]] = UNSET
    """Available options for select/radio fields"""

    ref: str
    """Element ref from the accessibility tree (e.g., "E42")"""

    required: bool
    """Whether this field must be filled"""


class V1FormFieldRequestDict(TypedDict):
    current_value: NotRequired[str]
    description: NotRequired[str]
    field_type: FieldTypeOrStr
    label: str
    options: NotRequired[list[str]]
    ref: str
    required: bool

from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.value import Value, ValueDict


class ErrorJson(SdkBaseModel):
    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Provider-specific options."""

    type_: str = Field(alias="type")
    value: Value
    """A JSON value can be a string, number, boolean, object, array, or null. JSON values can be serialized and
    deserialized by the JSON.stringify and JSON.parse methods."""


class ErrorJsonDict(TypedDict):
    provider_options: NotRequired[dict[str, Any]]
    type_: str
    value: ValueDict

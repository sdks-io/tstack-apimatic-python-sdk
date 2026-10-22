from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExecutionDenied(SdkBaseModel):
    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Provider-specific options."""

    reason: Optional[str] = UNSET
    """Optional reason for the execution denial."""

    type_: str = Field(alias="type")
    """Type when the user has denied the execution of the tool call."""


class ExecutionDeniedDict(TypedDict):
    provider_options: NotRequired[dict[str, Any]]
    reason: NotRequired[str]
    type_: str

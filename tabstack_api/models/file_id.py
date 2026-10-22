from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.file_id1 import FileId1, FileId1Dict


class FileId(SdkBaseModel):
    file_id: FileId1 = Field(alias="fileId")
    """ID of the file.

    If you use multiple providers, you need to specify the provider specific ids using the Record option. The key is the
    provider name, e.g. 'openai' or 'anthropic'."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Provider-specific options."""

    type_: str = Field(alias="type")


class FileIdDict(TypedDict):
    file_id: FileId1Dict
    provider_options: NotRequired[dict[str, Any]]
    type_: str

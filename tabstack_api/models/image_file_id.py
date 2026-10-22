from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.file_id11 import FileId11, FileId11Dict


class ImageFileId(SdkBaseModel):
    file_id: FileId11 = Field(alias="fileId")
    """Image that is referenced using a provider file id.

    If you use multiple providers, you need to specify the provider specific ids using the Record option. The key is the
    provider name, e.g. 'openai' or 'anthropic'."""

    provider_options: Optional[dict[str, Any]] = Field(default=UNSET, alias="providerOptions")
    """Provider-specific options."""

    type_: str = Field(alias="type")
    """Images that are referenced using a provider file id."""


class ImageFileIdDict(TypedDict):
    file_id: FileId11Dict
    provider_options: NotRequired[dict[str, Any]]
    type_: str

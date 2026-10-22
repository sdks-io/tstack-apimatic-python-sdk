from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.key_source import KeySourceOrStr


class V1TaskSetupEventData(SdkBaseModel):
    """Event data when a task is setup"""

    browser_name: str = Field(alias="browserName")
    data: Optional[Any] = UNSET
    guardrails: Optional[str] = UNSET
    has_api_key: Optional[bool] = Field(default=UNSET, alias="hasApiKey")
    iteration_id: str = Field(alias="iterationId")
    key_source: Optional[KeySourceOrStr] = Field(default=UNSET, alias="keySource")
    model: Optional[str] = UNSET
    provider: Optional[str] = UNSET
    proxy: Optional[str] = UNSET
    pw_cdp_endpoint: Optional[str] = Field(default=UNSET, alias="pwCdpEndpoint")
    pw_cdp_endpoint_count: Optional[float] = Field(default=UNSET, alias="pwCdpEndpointCount")
    """Total number of CDP endpoints configured (index, not URLs)"""

    pw_cdp_endpoints: Optional[list[str]] = Field(default=UNSET, alias="pwCdpEndpoints")
    pw_endpoint: Optional[str] = Field(default=UNSET, alias="pwEndpoint")
    task: str
    timestamp: float
    url: Optional[str] = UNSET
    vision: Optional[bool] = UNSET


class V1TaskSetupEventDataDict(TypedDict):
    browser_name: str
    data: NotRequired[Any]
    guardrails: NotRequired[str]
    has_api_key: NotRequired[bool]
    iteration_id: str
    key_source: NotRequired[KeySourceOrStr]
    model: NotRequired[str]
    provider: NotRequired[str]
    proxy: NotRequired[str]
    pw_cdp_endpoint: NotRequired[str]
    pw_cdp_endpoint_count: NotRequired[float]
    pw_cdp_endpoints: NotRequired[list[str]]
    pw_endpoint: NotRequired[str]
    task: str
    timestamp: float
    url: NotRequired[str]
    vision: NotRequired[bool]

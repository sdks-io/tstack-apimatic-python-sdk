from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .geotarget_geo_target import GeotargetGeoTarget, GeotargetGeoTargetDict


class V1AutomateRequest(SdkBaseModel):
    data: Optional[Any] = UNSET
    """JSON data to provide context for form filling or complex tasks"""

    geo_target: Optional[GeotargetGeoTarget] = UNSET
    """Optional geotargeting parameters for proxy requests"""

    guardrails: Optional[str] = UNSET
    """Safety constraints for execution"""

    interactive: bool = False
    """Enable interactive mode to allow human-in-the-loop input during task execution"""

    max_iterations: int = Field(default=50, alias="maxIterations")
    """Maximum task iterations"""

    max_validation_attempts: int = Field(default=3, alias="maxValidationAttempts")
    """Maximum validation attempts"""

    task: str
    """The task description in natural language"""

    trusted_hostnames: Optional[list[str]] = UNSET
    """TrustedHostnames lists hostnames where the action firewall is bypassed for fills and submissions. WARNING: on
    listed hosts, prompt injection from page content can drive the agent to fill and submit any field, including
    personal and credential data. Use only for sites you fully trust to receive your data."""

    unsafe_mode: bool = False
    """UnsafeMode disables the action firewall entirely. WARNING: prompt injection from page content can then cause the
    agent to submit your data, including credentials, personal information, and conversation context, to
    attacker-controlled forms. Only enable for trusted, controlled environments."""

    url: Optional[str] = UNSET
    """Starting URL for the task"""


class V1AutomateRequestDict(TypedDict):
    data: NotRequired[Any]
    geo_target: NotRequired[GeotargetGeoTargetDict]
    guardrails: NotRequired[str]
    interactive: NotRequired[bool]
    max_iterations: NotRequired[int]
    max_validation_attempts: NotRequired[int]
    task: str
    trusted_hostnames: NotRequired[list[str]]
    unsafe_mode: NotRequired[bool]
    url: NotRequired[str]

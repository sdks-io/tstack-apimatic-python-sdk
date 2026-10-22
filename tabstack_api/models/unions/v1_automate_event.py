from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..v1_automate_event_agent_action import V1AutomateEventAgentAction, V1AutomateEventAgentActionDict
from ..v1_automate_event_agent_extracted import V1AutomateEventAgentExtracted, V1AutomateEventAgentExtractedDict
from ..v1_automate_event_agent_processing import V1AutomateEventAgentProcessing, V1AutomateEventAgentProcessingDict
from ..v1_automate_event_agent_reasoned import V1AutomateEventAgentReasoned, V1AutomateEventAgentReasonedDict
from ..v1_automate_event_agent_status import V1AutomateEventAgentStatus, V1AutomateEventAgentStatusDict
from ..v1_automate_event_agent_step import V1AutomateEventAgentStep, V1AutomateEventAgentStepDict
from ..v1_automate_event_agent_waiting import V1AutomateEventAgentWaiting, V1AutomateEventAgentWaitingDict
from ..v1_automate_event_ai_generation import V1AutomateEventAiGeneration, V1AutomateEventAiGenerationDict
from ..v1_automate_event_ai_generation_error import (
    V1AutomateEventAiGenerationError,
    V1AutomateEventAiGenerationErrorDict,
)
from ..v1_automate_event_browser_action_completed import (
    V1AutomateEventBrowserActionCompleted,
    V1AutomateEventBrowserActionCompletedDict,
)
from ..v1_automate_event_browser_action_started import (
    V1AutomateEventBrowserActionStarted,
    V1AutomateEventBrowserActionStartedDict,
)
from ..v1_automate_event_browser_navigated import V1AutomateEventBrowserNavigated, V1AutomateEventBrowserNavigatedDict
from ..v1_automate_event_browser_reconnected import (
    V1AutomateEventBrowserReconnected,
    V1AutomateEventBrowserReconnectedDict,
)
from ..v1_automate_event_browser_screenshot_captured import (
    V1AutomateEventBrowserScreenshotCaptured,
    V1AutomateEventBrowserScreenshotCapturedDict,
)
from ..v1_automate_event_browser_screenshot_captured_image import (
    V1AutomateEventBrowserScreenshotCapturedImage,
    V1AutomateEventBrowserScreenshotCapturedImageDict,
)
from ..v1_automate_event_cdp_endpoint_connected import (
    V1AutomateEventCdpEndpointConnected,
    V1AutomateEventCdpEndpointConnectedDict,
)
from ..v1_automate_event_cdp_endpoint_cycle import V1AutomateEventCdpEndpointCycle, V1AutomateEventCdpEndpointCycleDict
from ..v1_automate_event_complete import V1AutomateEventComplete, V1AutomateEventCompleteDict
from ..v1_automate_event_done import V1AutomateEventDone, V1AutomateEventDoneDict
from ..v1_automate_event_error import V1AutomateEventError, V1AutomateEventErrorDict
from ..v1_automate_event_interactive_form_data_error import (
    V1AutomateEventInteractiveFormDataError,
    V1AutomateEventInteractiveFormDataErrorDict,
)
from ..v1_automate_event_interactive_form_data_request import (
    V1AutomateEventInteractiveFormDataRequest,
    V1AutomateEventInteractiveFormDataRequestDict,
)
from ..v1_automate_event_system_debug_compression import (
    V1AutomateEventSystemDebugCompression,
    V1AutomateEventSystemDebugCompressionDict,
)
from ..v1_automate_event_system_debug_message import (
    V1AutomateEventSystemDebugMessage,
    V1AutomateEventSystemDebugMessageDict,
)
from ..v1_automate_event_task_aborted import V1AutomateEventTaskAborted, V1AutomateEventTaskAbortedDict
from ..v1_automate_event_task_completed import V1AutomateEventTaskCompleted, V1AutomateEventTaskCompletedDict
from ..v1_automate_event_task_metrics import V1AutomateEventTaskMetrics, V1AutomateEventTaskMetricsDict
from ..v1_automate_event_task_metrics_incremental import (
    V1AutomateEventTaskMetricsIncremental,
    V1AutomateEventTaskMetricsIncrementalDict,
)
from ..v1_automate_event_task_setup import V1AutomateEventTaskSetup, V1AutomateEventTaskSetupDict
from ..v1_automate_event_task_started import V1AutomateEventTaskStarted, V1AutomateEventTaskStartedDict
from ..v1_automate_event_task_trace_context import V1AutomateEventTaskTraceContext, V1AutomateEventTaskTraceContextDict
from ..v1_automate_event_task_validated import V1AutomateEventTaskValidated, V1AutomateEventTaskValidatedDict
from ..v1_automate_event_task_validation_error import (
    V1AutomateEventTaskValidationError,
    V1AutomateEventTaskValidationErrorDict,
)

V1AutomateEvent: TypeAlias = Annotated[
    (
        Annotated[V1AutomateEventAgentAction, Tag("agent:action")]
        | Annotated[V1AutomateEventAgentExtracted, Tag("agent:extracted")]
        | Annotated[V1AutomateEventAgentProcessing, Tag("agent:processing")]
        | Annotated[V1AutomateEventAgentReasoned, Tag("agent:reasoned")]
        | Annotated[V1AutomateEventAgentStatus, Tag("agent:status")]
        | Annotated[V1AutomateEventAgentStep, Tag("agent:step")]
        | Annotated[V1AutomateEventAgentWaiting, Tag("agent:waiting")]
        | Annotated[V1AutomateEventAiGeneration, Tag("ai:generation")]
        | Annotated[V1AutomateEventAiGenerationError, Tag("ai:generation:error")]
        | Annotated[V1AutomateEventBrowserActionCompleted, Tag("browser:action_completed")]
        | Annotated[V1AutomateEventBrowserActionStarted, Tag("browser:action_started")]
        | Annotated[V1AutomateEventBrowserNavigated, Tag("browser:navigated")]
        | Annotated[V1AutomateEventBrowserReconnected, Tag("browser:reconnected")]
        | Annotated[V1AutomateEventBrowserScreenshotCaptured, Tag("browser:screenshot_captured")]
        | Annotated[V1AutomateEventBrowserScreenshotCapturedImage, Tag("browser:screenshot_captured_image")]
        | Annotated[V1AutomateEventCdpEndpointConnected, Tag("cdp:endpoint_connected")]
        | Annotated[V1AutomateEventCdpEndpointCycle, Tag("cdp:endpoint_cycle")]
        | Annotated[V1AutomateEventComplete, Tag("complete")]
        | Annotated[V1AutomateEventDone, Tag("done")]
        | Annotated[V1AutomateEventError, Tag("error")]
        | Annotated[V1AutomateEventInteractiveFormDataError, Tag("interactive:form_data:error")]
        | Annotated[V1AutomateEventInteractiveFormDataRequest, Tag("interactive:form_data:request")]
        | Annotated[V1AutomateEventSystemDebugCompression, Tag("system:debug_compression")]
        | Annotated[V1AutomateEventSystemDebugMessage, Tag("system:debug_message")]
        | Annotated[V1AutomateEventTaskAborted, Tag("task:aborted")]
        | Annotated[V1AutomateEventTaskCompleted, Tag("task:completed")]
        | Annotated[V1AutomateEventTaskMetrics, Tag("task:metrics")]
        | Annotated[V1AutomateEventTaskMetricsIncremental, Tag("task:metrics_incremental")]
        | Annotated[V1AutomateEventTaskSetup, Tag("task:setup")]
        | Annotated[V1AutomateEventTaskStarted, Tag("task:started")]
        | Annotated[V1AutomateEventTaskTraceContext, Tag("task:trace_context")]
        | Annotated[V1AutomateEventTaskValidated, Tag("task:validated")]
        | Annotated[V1AutomateEventTaskValidationError, Tag("task:validation_error")]
    ),
    WireDiscriminator("event"),
]
"""A Server-Sent Event from /v1/automate. Typed discriminated union keyed on event."""

V1AutomateEventDict: TypeAlias = (
    V1AutomateEventAgentActionDict
    | V1AutomateEventAgentExtractedDict
    | V1AutomateEventAgentProcessingDict
    | V1AutomateEventAgentReasonedDict
    | V1AutomateEventAgentStatusDict
    | V1AutomateEventAgentStepDict
    | V1AutomateEventAgentWaitingDict
    | V1AutomateEventAiGenerationDict
    | V1AutomateEventAiGenerationErrorDict
    | V1AutomateEventBrowserActionCompletedDict
    | V1AutomateEventBrowserActionStartedDict
    | V1AutomateEventBrowserNavigatedDict
    | V1AutomateEventBrowserReconnectedDict
    | V1AutomateEventBrowserScreenshotCapturedDict
    | V1AutomateEventBrowserScreenshotCapturedImageDict
    | V1AutomateEventCdpEndpointConnectedDict
    | V1AutomateEventCdpEndpointCycleDict
    | V1AutomateEventCompleteDict
    | V1AutomateEventDoneDict
    | V1AutomateEventErrorDict
    | V1AutomateEventInteractiveFormDataErrorDict
    | V1AutomateEventInteractiveFormDataRequestDict
    | V1AutomateEventSystemDebugCompressionDict
    | V1AutomateEventSystemDebugMessageDict
    | V1AutomateEventTaskAbortedDict
    | V1AutomateEventTaskCompletedDict
    | V1AutomateEventTaskMetricsDict
    | V1AutomateEventTaskMetricsIncrementalDict
    | V1AutomateEventTaskSetupDict
    | V1AutomateEventTaskStartedDict
    | V1AutomateEventTaskTraceContextDict
    | V1AutomateEventTaskValidatedDict
    | V1AutomateEventTaskValidationErrorDict
)

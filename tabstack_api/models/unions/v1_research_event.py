from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..v1_research_event_analyzing_end import V1ResearchEventAnalyzingEnd, V1ResearchEventAnalyzingEndDict
from ..v1_research_event_analyzing_start import V1ResearchEventAnalyzingStart, V1ResearchEventAnalyzingStartDict
from ..v1_research_event_complete import V1ResearchEventComplete, V1ResearchEventCompleteDict
from ..v1_research_event_error import V1ResearchEventError, V1ResearchEventErrorDict
from ..v1_research_event_evaluating_end import V1ResearchEventEvaluatingEnd, V1ResearchEventEvaluatingEndDict
from ..v1_research_event_evaluating_start import V1ResearchEventEvaluatingStart, V1ResearchEventEvaluatingStartDict
from ..v1_research_event_following_end import V1ResearchEventFollowingEnd, V1ResearchEventFollowingEndDict
from ..v1_research_event_following_start import V1ResearchEventFollowingStart, V1ResearchEventFollowingStartDict
from ..v1_research_event_iteration_end import V1ResearchEventIterationEnd, V1ResearchEventIterationEndDict
from ..v1_research_event_iteration_start import V1ResearchEventIterationStart, V1ResearchEventIterationStartDict
from ..v1_research_event_judging_end import V1ResearchEventJudgingEnd, V1ResearchEventJudgingEndDict
from ..v1_research_event_judging_start import V1ResearchEventJudgingStart, V1ResearchEventJudgingStartDict
from ..v1_research_event_outlining_end import V1ResearchEventOutliningEnd, V1ResearchEventOutliningEndDict
from ..v1_research_event_outlining_start import V1ResearchEventOutliningStart, V1ResearchEventOutliningStartDict
from ..v1_research_event_planning_end import V1ResearchEventPlanningEnd, V1ResearchEventPlanningEndDict
from ..v1_research_event_planning_start import V1ResearchEventPlanningStart, V1ResearchEventPlanningStartDict
from ..v1_research_event_prefetching_end import V1ResearchEventPrefetchingEnd, V1ResearchEventPrefetchingEndDict
from ..v1_research_event_prefetching_start import V1ResearchEventPrefetchingStart, V1ResearchEventPrefetchingStartDict
from ..v1_research_event_searching_end import V1ResearchEventSearchingEnd, V1ResearchEventSearchingEndDict
from ..v1_research_event_searching_start import V1ResearchEventSearchingStart, V1ResearchEventSearchingStartDict
from ..v1_research_event_start import V1ResearchEventStart, V1ResearchEventStartDict
from ..v1_research_event_writing_end import V1ResearchEventWritingEnd, V1ResearchEventWritingEndDict
from ..v1_research_event_writing_start import V1ResearchEventWritingStart, V1ResearchEventWritingStartDict

V1ResearchEvent: TypeAlias = Annotated[
    (
        Annotated[V1ResearchEventAnalyzingEnd, Tag("analyzing:end")]
        | Annotated[V1ResearchEventAnalyzingStart, Tag("analyzing:start")]
        | Annotated[V1ResearchEventComplete, Tag("complete")]
        | Annotated[V1ResearchEventError, Tag("error")]
        | Annotated[V1ResearchEventEvaluatingEnd, Tag("evaluating:end")]
        | Annotated[V1ResearchEventEvaluatingStart, Tag("evaluating:start")]
        | Annotated[V1ResearchEventFollowingEnd, Tag("following:end")]
        | Annotated[V1ResearchEventFollowingStart, Tag("following:start")]
        | Annotated[V1ResearchEventIterationEnd, Tag("iteration:end")]
        | Annotated[V1ResearchEventIterationStart, Tag("iteration:start")]
        | Annotated[V1ResearchEventJudgingEnd, Tag("judging:end")]
        | Annotated[V1ResearchEventJudgingStart, Tag("judging:start")]
        | Annotated[V1ResearchEventOutliningEnd, Tag("outlining:end")]
        | Annotated[V1ResearchEventOutliningStart, Tag("outlining:start")]
        | Annotated[V1ResearchEventPlanningEnd, Tag("planning:end")]
        | Annotated[V1ResearchEventPlanningStart, Tag("planning:start")]
        | Annotated[V1ResearchEventPrefetchingEnd, Tag("prefetching:end")]
        | Annotated[V1ResearchEventPrefetchingStart, Tag("prefetching:start")]
        | Annotated[V1ResearchEventSearchingEnd, Tag("searching:end")]
        | Annotated[V1ResearchEventSearchingStart, Tag("searching:start")]
        | Annotated[V1ResearchEventStart, Tag("start")]
        | Annotated[V1ResearchEventWritingEnd, Tag("writing:end")]
        | Annotated[V1ResearchEventWritingStart, Tag("writing:start")]
    ),
    WireDiscriminator("event"),
]
"""A Server-Sent Event from /v1/research. Typed discriminated union keyed on event."""

V1ResearchEventDict: TypeAlias = (
    V1ResearchEventAnalyzingEndDict
    | V1ResearchEventAnalyzingStartDict
    | V1ResearchEventCompleteDict
    | V1ResearchEventErrorDict
    | V1ResearchEventEvaluatingEndDict
    | V1ResearchEventEvaluatingStartDict
    | V1ResearchEventFollowingEndDict
    | V1ResearchEventFollowingStartDict
    | V1ResearchEventIterationEndDict
    | V1ResearchEventIterationStartDict
    | V1ResearchEventJudgingEndDict
    | V1ResearchEventJudgingStartDict
    | V1ResearchEventOutliningEndDict
    | V1ResearchEventOutliningStartDict
    | V1ResearchEventPlanningEndDict
    | V1ResearchEventPlanningStartDict
    | V1ResearchEventPrefetchingEndDict
    | V1ResearchEventPrefetchingStartDict
    | V1ResearchEventSearchingEndDict
    | V1ResearchEventSearchingStartDict
    | V1ResearchEventStartDict
    | V1ResearchEventWritingEndDict
    | V1ResearchEventWritingStartDict
)

from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncEventStream,
    AsyncRawClient,
    EventStream,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_event_decoder,
    json_body,
    json_event_decoder,
    param,
    unwrap,
)
from ..errors.research_v1_error import ResearchV1ErrorBody, research_v1_error_mapper
from ..models.unions.v1_research_event import V1ResearchEvent
from ..models.v1_research_request import V1ResearchRequest, V1ResearchRequestDict
from ..server.server import Server


class Research:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ResearchWithRawResponse(client, server, auth)

    def research_v1(
        self, body: V1ResearchRequest | V1ResearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventStream[V1ResearchEvent]:
        """Execute AI-powered research queries that search the web, analyze sources, and synthesize comprehensive
        answers. This endpoint **always streams** responses using Server-Sent Events (SSE).

        **Streaming Response:**
        - All responses are streamed using Server-Sent Events (``text/event-stream``)
        - Real-time progress updates as research progresses through phases

        **Research Modes:**
        - ``fast`` - Quick answers with minimal web searches (default)
        - ``balanced`` - Standard research with multiple iterations

        **Use Cases:**
        - Answering complex questions with cited sources
        - Synthesizing information from multiple web sources
        - Research reports on specific topics
        - Fact-checking and verification tasks

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            SSE stream with research progress and results

        Raises:
            ApiError: Bad request - Invalid query or missing required fields Unauthorized - Invalid or missing Bearer
                token Payment Required - organization is out of credits Too Many Requests - rate limit exceeded Internal
                server error Service unavailable - Research service not configured ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.research_v1(body, request_options=request_options))

    @property
    def with_raw_response(self) -> ResearchWithRawResponse:
        return self._with_raw_response


class AsyncResearch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncResearchWithRawResponse(client, server, auth)

    async def research_v1(
        self, body: V1ResearchRequest | V1ResearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsyncEventStream[V1ResearchEvent]:
        """Execute AI-powered research queries that search the web, analyze sources, and synthesize comprehensive
        answers. This endpoint **always streams** responses using Server-Sent Events (SSE).

        **Streaming Response:**
        - All responses are streamed using Server-Sent Events (``text/event-stream``)
        - Real-time progress updates as research progresses through phases

        **Research Modes:**
        - ``fast`` - Quick answers with minimal web searches (default)
        - ``balanced`` - Standard research with multiple iterations

        **Use Cases:**
        - Answering complex questions with cited sources
        - Synthesizing information from multiple web sources
        - Research reports on specific topics
        - Fact-checking and verification tasks

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            SSE stream with research progress and results

        Raises:
            ApiError: Bad request - Invalid query or missing required fields Unauthorized - Invalid or missing Bearer
                token Payment Required - organization is out of credits Too Many Requests - rate limit exceeded Internal
                server error Service unavailable - Research service not configured ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.research_v1(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncResearchWithRawResponse:
        return self._with_raw_response


class ResearchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def research_v1(
        self, body: V1ResearchRequest | V1ResearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventStream[V1ResearchEvent], ResearchV1ErrorBody]:
        """Execute AI-powered research queries that search the web, analyze sources, and synthesize comprehensive
        answers. This endpoint **always streams** responses using Server-Sent Events (SSE).

        **Streaming Response:**
        - All responses are streamed using Server-Sent Events (``text/event-stream``)
        - Real-time progress updates as research progresses through phases

        **Research Modes:**
        - ``fast`` - Quick answers with minimal web searches (default)
        - ``balanced`` - Standard research with multiple iterations

        **Use Cases:**
        - Answering complex questions with cited sources
        - Synthesizing information from multiple web sources
        - Research reports on specific topics
        - Fact-checking and verification tasks

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/research"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1ResearchRequest | V1ResearchRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_event_decoder[V1ResearchEvent](),
            error_mapper=research_v1_error_mapper,
            request_options=request_options,
        )


class AsyncResearchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def research_v1(
        self, body: V1ResearchRequest | V1ResearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsyncEventStream[V1ResearchEvent], ResearchV1ErrorBody]:
        """Execute AI-powered research queries that search the web, analyze sources, and synthesize comprehensive
        answers. This endpoint **always streams** responses using Server-Sent Events (SSE).

        **Streaming Response:**
        - All responses are streamed using Server-Sent Events (``text/event-stream``)
        - Real-time progress updates as research progresses through phases

        **Research Modes:**
        - ``fast`` - Quick answers with minimal web searches (default)
        - ``balanced`` - Standard research with multiple iterations

        **Use Cases:**
        - Answering complex questions with cited sources
        - Synthesizing information from multiple web sources
        - Research reports on specific topics
        - Fact-checking and verification tasks

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/research"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1ResearchRequest | V1ResearchRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_event_decoder[V1ResearchEvent](),
            error_mapper=research_v1_error_mapper,
            request_options=request_options,
        )

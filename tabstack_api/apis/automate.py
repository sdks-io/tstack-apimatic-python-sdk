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
    async_json_decoder,
    async_json_event_decoder,
    json_body,
    json_decoder,
    json_event_decoder,
    param,
    unwrap,
)
from ..errors.automate_input_v1_error import AutomateInputV1ErrorBody, automate_input_v1_error_mapper
from ..errors.automate_v1_error import AutomateV1ErrorBody, automate_v1_error_mapper
from ..models.unions.v1_automate_event import V1AutomateEvent
from ..models.v1_automate_input_request import V1AutomateInputRequest, V1AutomateInputRequestDict
from ..models.v1_automate_input_response import V1AutomateInputResponse
from ..models.v1_automate_request import V1AutomateRequest, V1AutomateRequestDict
from ..server.server import Server


class Automate:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AutomateWithRawResponse(client, server, auth)

    def automate_input_v1(
        self,
        request_id: str,
        body: V1AutomateInputRequest | V1AutomateInputRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1AutomateInputResponse:
        """Submit a response to an interactive form data request from an in-progress automation task. When the AI agent
        encounters a form requiring user data, it emits an ``interactive:form_data:request`` or
        ``interactive:form_data:error`` SSE event containing a ``requestId``. Use this endpoint to provide the requested
        data or cancel the request.

        **Lifecycle:**
        - Input requests expire after 2 minutes by default
        - Expired or already-answered requests return ``410 Gone``
        - Successful submissions return ``202 Accepted`` (fire-and-forget from caller's perspective)

        Args:
            request_id: The request ID from the interactive:form_data:request SSE event
            body: Input response with field values or cancellation
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Input response accepted and forwarded to the automation task

        Raises:
            ApiError: Bad request - Invalid JSON Unauthorized - Invalid or missing Bearer token Payment Required -
                organization is out of credits Gone - Input request has expired or already been answered Too Many
                Requests - rate limit exceeded Internal server error Service unavailable - Input service not configured
                ``error`` is ``V1ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.automate_input_v1(request_id, body, request_options=request_options))

    def automate_v1(
        self, body: V1AutomateRequest | V1AutomateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventStream[V1AutomateEvent]:
        """Execute AI-powered browser automation tasks using natural language with optional geotargeting. This endpoint
        **always streams** responses using Server-Sent Events (SSE).

        **Streaming Response:**
        - All responses are streamed using Server-Sent Events (``text/event-stream``)
        - Real-time progress updates and results as they're generated

        **Geotargeting:**
        - Optionally specify a country code for geotargeted browsing

        **Use Cases:**
        - Web scraping and data extraction
        - Form filling and interaction
        - Navigation and information gathering
        - Multi-step web workflows
        - Content analysis from web pages

        Args:
            body: Request body with optional geotargeting
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Task executed successfully (always streaming) **Streaming Response using Server-Sent Events:** All responses
            from the automate endpoint are streamed using Server-Sent Events. **Event Format:** - Each event starts with
            ``event: <type>`` followed by ``data: <JSON>`` - Empty lines separate events **Event Types:** **Task
            Events:** - ``start``: Task initialization - ``task:setup``: Task configuration - ``task:started``: Task
            execution begins - ``task:completed``: Task finished successfully - ``task:aborted``: Task was terminated -
            ``task:validated``: Task completion validation - ``task:validation_error``: Validation failed **Agent
            Events:** - ``agent:processing``: Agent thinking/planning - ``agent:status``: Status updates and plans -
            ``agent:step``: Processing step iterations - ``agent:action``: Actions being performed - ``agent:reasoned``:
            Agent reasoning output - ``agent:extracted``: Data extraction results - ``agent:waiting``: Agent waiting for
            operations **Browser Events:** - ``browser:navigated``: Page navigation events - ``browser:action_started``:
            Browser action initiated - ``browser:action_completed``: Browser action finished -
            ``browser:screenshot_captured``: Screenshot taken **System Events:** - ``system:debug_compression``: Debug
            compression info - ``system:debug_message``: Debug messages **Stream Control:** - ``complete``: End of
            stream with results - ``done``: Stream termination - ``error``: Error occurred

        Raises:
            ApiError: Bad request - Invalid task or missing required fields Unauthorized - Invalid or missing Bearer
                token Payment Required - organization is out of credits Too Many Requests - rate limit exceeded Internal
                server error Service unavailable - Automate service not configured ``error`` is ``AutomateResponse |
                RawError``."""
        return unwrap(self._with_raw_response.automate_v1(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AutomateWithRawResponse:
        return self._with_raw_response


class AsyncAutomate:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAutomateWithRawResponse(client, server, auth)

    async def automate_input_v1(
        self,
        request_id: str,
        body: V1AutomateInputRequest | V1AutomateInputRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1AutomateInputResponse:
        """Submit a response to an interactive form data request from an in-progress automation task. When the AI agent
        encounters a form requiring user data, it emits an ``interactive:form_data:request`` or
        ``interactive:form_data:error`` SSE event containing a ``requestId``. Use this endpoint to provide the requested
        data or cancel the request.

        **Lifecycle:**
        - Input requests expire after 2 minutes by default
        - Expired or already-answered requests return ``410 Gone``
        - Successful submissions return ``202 Accepted`` (fire-and-forget from caller's perspective)

        Args:
            request_id: The request ID from the interactive:form_data:request SSE event
            body: Input response with field values or cancellation
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Input response accepted and forwarded to the automation task

        Raises:
            ApiError: Bad request - Invalid JSON Unauthorized - Invalid or missing Bearer token Payment Required -
                organization is out of credits Gone - Input request has expired or already been answered Too Many
                Requests - rate limit exceeded Internal server error Service unavailable - Input service not configured
                ``error`` is ``V1ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.automate_input_v1(request_id, body, request_options=request_options)
        )

    async def automate_v1(
        self, body: V1AutomateRequest | V1AutomateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsyncEventStream[V1AutomateEvent]:
        """Execute AI-powered browser automation tasks using natural language with optional geotargeting. This endpoint
        **always streams** responses using Server-Sent Events (SSE).

        **Streaming Response:**
        - All responses are streamed using Server-Sent Events (``text/event-stream``)
        - Real-time progress updates and results as they're generated

        **Geotargeting:**
        - Optionally specify a country code for geotargeted browsing

        **Use Cases:**
        - Web scraping and data extraction
        - Form filling and interaction
        - Navigation and information gathering
        - Multi-step web workflows
        - Content analysis from web pages

        Args:
            body: Request body with optional geotargeting
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Task executed successfully (always streaming) **Streaming Response using Server-Sent Events:** All responses
            from the automate endpoint are streamed using Server-Sent Events. **Event Format:** - Each event starts with
            ``event: <type>`` followed by ``data: <JSON>`` - Empty lines separate events **Event Types:** **Task
            Events:** - ``start``: Task initialization - ``task:setup``: Task configuration - ``task:started``: Task
            execution begins - ``task:completed``: Task finished successfully - ``task:aborted``: Task was terminated -
            ``task:validated``: Task completion validation - ``task:validation_error``: Validation failed **Agent
            Events:** - ``agent:processing``: Agent thinking/planning - ``agent:status``: Status updates and plans -
            ``agent:step``: Processing step iterations - ``agent:action``: Actions being performed - ``agent:reasoned``:
            Agent reasoning output - ``agent:extracted``: Data extraction results - ``agent:waiting``: Agent waiting for
            operations **Browser Events:** - ``browser:navigated``: Page navigation events - ``browser:action_started``:
            Browser action initiated - ``browser:action_completed``: Browser action finished -
            ``browser:screenshot_captured``: Screenshot taken **System Events:** - ``system:debug_compression``: Debug
            compression info - ``system:debug_message``: Debug messages **Stream Control:** - ``complete``: End of
            stream with results - ``done``: Stream termination - ``error``: Error occurred

        Raises:
            ApiError: Bad request - Invalid task or missing required fields Unauthorized - Invalid or missing Bearer
                token Payment Required - organization is out of credits Too Many Requests - rate limit exceeded Internal
                server error Service unavailable - Automate service not configured ``error`` is ``AutomateResponse |
                RawError``."""
        return unwrap(await self._with_raw_response.automate_v1(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncAutomateWithRawResponse:
        return self._with_raw_response


class AutomateWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def automate_input_v1(
        self,
        request_id: str,
        body: V1AutomateInputRequest | V1AutomateInputRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1AutomateInputResponse, AutomateInputV1ErrorBody]:
        """Submit a response to an interactive form data request from an in-progress automation task. When the AI agent
        encounters a form requiring user data, it emits an ``interactive:form_data:request`` or
        ``interactive:form_data:error`` SSE event containing a ``requestId``. Use this endpoint to provide the requested
        data or cancel the request.

        **Lifecycle:**
        - Input requests expire after 2 minutes by default
        - Expired or already-answered requests return ``410 Gone``
        - Successful submissions return ``202 Accepted`` (fire-and-forget from caller's perspective)

        Args:
            request_id: The request ID from the interactive:form_data:request SSE event
            body: Input response with field values or cancellation
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/automate/{requestID}/input"),
            path_params=[param[str]("requestID", request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1AutomateInputRequest | V1AutomateInputRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[V1AutomateInputResponse],
            error_mapper=automate_input_v1_error_mapper,
            request_options=request_options,
        )

    def automate_v1(
        self, body: V1AutomateRequest | V1AutomateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventStream[V1AutomateEvent], AutomateV1ErrorBody]:
        """Execute AI-powered browser automation tasks using natural language with optional geotargeting. This endpoint
        **always streams** responses using Server-Sent Events (SSE).

        **Streaming Response:**
        - All responses are streamed using Server-Sent Events (``text/event-stream``)
        - Real-time progress updates and results as they're generated

        **Geotargeting:**
        - Optionally specify a country code for geotargeted browsing

        **Use Cases:**
        - Web scraping and data extraction
        - Form filling and interaction
        - Navigation and information gathering
        - Multi-step web workflows
        - Content analysis from web pages

        Args:
            body: Request body with optional geotargeting
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/automate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1AutomateRequest | V1AutomateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_event_decoder[V1AutomateEvent](),
            error_mapper=automate_v1_error_mapper,
            request_options=request_options,
        )


class AsyncAutomateWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def automate_input_v1(
        self,
        request_id: str,
        body: V1AutomateInputRequest | V1AutomateInputRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1AutomateInputResponse, AutomateInputV1ErrorBody]:
        """Submit a response to an interactive form data request from an in-progress automation task. When the AI agent
        encounters a form requiring user data, it emits an ``interactive:form_data:request`` or
        ``interactive:form_data:error`` SSE event containing a ``requestId``. Use this endpoint to provide the requested
        data or cancel the request.

        **Lifecycle:**
        - Input requests expire after 2 minutes by default
        - Expired or already-answered requests return ``410 Gone``
        - Successful submissions return ``202 Accepted`` (fire-and-forget from caller's perspective)

        Args:
            request_id: The request ID from the interactive:form_data:request SSE event
            body: Input response with field values or cancellation
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/automate/{requestID}/input"),
            path_params=[param[str]("requestID", request_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1AutomateInputRequest | V1AutomateInputRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[V1AutomateInputResponse],
            error_mapper=automate_input_v1_error_mapper,
            request_options=request_options,
        )

    async def automate_v1(
        self, body: V1AutomateRequest | V1AutomateRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsyncEventStream[V1AutomateEvent], AutomateV1ErrorBody]:
        """Execute AI-powered browser automation tasks using natural language with optional geotargeting. This endpoint
        **always streams** responses using Server-Sent Events (SSE).

        **Streaming Response:**
        - All responses are streamed using Server-Sent Events (``text/event-stream``)
        - Real-time progress updates and results as they're generated

        **Geotargeting:**
        - Optionally specify a country code for geotargeted browsing

        **Use Cases:**
        - Web scraping and data extraction
        - Form filling and interaction
        - Navigation and information gathering
        - Multi-step web workflows
        - Content analysis from web pages

        Args:
            body: Request body with optional geotargeting
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/automate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1AutomateRequest | V1AutomateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_event_decoder[V1AutomateEvent](),
            error_mapper=automate_v1_error_mapper,
            request_options=request_options,
        )

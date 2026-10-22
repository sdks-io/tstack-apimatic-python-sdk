from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.extract_json_v1_error import ExtractJsonV1ErrorBody, extract_json_v1_error_mapper
from ..errors.extract_markdown_v1_error import ExtractMarkdownV1ErrorBody, extract_markdown_v1_error_mapper
from ..models.v1_extract_jsonrequest import V1ExtractJsonrequest, V1ExtractJsonrequestDict
from ..models.v1_extract_markdown_request import V1ExtractMarkdownRequest, V1ExtractMarkdownRequestDict
from ..models.v1_extract_markdown_response import V1ExtractMarkdownResponse
from ..server.server import Server


class Extract:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ExtractWithRawResponse(client, server, auth)

    def extract_json_v1(
        self,
        body: V1ExtractJsonrequest | V1ExtractJsonrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Fetches a URL and extracts structured data according to a provided JSON schema

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad request - invalid input Unauthorized - Invalid or missing Bearer token Payment Required -
                organization is out of credits Invalid URL or inaccessible resource Too Many Requests - rate limit
                exceeded Server error ``error`` is ``V1ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.extract_json_v1(body, request_options=request_options))

    def extract_markdown_v1(
        self,
        body: V1ExtractMarkdownRequest | V1ExtractMarkdownRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1ExtractMarkdownResponse:
        """Fetches a URL and converts its HTML content to clean Markdown format with optional metadata extraction

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad request - URL is required Unauthorized - Invalid or missing Bearer token Payment Required -
                organization is out of credits Invalid URL or inaccessible resource Too Many Requests - rate limit
                exceeded Server error ``error`` is ``V1ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.extract_markdown_v1(body, request_options=request_options))

    @property
    def with_raw_response(self) -> ExtractWithRawResponse:
        return self._with_raw_response


class AsyncExtract:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncExtractWithRawResponse(client, server, auth)

    async def extract_json_v1(
        self,
        body: V1ExtractJsonrequest | V1ExtractJsonrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Fetches a URL and extracts structured data according to a provided JSON schema

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad request - invalid input Unauthorized - Invalid or missing Bearer token Payment Required -
                organization is out of credits Invalid URL or inaccessible resource Too Many Requests - rate limit
                exceeded Server error ``error`` is ``V1ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.extract_json_v1(body, request_options=request_options))

    async def extract_markdown_v1(
        self,
        body: V1ExtractMarkdownRequest | V1ExtractMarkdownRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1ExtractMarkdownResponse:
        """Fetches a URL and converts its HTML content to clean Markdown format with optional metadata extraction

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad request - URL is required Unauthorized - Invalid or missing Bearer token Payment Required -
                organization is out of credits Invalid URL or inaccessible resource Too Many Requests - rate limit
                exceeded Server error ``error`` is ``V1ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.extract_markdown_v1(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncExtractWithRawResponse:
        return self._with_raw_response


class ExtractWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def extract_json_v1(
        self,
        body: V1ExtractJsonrequest | V1ExtractJsonrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ExtractJsonV1ErrorBody]:
        """Fetches a URL and extracts structured data according to a provided JSON schema

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/extract/json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1ExtractJsonrequest | V1ExtractJsonrequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Any],
            error_mapper=extract_json_v1_error_mapper,
            request_options=request_options,
        )

    def extract_markdown_v1(
        self,
        body: V1ExtractMarkdownRequest | V1ExtractMarkdownRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1ExtractMarkdownResponse, ExtractMarkdownV1ErrorBody]:
        """Fetches a URL and converts its HTML content to clean Markdown format with optional metadata extraction

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/extract/markdown"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1ExtractMarkdownRequest | V1ExtractMarkdownRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[V1ExtractMarkdownResponse],
            error_mapper=extract_markdown_v1_error_mapper,
            request_options=request_options,
        )


class AsyncExtractWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def extract_json_v1(
        self,
        body: V1ExtractJsonrequest | V1ExtractJsonrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ExtractJsonV1ErrorBody]:
        """Fetches a URL and extracts structured data according to a provided JSON schema

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/extract/json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1ExtractJsonrequest | V1ExtractJsonrequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[Any],
            error_mapper=extract_json_v1_error_mapper,
            request_options=request_options,
        )

    async def extract_markdown_v1(
        self,
        body: V1ExtractMarkdownRequest | V1ExtractMarkdownRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1ExtractMarkdownResponse, ExtractMarkdownV1ErrorBody]:
        """Fetches a URL and converts its HTML content to clean Markdown format with optional metadata extraction

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/extract/markdown"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1ExtractMarkdownRequest | V1ExtractMarkdownRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[V1ExtractMarkdownResponse],
            error_mapper=extract_markdown_v1_error_mapper,
            request_options=request_options,
        )

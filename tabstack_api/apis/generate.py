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
from ..errors.generate_json_v1_error import GenerateJsonV1ErrorBody, generate_json_v1_error_mapper
from ..models.v1_generate_jsonrequest import V1GenerateJsonrequest, V1GenerateJsonrequestDict
from ..server.server import Server


class Generate:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GenerateWithRawResponse(client, server, auth)

    def generate_json_v1(
        self,
        body: V1GenerateJsonrequest | V1GenerateJsonrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Fetches URL content, extracts data, and transforms it using AI based on custom instructions. Use this to
        generate new content, summaries, or restructured data.

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
        return unwrap(self._with_raw_response.generate_json_v1(body, request_options=request_options))

    @property
    def with_raw_response(self) -> GenerateWithRawResponse:
        return self._with_raw_response


class AsyncGenerate:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGenerateWithRawResponse(client, server, auth)

    async def generate_json_v1(
        self,
        body: V1GenerateJsonrequest | V1GenerateJsonrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Fetches URL content, extracts data, and transforms it using AI based on custom instructions. Use this to
        generate new content, summaries, or restructured data.

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
        return unwrap(await self._with_raw_response.generate_json_v1(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncGenerateWithRawResponse:
        return self._with_raw_response


class GenerateWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def generate_json_v1(
        self,
        body: V1GenerateJsonrequest | V1GenerateJsonrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GenerateJsonV1ErrorBody]:
        """Fetches URL content, extracts data, and transforms it using AI based on custom instructions. Use this to
        generate new content, summaries, or restructured data.

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/generate/json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1GenerateJsonrequest | V1GenerateJsonrequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Any],
            error_mapper=generate_json_v1_error_mapper,
            request_options=request_options,
        )


class AsyncGenerateWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def generate_json_v1(
        self,
        body: V1GenerateJsonrequest | V1GenerateJsonrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GenerateJsonV1ErrorBody]:
        """Fetches URL content, extracts data, and transforms it using AI based on custom instructions. Use this to
        generate new content, summaries, or restructured data.

        Args:
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/generate/json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1GenerateJsonrequest | V1GenerateJsonrequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[Any],
            error_mapper=generate_json_v1_error_mapper,
            request_options=request_options,
        )

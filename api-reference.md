# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [TabstackApiClient](tabstack_api/client.py)

## Automate

> Source: [Automate](tabstack_api/apis/automate.py)

<details>
<summary><code>def automate_input_v1(request_id: str, body: V1AutomateInputRequest | V1AutomateInputRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> V1AutomateInputResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Submit a response to an interactive form data request from an in-progress automation task. When the AI agent encounters a form requiring user data, it emits an `interactive:form_data:request` or `interactive:form_data:error` SSE event containing a `requestId`. Use this endpoint to provide the requested data or cancel the request.

**Lifecycle:**
- Input requests expire after 2 minutes by default
- Expired or already-answered requests return `410 Gone`
- Successful submissions return `202 Accepted` (fire-and-forget from caller's perspective)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.automate.automate_input_v1("some example string", V1AutomateInputRequest())
    # TODO: Handle 'response' of type V1AutomateInputResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AutomateInputV1ErrorBody
```

**Async**

```python
try:
    response = await async_client.automate.automate_input_v1("some example string", V1AutomateInputRequest())
    # TODO: Handle 'response' of type V1AutomateInputResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AutomateInputV1ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_id</code> | <code>str</code> | The request ID from the interactive:form_data:request SSE event |
| <code>body</code> | <code>[V1AutomateInputRequest](tabstack_api/models/v1_automate_input_request.py) \| [V1AutomateInputRequestDict](tabstack_api/models/v1_automate_input_request.py)</code> | Input response with field values or cancellation |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tabstack_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[V1AutomateInputResponse](tabstack_api/models/v1_automate_input_response.py)</code> -- Input response accepted and forwarded to the automation task

**OnError**: <code>[ApiError](tabstack_api/core/exceptions.py)&#91;[AutomateInputV1ErrorBody](tabstack_api/errors/automate_input_v1_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 402, 410, 429, 500, 503 | <code>[V1ErrorResponse](tabstack_api/models/v1_error_response.py)</code> |
| anything unmapped | <code>[RawError](tabstack_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def automate_v1(body: V1AutomateRequest | V1AutomateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> EventStream[V1AutomateEvent]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Execute AI-powered browser automation tasks using natural language with optional geotargeting. This endpoint **always streams** responses using Server-Sent Events (SSE).

**Streaming Response:**
- All responses are streamed using Server-Sent Events (`text/event-stream`)
- Real-time progress updates and results as they're generated

**Geotargeting:**
- Optionally specify a country code for geotargeted browsing

**Use Cases:**
- Web scraping and data extraction
- Form filling and interaction
- Navigation and information gathering
- Multi-step web workflows
- Content analysis from web pages

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.automate.automate_v1(
        V1AutomateRequest(
            guardrails="browse and extract only, don't interact with repositories",
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
            url="https://github.com/trending",
        ),
    )
    # TODO: Handle 'response' of type EventStream[V1AutomateEvent]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AutomateV1ErrorBody
```

**Async**

```python
try:
    response = await async_client.automate.automate_v1(
        V1AutomateRequest(
            guardrails="browse and extract only, don't interact with repositories",
            task="Find the top 3 trending repositories and extract their names, descriptions, and star counts",
            url="https://github.com/trending",
        ),
    )
    # TODO: Handle 'response' of type AsyncEventStream[V1AutomateEvent]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AutomateV1ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[V1AutomateRequest](tabstack_api/models/v1_automate_request.py) \| [V1AutomateRequestDict](tabstack_api/models/v1_automate_request.py)</code> | Request body with optional geotargeting |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tabstack_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>EventStream&#91;[V1AutomateEvent](tabstack_api/models/unions/v1_automate_event.py)&#93;</code> -- Task executed successfully (always streaming)

**Streaming Response using Server-Sent Events:**
All responses from the automate endpoint are streamed using Server-Sent Events.

**Event Format:**
- Each event starts with `event: <type>` followed by `data: <JSON>`
- Empty lines separate events

**Event Types:**

**Task Events:**
- `start`: Task initialization
- `task:setup`: Task configuration
- `task:started`: Task execution begins
- `task:completed`: Task finished successfully
- `task:aborted`: Task was terminated
- `task:validated`: Task completion validation
- `task:validation_error`: Validation failed

**Agent Events:**
- `agent:processing`: Agent thinking/planning
- `agent:status`: Status updates and plans
- `agent:step`: Processing step iterations
- `agent:action`: Actions being performed
- `agent:reasoned`: Agent reasoning output
- `agent:extracted`: Data extraction results
- `agent:waiting`: Agent waiting for operations

**Browser Events:**
- `browser:navigated`: Page navigation events
- `browser:action_started`: Browser action initiated
- `browser:action_completed`: Browser action finished
- `browser:screenshot_captured`: Screenshot taken

**System Events:**
- `system:debug_compression`: Debug compression info
- `system:debug_message`: Debug messages

**Stream Control:**
- `complete`: End of stream with results
- `done`: Stream termination
- `error`: Error occurred

**OnError**: <code>[ApiError](tabstack_api/core/exceptions.py)&#91;[AutomateV1ErrorBody](tabstack_api/errors/automate_v1_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[AutomateResponse](tabstack_api/models/automate_response.py)</code> |
| 401, 402, 429, 500, 503 | <code>[RawError](tabstack_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](tabstack_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Extract

> Source: [Extract](tabstack_api/apis/extract.py)

<details>
<summary><code>def extract_json_v1(body: V1ExtractJsonrequest | V1ExtractJsonrequestDict, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetches a URL and extracts structured data according to a provided JSON schema

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.extract.extract_json_v1(
        V1ExtractJsonrequest(effort=Effort.STANDARD, json_schema={}, nocache=False, url="https://news.ycombinator.com")
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExtractJsonV1ErrorBody
```

**Async**

```python
try:
    response = await async_client.extract.extract_json_v1(
        V1ExtractJsonrequest(effort=Effort.STANDARD, json_schema={}, nocache=False, url="https://news.ycombinator.com")
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExtractJsonV1ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[V1ExtractJsonrequest](tabstack_api/models/v1_extract_jsonrequest.py) \| [V1ExtractJsonrequestDict](tabstack_api/models/v1_extract_jsonrequest.py)</code> | Request body |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tabstack_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](tabstack_api/core/exceptions.py)&#91;[ExtractJsonV1ErrorBody](tabstack_api/errors/extract_json_v1_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 402, 422, 429, 500 | <code>[V1ErrorResponse](tabstack_api/models/v1_error_response.py)</code> |
| anything unmapped | <code>[RawError](tabstack_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def extract_markdown_v1(body: V1ExtractMarkdownRequest | V1ExtractMarkdownRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> V1ExtractMarkdownResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetches a URL and converts its HTML content to clean Markdown format with optional metadata extraction

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.extract.extract_markdown_v1(V1ExtractMarkdownRequest(url="https://example.com"))
    # TODO: Handle 'response' of type V1ExtractMarkdownResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExtractMarkdownV1ErrorBody
```

**Async**

```python
try:
    response = await async_client.extract.extract_markdown_v1(V1ExtractMarkdownRequest(url="https://example.com"))
    # TODO: Handle 'response' of type V1ExtractMarkdownResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExtractMarkdownV1ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[V1ExtractMarkdownRequest](tabstack_api/models/v1_extract_markdown_request.py) \| [V1ExtractMarkdownRequestDict](tabstack_api/models/v1_extract_markdown_request.py)</code> | Request body |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tabstack_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[V1ExtractMarkdownResponse](tabstack_api/models/v1_extract_markdown_response.py)</code> -- OK

**OnError**: <code>[ApiError](tabstack_api/core/exceptions.py)&#91;[ExtractMarkdownV1ErrorBody](tabstack_api/errors/extract_markdown_v1_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 402, 422, 429, 500 | <code>[V1ErrorResponse](tabstack_api/models/v1_error_response.py)</code> |
| anything unmapped | <code>[RawError](tabstack_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Generate

> Source: [Generate](tabstack_api/apis/generate.py)

<details>
<summary><code>def generate_json_v1(body: V1GenerateJsonrequest | V1GenerateJsonrequestDict, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetches URL content, extracts data, and transforms it using AI based on custom instructions. Use this to generate new content, summaries, or restructured data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.generate.generate_json_v1(
        V1GenerateJsonrequest(
            effort=Effort.STANDARD,
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary describing the story in simple terms.",
            json_schema={},
            nocache=False,
            url="https://news.ycombinator.com",
        ),
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateJsonV1ErrorBody
```

**Async**

```python
try:
    response = await async_client.generate.generate_json_v1(
        V1GenerateJsonrequest(
            effort=Effort.STANDARD,
            instructions="For each story, categorize it (tech/business/science/other) and write a one-sentence summary describing the story in simple terms.",
            json_schema={},
            nocache=False,
            url="https://news.ycombinator.com",
        ),
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateJsonV1ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[V1GenerateJsonrequest](tabstack_api/models/v1_generate_jsonrequest.py) \| [V1GenerateJsonrequestDict](tabstack_api/models/v1_generate_jsonrequest.py)</code> | Request body |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tabstack_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](tabstack_api/core/exceptions.py)&#91;[GenerateJsonV1ErrorBody](tabstack_api/errors/generate_json_v1_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 402, 422, 429, 500 | <code>[V1ErrorResponse](tabstack_api/models/v1_error_response.py)</code> |
| anything unmapped | <code>[RawError](tabstack_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Research

> Source: [Research](tabstack_api/apis/research.py)

<details>
<summary><code>def research_v1(body: V1ResearchRequest | V1ResearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> EventStream[V1ResearchEvent]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Execute AI-powered research queries that search the web, analyze sources, and synthesize comprehensive answers. This endpoint **always streams** responses using Server-Sent Events (SSE).

**Streaming Response:**
- All responses are streamed using Server-Sent Events (`text/event-stream`)
- Real-time progress updates as research progresses through phases

**Research Modes:**
- `fast` - Quick answers with minimal web searches (default)
- `balanced` - Standard research with multiple iterations

**Use Cases:**
- Answering complex questions with cited sources
- Synthesizing information from multiple web sources
- Research reports on specific topics
- Fact-checking and verification tasks

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.research.research_v1(V1ResearchRequest(query="some example string"))
    # TODO: Handle 'response' of type EventStream[V1ResearchEvent]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResearchV1ErrorBody
```

**Async**

```python
try:
    response = await async_client.research.research_v1(V1ResearchRequest(query="some example string"))
    # TODO: Handle 'response' of type AsyncEventStream[V1ResearchEvent]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResearchV1ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[V1ResearchRequest](tabstack_api/models/v1_research_request.py) \| [V1ResearchRequestDict](tabstack_api/models/v1_research_request.py)</code> | Request body |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tabstack_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>EventStream&#91;[V1ResearchEvent](tabstack_api/models/unions/v1_research_event.py)&#93;</code> -- SSE stream with research progress and results

**OnError**: <code>[ApiError](tabstack_api/core/exceptions.py)&#91;[ResearchV1ErrorBody](tabstack_api/errors/research_v1_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 402, 429, 500, 503 | <code>[RawError](tabstack_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](tabstack_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>


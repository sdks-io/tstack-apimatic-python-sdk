<!-- Generated file — do not edit; regenerated with the SDK. -->

# Extract — operations

Accessor: `client.extract` · Source: `tabstack_api/apis/extract.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.extract.extract_json_v1

- **Route**: `POST /extract/json`
- **Auth**: `bearer_auth`
- **Signature**: `def extract_json_v1(body: V1ExtractJsonrequest | V1ExtractJsonrequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, ExtractJsonV1ErrorBody]`
- **Error**: `ExtractJsonV1ErrorBody` — **Case A (typed)**
- **Error arms**: `V1ErrorResponse` [400, 401, 402, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ExtractJsonrequest` | `tabstack_api/models/v1_extract_jsonrequest.py` |
| `V1ExtractJsonrequestDict` | `tabstack_api/models/v1_extract_jsonrequest.py` |
| `ExtractJsonV1ErrorBody` | `tabstack_api/errors/extract_json_v1_error.py` |
| `V1ErrorResponse` | `tabstack_api/models/v1_error_response.py` |

### client.extract.extract_markdown_v1

- **Route**: `POST /extract/markdown`
- **Auth**: `bearer_auth`
- **Signature**: `def extract_markdown_v1(body: V1ExtractMarkdownRequest | V1ExtractMarkdownRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `V1ExtractMarkdownResponse`
- **Returns (raw)**: `ApiResult[V1ExtractMarkdownResponse, ExtractMarkdownV1ErrorBody]`
- **Error**: `ExtractMarkdownV1ErrorBody` — **Case A (typed)**
- **Error arms**: `V1ErrorResponse` [400, 401, 402, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ExtractMarkdownRequest` | `tabstack_api/models/v1_extract_markdown_request.py` |
| `V1ExtractMarkdownRequestDict` | `tabstack_api/models/v1_extract_markdown_request.py` |
| `V1ExtractMarkdownResponse` | `tabstack_api/models/v1_extract_markdown_response.py` |
| `ExtractMarkdownV1ErrorBody` | `tabstack_api/errors/extract_markdown_v1_error.py` |
| `V1ErrorResponse` | `tabstack_api/models/v1_error_response.py` |


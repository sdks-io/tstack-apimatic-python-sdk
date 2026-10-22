<!-- Generated file — do not edit; regenerated with the SDK. -->

# Generate — operations

Accessor: `client.generate` · Source: `tabstack_api/apis/generate.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.generate.generate_json_v1

- **Route**: `POST /generate/json`
- **Auth**: `bearer_auth`
- **Signature**: `def generate_json_v1(body: V1GenerateJsonrequest | V1GenerateJsonrequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GenerateJsonV1ErrorBody]`
- **Error**: `GenerateJsonV1ErrorBody` — **Case A (typed)**
- **Error arms**: `V1ErrorResponse` [400, 401, 402, 422, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1GenerateJsonrequest` | `tabstack_api/models/v1_generate_jsonrequest.py` |
| `V1GenerateJsonrequestDict` | `tabstack_api/models/v1_generate_jsonrequest.py` |
| `GenerateJsonV1ErrorBody` | `tabstack_api/errors/generate_json_v1_error.py` |
| `V1ErrorResponse` | `tabstack_api/models/v1_error_response.py` |


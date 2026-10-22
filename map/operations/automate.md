<!-- Generated file — do not edit; regenerated with the SDK. -->

# Automate — operations

Accessor: `client.automate` · Source: `tabstack_api/apis/automate.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.automate.automate_input_v1

- **Route**: `POST /automate/{requestID}/input`
- **Auth**: `bearer_auth`
- **Signature**: `def automate_input_v1(request_id: str, body: V1AutomateInputRequest | V1AutomateInputRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `request_id`, `body`
- **Params**: `request_id` — path `requestID` · `body` — JSON body
- **Returns (parsed)**: `V1AutomateInputResponse`
- **Returns (raw)**: `ApiResult[V1AutomateInputResponse, AutomateInputV1ErrorBody]`
- **Error**: `AutomateInputV1ErrorBody` — **Case A (typed)**
- **Error arms**: `V1ErrorResponse` [400, 401, 402, 410, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1AutomateInputRequest` | `tabstack_api/models/v1_automate_input_request.py` |
| `V1AutomateInputRequestDict` | `tabstack_api/models/v1_automate_input_request.py` |
| `V1AutomateInputResponse` | `tabstack_api/models/v1_automate_input_response.py` |
| `AutomateInputV1ErrorBody` | `tabstack_api/errors/automate_input_v1_error.py` |
| `V1ErrorResponse` | `tabstack_api/models/v1_error_response.py` |

### client.automate.automate_v1

- **Route**: `POST /automate`
- **Auth**: `bearer_auth`
- **Signature**: `def automate_v1(body: V1AutomateRequest | V1AutomateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `EventStream[V1AutomateEvent]`
- **Returns (raw)**: `ApiResult[EventStream[V1AutomateEvent], AutomateV1ErrorBody]`
- **Error**: `AutomateV1ErrorBody` — **Case A (typed)**
- **Error arms**: `AutomateResponse` [400] · `RawError` [401, 402, 429, 500, 503, anything unmapped]

| Type | Source |
| --- | --- |
| `V1AutomateRequest` | `tabstack_api/models/v1_automate_request.py` |
| `V1AutomateRequestDict` | `tabstack_api/models/v1_automate_request.py` |
| `V1AutomateEvent` | `tabstack_api/models/unions/v1_automate_event.py` |
| `AutomateV1ErrorBody` | `tabstack_api/errors/automate_v1_error.py` |
| `AutomateResponse` | `tabstack_api/models/automate_response.py` |


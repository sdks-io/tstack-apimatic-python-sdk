<!-- Generated file — do not edit; regenerated with the SDK. -->

# Research — operations

Accessor: `client.research` · Source: `tabstack_api/apis/research.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.research.research_v1

- **Route**: `POST /research`
- **Auth**: `bearer_auth`
- **Signature**: `def research_v1(body: V1ResearchRequest | V1ResearchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `EventStream[V1ResearchEvent]`
- **Returns (raw)**: `ApiResult[EventStream[V1ResearchEvent], ResearchV1ErrorBody]`
- **Error**: `ResearchV1ErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 402, 429, 500, 503, anything unmapped]

| Type | Source |
| --- | --- |
| `V1ResearchRequest` | `tabstack_api/models/v1_research_request.py` |
| `V1ResearchRequestDict` | `tabstack_api/models/v1_research_request.py` |
| `V1ResearchEvent` | `tabstack_api/models/unions/v1_research_event.py` |
| `ResearchV1ErrorBody` | `tabstack_api/errors/research_v1_error.py` |


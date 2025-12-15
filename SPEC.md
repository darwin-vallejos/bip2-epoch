\# BIP-2 v1.1 Specification



\## 1. Scope



BIP-2 defines a minimal protocol for multi-party agreement identity using deterministic

hashing over canonical message sets.



It enables:

\- Verifiable agreement epochs

\- Tamper-evident aggregation

\- Deterministic replay and audit



It is NOT a blockchain, consensus algorithm, or transport layer.



\## 2. Core Concepts



\### Epoch

A bounded set of messages produced by independent agents within a shared time window.



\### Message

A canonical JSON object containing:

\- agent\_id

\- timestamp\_utc

\- payload

\- message\_hash



\### Message Hash

SHA-256 hash of the canonical JSON serialization of the message excluding

`message\_hash` and `network\_hash`.



\### Network Hash

SHA-256 hash of the ordered list of all message\_hash values in the epoch.



\## 3. Canonicalization Rules



\- UTF-8 encoding

\- Sorted JSON keys

\- No insignificant whitespace

\- Arrays preserve order



\## 4. Determinism



Identical inputs MUST produce identical hashes across all participants.



\## 5. Non-Goals



\- Consensus resolution

\- Sybil resistance

\- Transport security

\- Blockchain dependency




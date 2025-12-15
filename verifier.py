import json
import hashlib


def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_hex(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def compute_message_hash(message: dict) -> str:
    msg = dict(message)
    msg.pop("message_hash", None)
    msg.pop("network_hash", None)
    return sha256_hex(canonical_json(msg))


def compute_network_hash(messages: list) -> str:
    hashes = [m["message_hash"] for m in messages]
    return sha256_hex(canonical_json(hashes))


def verify_epoch(messages: list) -> bool:
    for m in messages:
        if compute_message_hash(m) != m["message_hash"]:
            return False

    expected = compute_network_hash(messages)
    return all(m["network_hash"] == expected for m in messages)


if __name__ == "__main__":
    print("BIP-2 verifier loaded.")

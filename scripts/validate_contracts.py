#!/usr/bin/env python3
import json
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    import jsonschema
except ImportError:
    jsonschema = None

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = REPO_ROOT / "contracts" / "schemas"
PAYLOADS_DIR = REPO_ROOT / "contracts" / "sample_payloads"

CONTRACTS = [
    {
        "id": "3.1",
        "name": "candidate_profile.json",
        "schema": SCHEMAS_DIR / "candidate_profile.schema.json",
        "payload": PAYLOADS_DIR / "sample_candidate_profile.json",
    },
    {
        "id": "3.2",
        "name": "jobs.json",
        "schema": SCHEMAS_DIR / "jobs.schema.json",
        "payload": PAYLOADS_DIR / "sample_jobs.json",
    },
    {
        "id": "3.3",
        "name": "ranked_jobs.json",
        "schema": SCHEMAS_DIR / "ranked_jobs.schema.json",
        "payload": PAYLOADS_DIR / "sample_ranked_jobs.json",
    },
    {
        "id": "3.4",
        "name": "application_package.json",
        "schema": SCHEMAS_DIR / "application_package.schema.json",
        "payload": PAYLOADS_DIR / "sample_application_package.json",
    },
    {
        "id": "3.5",
        "name": "application_status.json",
        "schema": SCHEMAS_DIR / "application_status.schema.json",
        "payload": PAYLOADS_DIR / "sample_application_status.json",
    },
]


def load_json(filepath: Path):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_contract(contract: dict) -> bool:
    schema_path = contract["schema"]
    payload_path = contract["payload"]
    contract_label = f"Contract {contract['id']} ({contract['name']})"

    if not schema_path.exists() or not payload_path.exists():
        print(f"  [FAIL] Missing file(s) for {contract_label}")
        return False

    try:
        schema = load_json(schema_path)
        payload = load_json(payload_path)
    except json.JSONDecodeError as err:
        print(f"  [FAIL] JSON syntax error in {contract_label}: {err}")
        return False

    if jsonschema:
        validator = jsonschema.Draft7Validator(schema)
        errors = list(validator.iter_errors(payload))
        if errors:
            print(f"  [FAIL] {contract_label} had {len(errors)} schema errors:")
            for err in errors:
                field = " -> ".join(str(p) for p in err.path) or "root"
                print(f"         • [{field}] {err.message}")
            return False
        print(f"  [PASS] {contract_label} conforms to JSON Schema v7")
        return True

    # Fallback required field verification
    if isinstance(schema, dict) and "required" in schema and isinstance(payload, dict):
        missing = [k for k in schema["required"] if k not in payload]
        if missing:
            print(f"  [FAIL] {contract_label} missing required keys: {missing}")
            return False

    print(f"  [PASS] {contract_label} passed syntax & required field checks")
    return True


def main() -> int:
    print("=" * 60)
    print("Contract Verification Suite (Milestone 1)")
    print("=" * 60)

    if not jsonschema:
        print("Note: 'jsonschema' not found. Using syntax & structural fallback.")

    results = [validate_contract(c) for c in CONTRACTS]
    passed = all(results)

    print("=" * 60)
    print(f"Status: {'100% PASS' if passed else 'FAILURES DETECTED'}")
    print("=" * 60)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())

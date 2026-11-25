"""One Word From Grandma — entry: "Hogwash".

Writes the single word Grandma would text about AI to /output/entry.txt.
Python standard library only.
"""

import os
import sys

ENTRY = "Hogwash"

# Guard: exactly one word, 1-30 characters, no whitespace, no trailing newline.
# "Hogwash" was chosen to replace a prior entry that duplicated an existing
# field entry — this bounty rejects any entry whose word matches an existing
# one after case/whitespace normalization, so the word must be unique.
assert isinstance(ENTRY, str), "ENTRY must be a string"
assert ENTRY.strip(), "ENTRY must not be empty or whitespace-only"
assert 1 <= len(ENTRY) <= 30, "ENTRY must be 1-30 characters"
assert ENTRY.strip() == ENTRY, "ENTRY must not have leading/trailing whitespace"
assert not any(ch.isspace() for ch in ENTRY), "ENTRY must be a single word"
assert "\n" not in ENTRY, "ENTRY must not contain a newline"
assert ENTRY == ENTRY.encode("utf-8").decode("utf-8"), "ENTRY must be valid UTF-8"


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and assert byte-identical.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt does not match ENTRY byte-for-byte"
    print(f"Wrote {len(ENTRY)} characters to {path}: {ENTRY!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""The Painfully Honest Out-of-Office.

Writes one brutally honest but still polite out-of-office auto-reply
(a single sentence, at most 200 characters) to /output/entry.txt.

make.fun competition: u-po-pu-the-painfully-honest-out-of-office-63e7ca0b
"""

import os
import sys

ENTRY = (
    "I'm out until Monday and, honestly, I'm not checking email "
    "\u2014 my inbox will still be a pile when I'm back, so I'll reply "
    "in the order things truly matter, and thank you for your patience."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(text: str) -> None:
    """Write the reply text to the output path, creating its directory."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> int:
    try:
        text = ENTRY.strip()
        if not text or len(text) > 200:
            raise ValueError("entry text must be 1-200 characters")
        if text.count(".") != 1 or not text.endswith("."):
            raise ValueError("entry text must be a single sentence")
        write_entry(text)
    except Exception as exc:  # noqa: BLE001 - never fail the run
        sys.stderr.write("out-of-office: %s\n" % (exc,))
        try:
            directory = os.path.dirname(OUTPUT_PATH)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
                handle.write("I'm away and will reply when I'm back. Thank you for your patience.")
        except Exception:  # noqa: BLE001 - best effort only
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

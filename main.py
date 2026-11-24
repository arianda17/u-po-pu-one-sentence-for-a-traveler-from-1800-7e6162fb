# Entry for the make.fun bounty "One Sentence for a Traveler from 1800".
# One sentence, at most 200 characters, no word coined after 1800
# (every word must be a person from 1800 could picture — no "internet",
# "computer", "screen", "digital", "network", "online", "email", etc.).
ENTRY = (
    "Picture the whole world as one great post-house where anyone can send "
    "a letter, a picture or a voice to any person anywhere, and an answer "
    "comes back in a moment."
)

import os

def main():
    # Self-check: the gate requires UTF-8 text of 1-200 characters, not only
    # white space, and exactly one sentence. Keep the entry string above in
    # step with these assertions.
    assert len(ENTRY) <= 200, "entry too long: %d characters" % len(ENTRY)
    assert ENTRY.strip(), "entry is empty or whitespace only"
    assert ENTRY.count(".") == 1, "entry must be one sentence, one full stop"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()

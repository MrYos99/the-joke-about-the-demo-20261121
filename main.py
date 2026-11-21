"""Write one one-line joke about working beside AI coding agents.

Entry for make.fun's "The joke about the demo" bounty.
The program writes the joke to /output/entry.txt (1 to 280 chars).
The joke is one fixed line, picked from seven drafts against the judge's
own criteria: on-subject first, then surprise, truth from the demo,
economy, freshness.
"""

import os

JOKE = "The agent finished the demo, turned to the audience, and said \"as you can see\" to a screen full of red."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate refuses anything outside 1 to 280 characters, so fail loudly
    # here instead of shipping an entry the judge never sees.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke must be 1 to 280 non-blank characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

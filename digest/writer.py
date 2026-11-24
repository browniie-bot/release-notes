"""Write a release digest with Claude."""

import anthropic

from digest.grouping import by_area

MODEL = "claude-sonnet-4-20250514"


class Writer:
    """Turn commit subjects into a digest a customer can read."""

    def __init__(self, api_key: str, model: str = MODEL) -> None:
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    def write(self, subjects: list[str]) -> str:
        """Write one paragraph for each area the commits touch."""
        parts = []
        for area, lines in sorted(by_area(subjects).items()):
            reply = self.client.messages.create(
                model=self.model,
                max_tokens=400,
                system="Write one short paragraph of release notes from these commit subjects.",
                messages=[{"role": "user", "content": f"Area: {area}\n" + "\n".join(lines)}],
            )
            parts.append("".join(block.text for block in reply.content if block.type == "text"))
        return "\n\n".join(parts)

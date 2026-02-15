import re

def clean_text(text: str) -> str:
    # Remove page numbers like "Page 12"
    text = re.sub(r"\bPage\s+\d+\b", " ", text, flags=re.IGNORECASE)

    # Remove standalone numbers
    text = re.sub(r"\n\d+\n", "\n", text)

    # Remove weird slash codes like /H11005
    text = re.sub(r"/H\d+", " ", text)

    # Remove repeated spaces
    text = re.sub(r"\s+", " ", text)

    # Remove very short junk lines
    lines = [
        line.strip()
        for line in text.splitlines()
        if len(line.strip()) > 30
    ]

    return "\n".join(lines)

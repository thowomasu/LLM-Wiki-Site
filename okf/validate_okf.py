from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESERVED = {"index.md", "log.md"}


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    frontmatter = text[4:end].strip()
    values = {}
    for line in frontmatter.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def validate():
    errors = []
    for path in sorted(ROOT.rglob("*.md")):
        if path.name in RESERVED:
            continue
        frontmatter = parse_frontmatter(path)
        if frontmatter is None:
            errors.append(f"{path.relative_to(ROOT)}: missing parseable frontmatter")
            continue
        if not frontmatter.get("type"):
            errors.append(f"{path.relative_to(ROOT)}: missing required type field")

    if errors:
        print("OKF validation failed")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("OKF validation passed")


if __name__ == "__main__":
    validate()

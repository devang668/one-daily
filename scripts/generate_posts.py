from __future__ import annotations

import re
import shutil
import subprocess
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
THOUGHTS_DIR = ROOT / "thoughts"
GENERATED_DIR = ROOT / "_posts" / "generated"
THOUGHT_NOTE_EXCLUDES = {"README.md"}


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def file_commit_date(path: Path) -> date:
    rel_path = path.relative_to(ROOT).as_posix()

    for args in (
        ("log", "-1", "--follow", "--format=%cs", "--", rel_path),
        ("log", "--diff-filter=A", "--follow", "--format=%cs", "--", rel_path),
    ):
        value = run_git(*args)
        if value:
            return date.fromisoformat(value.splitlines()[0].strip())

    return date.today()


def parse_date_from_name(name: str, fallback_year: int) -> date | None:
    stem = Path(name).stem

    patterns = [
        re.compile(r"(?P<year>20\d{2})[-_.](?P<month>\d{1,2})[-_.](?P<day>\d{1,2})"),
        re.compile(r"(?P<month>\d{1,2})[-_.](?P<day>\d{1,2})"),
        re.compile(r"(?P<month>\d{2})(?P<day>\d{2})"),
    ]

    for pattern in patterns:
        match = pattern.search(stem)
        if not match:
            continue

        year = int(match.groupdict().get("year") or fallback_year)
        month = int(match.group("month"))
        day = int(match.group("day"))

        try:
            return date(year, month, day)
        except ValueError:
            return None

    return None


def clean_filename_prefix(stem: str) -> str:
    cleaned = re.sub(r"^(20\d{2}[-_.]\d{1,2}[-_.]\d{1,2}|[\d._-]+)", "", stem)
    cleaned = cleaned.strip(" -_.")
    return cleaned


def title_from_filename(path: Path) -> str:
    stem = clean_filename_prefix(path.stem)
    if not stem:
        return path.stem.strip() or "未命名"

    words = re.sub(r"[-_]+", " ", stem).strip()
    if re.search(r"[A-Za-z]", words):
        return words.title()
    return words


def extract_title_and_body(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = text.split("\n")

    first_index = next((i for i, line in enumerate(lines) if line.strip()), None)
    if first_index is None:
        return (title_from_filename(path), "")

    first_line = lines[first_index].strip()
    body_start = first_index + 1

    if first_line.startswith("#"):
        title = first_line.lstrip("#").strip() or title_from_filename(path)
    elif re.match(r"https?://", first_line, re.IGNORECASE):
        title = title_from_filename(path)
        body_start = first_index
    else:
        title = first_line

    body_lines = lines[body_start:]
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)
    body = "\n".join(body_lines).strip()

    return (title, body)


def slugify(value: str) -> str:
    slug = value.lower()
    slug = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug).strip("-")
    return slug or "note"


def build_front_matter(title: str, post_date: date, source_path: Path) -> str:
    escaped_title = title.replace("\\", "\\\\").replace('"', '\\"')
    return "\n".join(
        [
            "---",
            "layout: post",
            f'title: "{escaped_title}"',
            f"date: {post_date.isoformat()}",
            f"source_path: {source_path.relative_to(ROOT).as_posix()}",
            "---",
            "",
        ]
    )


def collect_note_files() -> list[Path]:
    files: list[Path] = []

    if THOUGHTS_DIR.exists():
        for path in sorted(THOUGHTS_DIR.rglob("*.md")):
            if path.name in THOUGHT_NOTE_EXCLUDES or path.name.startswith("_"):
                continue
            files.append(path)

    return files


def main() -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    for source in collect_note_files():
        commit_date = file_commit_date(source)
        post_date = parse_date_from_name(source.name, commit_date.year) or commit_date
        title, body = extract_title_and_body(source)
        slug = slugify(clean_filename_prefix(source.stem) or title)
        target = GENERATED_DIR / f"{post_date.isoformat()}-{slug}.md"

        output = build_front_matter(title, post_date, source)
        if body:
            output += body.rstrip() + "\n"

        target.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()

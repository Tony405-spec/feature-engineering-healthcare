from __future__ import annotations

import json
from pathlib import Path


def validate_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid notebook JSON ({exc})"]

    if notebook.get("nbformat") is None:
        errors.append(f"{path}: missing nbformat")
    if not isinstance(notebook.get("cells"), list):
        errors.append(f"{path}: missing cells list")

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    notebooks = sorted(repo_root.glob("*.ipynb"))
    errors = [error for notebook in notebooks for error in validate_notebook(notebook)]

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Validated {len(notebooks)} notebook(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

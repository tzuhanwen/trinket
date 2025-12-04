import os
from pathlib import Path

import __main__


def find_upwards(file_name: str, start_dir: str | None = None) -> Path | None:
    """Find target file along parents, return None if not found."""

    if start_dir is None:
        file = getattr(__main__, "__file__", None)
        if file is not None:
            start_path = Path(file).parent
        else:
            start_path = Path(os.getcwd())
    else:
        start_path = Path(start_dir).resolve()

    paths = [start_path] + list(start_path.parents)

    for parent in paths:
        candidate = parent / file_name
        if candidate.exists():
            return candidate

    return None

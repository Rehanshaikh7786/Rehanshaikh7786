from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).parent
print("Rehan Shaikh GitHub profile asset check")
for name in ("README.md", "dark.svg", "light.svg"):
    path = root / name
    if not path.exists():
        raise FileNotFoundError(name)
    print(f"[OK] {name}")
print("Checked:", datetime.now(timezone.utc).isoformat())

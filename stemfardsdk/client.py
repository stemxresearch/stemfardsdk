from typing import Any, Dict


class Result:
    """Wrapper for matrix analysis results with attribute-style access, including nested dicts."""

    def __init__(self, data: Dict[str, Any]):
        self._data = {
            k: Result(v) if isinstance(v, dict) else v
            for k, v in data.items()
        }

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        raise AttributeError(
            f"'Result' object has no attribute '{name}'. "
            f"Available attributes are: {', '.join(self._data.keys())}"
        )

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __dir__(self):
        return list(self._data.keys()) + list(super().__dir__())

    def keys(self):
        return self._data.keys()

    def items(self):
        return self._data.items()

    def as_dict(self) -> Dict[str, Any]:
        """Recursively convert to dictionary."""
        return {
            k: v.as_dict() if isinstance(v, Result) else v
            for k, v in self._data.items()
        }

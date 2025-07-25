import requests
from typing import List, Union
from .config import BASE_URL
from .client import Result

def matrix_operations(
    a, b, operation,
    decimals: int = 8,
) -> Result:
    """
    
    """
    api_name = "Matrix operations"
    url = f"{BASE_URL}/linear-algebra/matrix-operations"
    payload = {
        "array_a": a,
        "array_b": b,
        "operation": operation,
        "decimals": decimals
    }

    response = requests.post(url, json=payload)
    if not response.ok:
        try:
            detail = response.json()["detail"]
            raise RuntimeError(f"{api_name} error: {detail}")
        except Exception:
            raise RuntimeError(f"Error {response.status_code}: {response.text}")

    return Result(response.json())

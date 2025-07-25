import requests
from .config import BASE_URL
from .client import Result

def matrix_analysis(A, decimals: int = 8) -> Result:
    """
    
    """
    api_name = "Matrix analysis"
    url = f"{BASE_URL}/linear-algebra/matrix-analysis"
    payload = {
        "A": A,
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
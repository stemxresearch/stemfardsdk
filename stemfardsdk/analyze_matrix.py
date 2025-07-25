import requests
from typing import List, Union
from .config import BASE_URL
from .client import Result

def analyze_matrix(
    array: List[List[Union[int, float, str]]],
    decimals: int = 8,
) -> Result:
    """
    Analyze a matrix via FastAPI backend and return results with attribute access.

    Parameters
    ----------
    array : list of list of int/float/str
        Matrix to be analyzed.
    decimals : int, optional (default=8)
        Number of decimal places to round results.

    Returns
    -------
    Result
        Object containing all matrix properties accessible via dot notation.

    Raises
    ------
    RuntimeError
        If request fails or backend returns an error.
        
    Examples
    --------
    >>> from stemfardsdk import analyze_matrix
    >>> matrix = [[1, 2], [3, 4]]
    >>> result = analyze_matrix(matrix)
    >>> print(result.determinant)
    -2.0

    >>> print(result.svd.U)
    [[-0.4045, -0.9145], [-0.9145, 0.4045]]

    >>> print(result.as_dict()["trace"])
    5.0
    """
    api_name = "Matrix analysis"
    url = f"{BASE_URL}/linear-algebra/analyze-matrix"
    payload = {
        "array": array,
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

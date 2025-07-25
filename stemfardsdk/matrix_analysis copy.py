from typing import Dict, List, Union

from stemfardsdk.core import response_result
from .config import BASE_URL
from .client import Result


def matrix_analysis(
    A: List,
    as_dict: bool = True,
    decimals: int = 8,
) -> Union[Dict, Result]:
    """
    Perform matrix analysis on a given matrix A using a remote API.

    Sends matrix `A` to the matrix analysis endpoint and returns key 
    properties such as rank, determinant, inverse, trace, 
    eigenvalues, etc., depending on the backend implementation.

    Parameters
    ----------
    A : List
        The matrix to be analyzed, represented as a list of lists.

    as_dict : bool, default=True
        If True, return the result as a dictionary.
        If False, wrap the result using the `Result` class.

    decimals : int, default=8
        Number of decimal places to round the numeric results.

    Returns
    -------
    dict or Result
        The matrix analysis results in dictionary format or as 
        a `Result` object.
    
    Examples
    --------
    >>> from stemfardsdk.linear_algebra import matrix_analysis

    >>> A = [[1, 2], [3, 4]]

    >>> res = matrix_analysis(A, as_dict=True)
    >>> print(res)

    >>> res = matrix_analysis(A, as_dict=False)
    >>> print(res.result)
    """
    api_name = "Matrix analysis"
    url = f"{BASE_URL}/linear-algebra/matrix-analysis"
    payload = {
        "A": A,
        "decimals": decimals
    }

    result = response_result(
        url=url, payload=payload, api_name=api_name, as_dict=as_dict
    )
    
    return result
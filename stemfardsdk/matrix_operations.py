from typing import Dict, List, Union

from stemfardsdk.core import response_result
from .config import BASE_URL
from .client import Result


def matrix_operations(
    A: List,
    B: List,
    operation: str,
    as_dict: bool,
    decimals: int = 8
) -> Union[Dict, Result]:
    """
    Perform a matrix operation using a remote linear algebra API.

    Sends two matrices `a` and `b` along with the operation to be 
    performed (e.g., addition, subtraction, multiplication) to the 
    server, and returns the result either as a dictionary or 
    a `Result` object.

    Parameters
    ----------
    A : List
        The first matrix, represented as a list of lists.

    B : List
        The second matrix, represented as a list of lists.

    operation : str
        The matrix operation to perform. Supported values include:
        'add', 'subtract', 'multiply', 'divide', 'raise'.

    as_dict : bool, default=True
        Whether to return the result as a dictionary or as a `Result` 
        object.

    decimals : int, optional, default=8
        Number of decimal places to round numerical results to.

    Returns
    -------
    dict or Result
        The result of the matrix operation, either as a dictionary or 
        a `Result` object.

    Raises
    ------
    RuntimeError
        If the HTTP request fails or returns an error response from 
        the API.

    Examples
    --------
    >>> from stemfardsdk.linear_algebra import matrix_operations

    >>> A = [[1, 2], [3, 4]]
    >>> B = [[5, 6], [7, 8]]

    >>> # Perform matrix addition and return as a dictionary
    >>> result = matrix_operations(A=A, B=B, operation="add", as_dict=True)
    >>> print(result)

    >>> # Perform multiplication and return as a Result object
    >>> res = matrix_operations(A=A, B=B, operation="multiply", as_dict=False)
    >>> print(res.result)
    [[19, 22], [43, 50]]
    """
    api_name = "Matrix operations"
    url = f"{BASE_URL}/linear-algebra/matrix-operations"
    payload = {
        "A": A,
        "B": B,
        "operation": operation,
        "decimals": decimals
    }

    result = response_result(
        url=url, payload=payload, api_name=api_name, as_dict=as_dict
    )
    
    return result
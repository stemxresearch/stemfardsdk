from typing import Dict
from fastapi import requests
from stemfardsdk.client import Result


def response_result(
    url: str, payload, api_name: str = "API", as_dict: bool = True
) -> Dict | Result:
    """
    Converts a response or dictionary into a Result object or plain 
    dictionary.

    Parameters
    ----------
    result : Union[dict, requests.Response]
        A dictionary or HTTP response containing JSON data.

    as_dict : bool, default=True
        If True, returns a dictionary.
        If False, wraps the result using the Result class.

    Returns
    -------
    dict or Result
        The processed result.
    """
    response = requests.post(url, json=payload)
    if not response.ok:
        try:
            detail = response.json().get("detail", "Unknown error")
            raise RuntimeError(f"{api_name} error: {detail}")
        except Exception:
            raise RuntimeError(f"Error {response.status_code}: {response.text}")
    
    result = response.json()

    return result if as_dict else Result(result)
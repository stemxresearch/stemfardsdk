from typing import Dict
import requests

from stemfardsdk.client import Result


def response_result(
    url: str, payload: Dict, api_name: str = "API", as_dict: bool = True
) -> Dict | Result:
    """
    Sends a POST request to a given API endpoint and returns the result.

    This function abstracts the process of sending an HTTP POST 
    request to a JSON API, handling any HTTP or response parsing 
    errors, and optionally converting the result into a custom 
    `Result` object.

    Parameters
    ----------
    url : str
        The URL endpoint of the API to which the POST request is sent.

    payload : dict
        The JSON payload to include in the body of the POST request.

    api_name : str, default='API'
        A human-readable name of the API used in error messages 

    as_dict : bool, default=True
        If True, the function returns the response as a plain 
        dictionary. If False, the result is wrapped in a `Result` 
        object from `stemfardsdk.client`.

    Returns
    -------
    dict or Result
        The parsed JSON response from the API, either as a dictionary 
        or a `Result` object depending on the `as_dict` flag.

    Raises
    ------
    RuntimeError
        If the request fails (non-2D status code), or if the response 
        cannot be parsed as JSON.
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
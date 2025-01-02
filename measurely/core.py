from typing import Dict, TypedDict
from requests import request


# Define the structure for the metric payload to be sent to the API
class CapturePayload(TypedDict):
    value: int  # The metric value to be recorded
    filters : Dict[str, str] # Optional filters for categorizing the metric.


# Define the structure for the result returned from the API after capturing a metric
class CaptureResult(TypedDict):
    success: bool  # Indicates whether the API call was successful
    message: str  # Contains the server's response or an error message



# The Measurely class provides methods for interacting with the Measurely API
class Measurely:
    # Class variable to store the API key
    api_key: str = ""

    @staticmethod
    def init(NEW_API_KEY: str):
        """
        Initializes the Measurely package with your application API key.
        This method must be called before using other functions.
        """
        Measurely.api_key = NEW_API_KEY

    @staticmethod
    def capture(metric_identifier: str, payload: CapturePayload) -> CaptureResult:
        """
        Sends a metric to Measurely for tracking.

        Parameters:
        - metric_identifier: The unique identifier for the metric you are capturing.
        - payload: A CapturePayload object containing the metric value.

        Returns:
        - A CaptureResult object indicating the success or failure of the API call.
        """
        # Check if the API key is set, if not, return an error message
        if Measurely.api_key == "":
            return CaptureResult(
                success=False, message="Missing API KEY, please call the init function"
            )

        # Send the metric data to the Measurely API
        response = request(
            "POST",  # Changed "POS" to "POST" for correct HTTP method
            f"https://api.measurely.dev/event/v1/{metric_identifier}",  # Endpoint URL with the metric identifier
            data=payload,  # The metric payload to be sent
            headers={
                "Content-Type": "application/json",
                "Authorization": Measurely.api_key,
            },
        )

        # Check the response status to determine if the API call was successful
        success = False
        if response.status_code == 200:  # HTTP status 200 indicates success
            success = True

        # Return the result of the API call
        return CaptureResult(success=success, message=response.text)

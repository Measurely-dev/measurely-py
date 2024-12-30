# Measurely-py

Measurely-py is a lightweight Python library for interacting with the Measurely API, enabling developers to manage and track custom metrics programmatically using Python.

## Installation

To use the Measurely package in your Python project, you can install it using pip:

```bash
pip install measurely-py
```

## Usage

### 1. Initialize the Measurely package

Before you can send any metrics to Measurely, you need to initialize the package with your API key. The `init` method accepts your API key as a string and sets it for use in subsequent API calls.

```python
from measurely import Measurely

# Initialize the Measurely package with your API key
Measurely.init("YOUR_API_KEY")
```

### 2. Send a Metric (Capture)

The `capture` method is used to send metric data to Measurely. You need to pass the metric identifier (which is a unique name or ID for the metric) and the metric value you want to track.

#### Example of sending a metric

```python
from measurely import Measurely, CapturePayload

# Initialize the Measurely package with your API key
Measurely.init("YOUR_API_KEY")

# Create a metric payload
payload = CapturePayload(value=42)

# Capture the metric and get the result
result = Measurely.capture("example_metric", payload)

# Handle the result
if result["success"]:
    print("Metric captured successfully!")
else:
    print(f"Error capturing metric: {result['message']}")
```

### 3. Error Handling

The `capture` method returns a `CaptureResult` dictionary that contains two fields:

- `success` (bool): Indicates if the API call was successful.
- `message` (str): Contains the response message from the server, which could either be a success message or an error message.

## API Reference

#### `init(NEW_API_KEY: str)`

- **Description**: Initializes the Measurely package with your API key.
- **Parameters**:
  - `NEW_API_KEY`: The API key provided by Measurely.
- **Returns**: None.

#### `capture(metric_identifier: str, payload: CapturePayload) -> CaptureResult`

- **Description**: Sends a metric value to Measurely for tracking.
- **Parameters**:
  - `metric_identifier`: The unique identifier for the metric you are capturing.
  - `payload`: A `CapturePayload` object that contains the metric value to be recorded.
- **Returns**: A `CaptureResult` dictionary that contains the success status and response message.

### Types

#### `CapturePayload`

```python
from typing import TypedDict

class CapturePayload(TypedDict):
    value: int  # The metric value to be recorded.
```

- **Description**: This class defines the data payload that is sent to the Measurely API when capturing a metric.
- **Fields**:
  - `value` (int): The metric value that you want to track.

#### `CaptureResult`

```python
class CaptureResult(TypedDict):
    success: bool  # Indicates if the API call was successful
    message: str   # Contains the server's response or an error message
```

- **Description**: This class represents the result of the API call to capture a metric.
- **Fields**:
  - `success` (bool): Indicates if the metric capture was successful.
  - `message` (str): Contains the server's response or an error message.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to improve the [library](https://github.com/measurely-dev/measurely-py.git).

## License

This library is licensed under the MIT License.

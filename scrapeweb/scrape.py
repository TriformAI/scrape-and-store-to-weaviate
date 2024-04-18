import json
import requests


def handler(event, context):
    # Extract the URL from the 'event' dict using a key, allowing for graceful failure if the key isn't present.
    input = event.get("input_0")

    # Validate the input to ensure there's a URL to process. If not, immediately return an error in JSON format.
    if not input:
        return json.dumps({"error": "No http link provided"})

    # Perform an HTTP GET request using the 'requests' library, which simplifies web requests over built-in alternatives.
    response = requests.get(url=input)

    # Decode the binary response content to a UTF-8 string, the default encoding for web content.
    content_str = response.content.decode("utf-8")

    # Return the webpage content as a JSON string, using indentation for readability in the output.
    return json.dumps({"output_0": content_str}, indent=2)

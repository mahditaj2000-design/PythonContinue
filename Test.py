
import requests
import json

# Define the inputBody and headers
input_body = {
    "tasks": {
        "import": {
            "operation": "import/upload"
        },
        "compress": {
            "operation": "compress",
            "input": "import",
            "input_format": "mp3",
            "output_format": "mp3",
            "options": {
                "compression_method": "percentage",
                "target_size_percentage": 40
            }
        },
        "export-url": {
            "operation": "export/url",
            "input": [
                "compress"
            ]
        }
    }
} 

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer {access-token}'
}

url = "https://api.freeconvert.com/v1/process/jobs"

# Make a POST request and print the response
response = requests.post(url, data=json.dumps(input_body), headers=headers)

if response.status_code == 200:
    response_json = response.json()
    print(response_json)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)



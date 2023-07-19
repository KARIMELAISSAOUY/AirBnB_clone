import requests

def validate_html(html_code):
    url = "https://validator.w3.org/nu/?out=json"
    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "User-Agent": "W3C_Validator/1.0"
    }
    data = html_code.encode("utf-8")

    response = requests.post(url, headers=headers, data=data)
    result = response.json()

    if response.status_code == 200:
        if result["messages"]:
            for message in result["messages"]:
                print(f"{message['type'].capitalize()}: {message['message']} at line {message['lastLine']}")
        else:
            print("No validation errors found.")
    else:
        print("An error occurred while connecting to the validator.")

# Example usage
html = """
<!DOCTYPE html>
<html>
<head>
    <title>W3C Validator Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
    <p>alx</p>
</body>
</html>
"""

validate_html(html)

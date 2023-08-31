import requests

url = "http://143.110.242.113:5001/api/messages"  # Replace with your server's URL
data = {"message": "Hello ME"}
response = requests.post(url, json=data)
response_data = response.json()  # Parse the JSON response

# Print the server response message
print("Server Response:", response_data.get("response_message", "No response"))
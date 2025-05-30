import http.client

# Create a new connection for each request (Non-Persistent)
conn = http.client.HTTPConnection("example.com")

# Send the request
conn.request("GET", "/")

# Get the response
response = conn.getresponse()
print("Status:", response.status)
print("Data:", response.read().decode())

# Close the connection
conn.close()
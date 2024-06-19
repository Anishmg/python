import base64

# Username and password
username = 'poojasoundar2003@gmail.com'
password = 'divshellohello10'

# Concatenate username and password with colon separator
credentials = f"{username}:{password}"

# Encode the credentials string using UTF-8 encoding and then encode with Base64
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Print the encoded credentials
print("Encoded credentials:", encoded_credentials)

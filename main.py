import os
import requests

AWS_CONTAINER_AUTHORIZATION_TOKEN = os.getenv("AWS_CONTAINER_AUTHORIZATION_TOKEN")
AWS_CONTAINER_CREDENTIALS_FULL_URI = os.getenv("AWS_CONTAINER_CREDENTIALS_FULL_URI")

resp = requests.get(
    url = AWS_CONTAINER_CREDENTIALS_FULL_URI,
    headers = {"Authorization": AWS_CONTAINER_AUTHORIZATION_TOKEN}
)
resp = resp.json()

print(f'export AWS_ACCESS_KEY_ID={resp["AccessKeyId"]};')
print(f'export AWS_SECRET_ACCESS_KEY={resp["SecretAccessKey"]};')
print(f'export AWS_SESSION_TOKEN={resp["Token"]};')

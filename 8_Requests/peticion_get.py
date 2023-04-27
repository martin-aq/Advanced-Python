import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "python"}
)
print(response.status_code)
print(response.json())

data = response.json()
print(data.keys())

# print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.content)
# print(response.json()["current_user_url"])

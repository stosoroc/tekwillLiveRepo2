import requests

response = requests.get(
    'https://www.google.com/'
)
print(response)
print()

for k, v in response.headers.items():
    print(k, v)

for k, v in response.cookies.items():
    print(k, v)

for k, v in response.request.headers.items():
    print('Req header: ', k, v)

response2 = requests.get(
    'https://www.google.com/search',
    params={'q': 'Wikipeda'},

    cookies=response.cookies
)

print(response2)
print()

for k, v in response2.cookies.items():
    print(k, v)

print()

# print(response2.content)

with open('file.html', 'wb') as f:
    f.write(response2.content)

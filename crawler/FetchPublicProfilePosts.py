import requests

# Replace 'your_access_token' with the access token you obtained
access_token = 'EAAJfTdrYTSkBO0rU0MYjPp5Nr0ra0ABN8MDJbpmjd5QzIaXeeFLXDsL7ys03O6xZChAPQrv1gMA3damIJHGvYrCcHMT79BPsQ5fgMKHb0W0JkJpagu6bHgBnUZAWz13zAGcYK3A5vxoUFMtdBOZACgki4mT2Lw6aPWjLlRoZA5hQmAwHogueRr21NsEYatngBXzk3k6K67Oo1ZCvow28X9dB59hqmxnal8K43URF3vZCJBZCE93F0gv04dJVCYeUQZDZD'
user_id = 'chamok.hasan'

# Specify the fields you want to retrieve
fields = 'id,message,created_time'

# Make a GET request to retrieve posts from the user's profile
url = f'https://graph.facebook.com/v12.0/{user_id}/feed'
params = {'access_token': access_token, 'fields': fields}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for post in data.get('data', []):
        print(post)
else:
    print(f"Error: {response.status_code}")
    print(response.text)


# https://pypi.org/project/python-facebook-api/0.9.0/
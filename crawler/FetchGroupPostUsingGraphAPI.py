import requests

# Replace 'access_token' with a valid access token generated through the Facebook Graph API Explorer
access_token = 'EAAJfTdrYTSkBOxk1jcMwsxHLmNUbCsTrugSHti05lDW8jkLbbgSMnBJebYZAxdoKEbZB323CUIOH32rM1zZCUh5ZCaZAzXjcTj8H72aIWkTFMxnI8g6ZCCLIQsHQ5XSztj0fU14FMVUP2x4FaD6aKuZCVJNNJ41e2VMH9DofdIyPLRuSZABPlN1fDpZACsSFoDqtg1R6FDCu077oAmMNoJwZDZD'
group_id = '1590338747870221'

# Specify the fields you want to retrieve
fields = 'id,message,created_time'

# Make a GET request to retrieve posts from the group
url = f'https://graph.facebook.com/v12.0/{group_id}/feed'
params = {'access_token': access_token, 'fields': fields}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for post in data.get('data', []):
        print(post)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
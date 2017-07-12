import requests
from constants import base_url,app_access_token
def fetch_user_id(insta_username):
    request_url = ( base_url+ 'users/search?q=%s&access_token=%s') % (insta_username, app_access_token)
    print ('GET request url : %s' % (request_url))
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:

        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None

    else:
        print ('Status code other than 200 received!')
        exit()

import requests
from constants import base_url,app_access_token
# Function to retrieve own post id

def fetch_own_post_id():
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (app_access_token)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            return own_media['data'][0]['id']
        else:
            print ('Post does not exist!')
    else:
        print ('Status code other than 200 received!')
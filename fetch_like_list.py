import requests
from get_post_id import get_post_id
from constants import base_url,app_access_token

# Working
# 5. Function declaration to get a list of the likers for a particular post.

def fetch_like_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (base_url + 'media/%s/likes?access_token= %s') % (media_id,app_access_token )
    print 'GET request url : %s' % (request_url)
    list_of_likes_info = requests.get(request_url).json()

    if list_of_likes_info['meta']['code'] == 200:

        if len(list_of_likes_info['data']):
            for x in range(len(list_of_likes_info['data'])):
                print 'list of likes is %s' % (list_of_likes_info['data'][x]['username'])
        else:
            print ('likes does not exist.')

    else:
        print ('status code other than 200 received.')
